# ROS1 UR10e + Robotiq Manipulator Stack

This subdirectory contains the ROS1 (Noetic) implementation of the industrial pick-and-place workspace pipeline using the **UR10e Cobot** and a **Robotiq 2F-140 Parallel Gripper**.

The simulation environment runs inside **Gazebo** with motion planning, joint trajectory calculation, and collision avoidance handled entirely via the **MoveIt! Motion Planning Framework**.

---

## 🛠️ Kinematic & Control Architecture

* **Robot Arm:** Universal Robots UR10e (6-DOF)
* **End-Effector:** Robotiq 2F-140 Gripper integrated directly onto the `tool0` flange.
* **IK Solver:** `KDLKinematicsPlugin` running within MoveIt's planning group.
* **Control Interface:** `JointTrajectoryController` passing interpolated waypoints directly to Gazebo hardware interfaces.

---

## 📂 Subdirectory File Structure

* **`src/`**
  * `pick_place_node.cpp`: C++ node for MoveIt planning scene collision objects, attached body geometry, and grasp pose calculations.
* **`scripts/`** (or `sripts/`)
  * `pick_place_controller.py`: Python script handling high-level task sequencing, joint trajectory execution, and state callbacks.
* **`launch/`**
  * Custom launch files to load scene parameters, spawn controllers, and bring up the manipulation stack in Gazebo/RViz.
* **`CMakeLists.txt` & `package.xml`**
  * ROS Noetic build configurations, MoveIt/roscpp/rospy dependency declarations, and target executable installations.

---

## 🚀 Execution & Command Reference

### 1. Launch the Simulation Environment (Gazebo + RViz)

```bash
roslaunch ur_gazebo ur10e_bringup.launch
roslaunch ur10e_moveit_config ur10e_moveit_planning_execution.launch sim:=true
roslaunch ur10e_moveit_config moveit_rviz.launch
