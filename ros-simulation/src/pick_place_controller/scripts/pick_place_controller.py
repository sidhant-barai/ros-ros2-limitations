#!/usr/bin/env python3

import sys
import rospy
import moveit_commander
import geometry_list_utils # For custom matrix conversions if needed
from geometry_msgs.msg import Pose, PoseStamped
from std_srvs.srv import Empty

class UR10ePickPlaceController(object):
    """
    Kinematic Controller for UR10e + Robotiq 2F-140 Pick and Place Sequence
    Utilizes MoveIt! Commander for path planning and joint trajectory execution.
    """
    def __init__(self):
        super(UR10ePickPlaceController, self).__init__()

        # Initialize moveit_commander and ROS node
        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node('ur10e_pick_place_controller', anonymous=True)

        # Instantiate MoveGroupCommanders for the UR10e arm and the gripper
        self.robot = moveit_commander.RobotCommander()
        self.scene = moveit_commander.PlanningSceneInterface()
        
        self.arm_group = moveit_commander.MoveGroupCommander("manipulator")
        self.gripper_group = moveit_commander.MoveGroupCommander("gripper")

        # Set planning parameters for smooth, predictable trajectories
        self.arm_group.set_planning_time(5.0)
        self.arm_group.set_num_planning_attempts(10)
        self.arm_group.set_max_velocity_scaling_factor(0.3)  # Safe speed limit
        self.arm_group.set_max_acceleration_scaling_factor(0.2)

        rospy.loginfo("UR10e Pick & Place Controller Initialized successfully.")

    def set_gripper_state(self, state):
        """
        Actuates gripper to predefined joint states (Open/Closed).
        """
        rospy.loginfo(f"Sending gripper command: {state}")
        joint_goal = self.gripper_group.get_current_joint_values()
        
        if state == "open":
            # Target joint values representing an open state (0.0 rad)
            joint_goal = [0.0] * len(joint_goal)
        elif state == "close":
            # Target joint values representing closed around the target object
            joint_goal = [0.7] * len(joint_goal)  # Approximate Robotiq closure limit
        
        self.gripper_group.go(joint_goal, wait=True)
        self.gripper_group.stop()

    def move_to_pose(self, x, y, z, rx, ry, rz, rw):
        """
        Plans and executes an end-effector trajectory to a target Cartesian Pose.
        """
        pose_goal = Pose()
        pose_goal.position.x = x
        pose_goal.position.y = y
        pose_goal.position.z = z
        pose_goal.orientation.x = rx
        pose_goal.orientation.y = ry
        pose_goal.orientation.z = rz
        pose_goal.orientation.w = rw

        self.arm_group.set_pose_target(pose_goal)
        
        # Plan the trajectory
        success, plan, planning_time, error_code = self.arm_group.plan()
        
        if success:
            rospy.loginfo("Cartesian path planned. Executing trajectory...")
            self.arm_group.execute(plan, wait=True)
            self.arm_group.stop()
            self.arm_group.clear_pose_targets()
            return True
        else:
            rospy.logerr("Path planning failed.")
            return False

    def execute_sequence(self):
        """
        Executes complete pick, lift, move, and place sequence.
        """
        # Step 1: Initialize at Home joint configurations
        rospy.loginfo("Step 1: Moving to Home Position...")
        self.arm_group.set_named_target("home")
        self.arm_group.go(wait=True)
        self.set_gripper_state("open")
        rospy.sleep(1.0)

        # Step 2: Approach Pick Position (Z offset)
        rospy.loginfo("Step 2: Approaching pick location...")
        # Coordinates match simulated workspace target object position
        self.move_to_pose(0.5, -0.2, 0.35, 0.0, 1.0, 0.0, 0.0) 
        
        # Step 3: Descend to target & Close Gripper
        rospy.loginfo("Step 3: Descending to grasp...")
        self.move_to_pose(0.5, -0.2, 0.22, 0.0, 1.0, 0.0, 0.0) 
        self.set_gripper_state("close")
        rospy.sleep(1.0)

        # Step 4: Lift with payload
        rospy.loginfo("Step 4: Post-grasp ascent...")
        self.move_to_pose(0.5, -0.2, 0.40, 0.0, 1.0, 0.0, 0.0)

        # Step 5: Translate to Place Position
        rospy.loginfo("Step 5: Moving to place location...")
        self.move_to_pose(0.2, 0.5, 0.40, 0.0, 1.0, 0.0, 0.0)

        # Step 6: Descend and Open Gripper
        rospy.loginfo("Step 6: Lowering payload to target platform...")
        self.move_to_pose(0.2, 0.5, 0.24, 0.0, 1.0, 0.0, 0.0)
        self.set_gripper_state("open")
        rospy.sleep(1.0)

        # Step 7: Return to Home
        rospy.loginfo("Step 7: Retracting and returning home...")
        self.move_to_pose(0.2, 0.5, 0.40, 0.0, 1.0, 0.0, 0.0)
        self.arm_group.set_named_target("home")
        self.arm_group.go(wait=True)
        
        rospy.loginfo("Pick and Place sequence complete!")

if __name__ == '__main__':
    try:
        controller = UR10ePickPlaceController()
        controller.execute_sequence()
    except rospy.ROSInterruptException:
        pass
