# ROS1 UR10e + Robotiq Manipulator Stack

This subdirectory contains the ROS1 (Noetic) implementation of the industrial pick-and-place workspace pipeline using the **UR10e Cobot** and a **Robotiq 2F-140 Parallel Gripper**. 

The simulation environment runs inside **Gazebo** with motion planning, joint trajectory calculation, and collision avoidance handled entirely via the **MoveIt! Motion Planning Framework**.

---

## 🛠️ Kinematic & Control Architecture
- **Robot Arm:** Universal Robots UR10e (6-DOF)
- **End-Effector:** Robotiq 2F-140 Gripper integrated directly onto the `tool0` flange.
- **IK Solver:** `KDLKinematicsPlugin` running within MoveIt's planning group.
- **Control Interface:** `JointTrajectoryController` passing interpolated waypoints directly to Gazebo hardware interfaces.

---

## 📸 Simulation Screenshots
All visual proof, Gazebo snapshots, and RViz motion plans for this stack are archived in the main repository media folder:

- **Gazebo Workspace Environment:** `../../media/ros1_gazebo_workspace.png`
- **RViz Motion Planning & Trajectories:** `../../media/ros1_pick_place_rviz.png`

---

## 🚀 Execution & Command Reference

### 1. Launch the Simulation Environment (Gazebo + RViz)
```bash
roslaunch ur_gazebo ur10e_bringup.launch
roslaunch ur10e_moveit_config ur10e_moveit_planning_execution.launch sim:=true
roslaunch ur10e_moveit_config moveit_rviz.launch
