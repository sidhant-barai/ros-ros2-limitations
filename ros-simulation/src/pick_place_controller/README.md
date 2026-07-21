# ROS1 UR10e + Robotiq Manipulator Stack

This subdirectory contains the ROS1 (Noetic) implementation of the industrial pick-and-place workspace pipeline using the **UR10e Cobot** and a **Robotiq 2F-140 Parallel Gripper**. 

The simulation environment runs inside **Gazebo** with motion planning, joint trajectory calculation, and collision avoidance handled entirely via the **MoveIt! Motion Planning Framework**.

---

## 🛠️ Kinematic & Control Architecture
- **Robot Arm:** Universal Robots UR10e (6-DOF)
- **End-Effector:** Robotiq 2F-140 Gripper integrated directly onto the `tool0` mount.
- **IK Solver:** `KDLKinematicsPlugin` (numerical) running within MoveIt's interface.
- **Control Interface:** `JointTrajectoryController` passing planning paths directly to the simulated hardware controllers over Gazebo.

---

## 📸 Simulation Results

> **Placeholder Note:** Add your Gazebo or RViz execution screenshots in this section or link to the media folder.

| Simulation State | Description |
|---|---|
| `<Add Pick Image Link>` | **Step 1: Pick Phase** – UR10e reaches the target coordinates inside the Gazebo workspace using Cartestian Inverse Kinematics planning. |
| `<Add Place Image Link>` | **Step 2: Place Phase** – The gripper closes on the simulated object, lifts it, and transfers it to the deposition zone safely. |

---

## 🚀 Execution & Command Reference

To launch this environment and execute the Pick & Place task, open your terminal and follow these steps:

### 1. Launch the Simulation Environment (Gazebo + RViz)
```bash
roslaunch ur_gazebo ur10e_bringup.launch
roslaunch ur10e_moveit_config ur10e_moveit_planning_execution.launch sim:=true
roslaunch ur10e_moveit_config moveit_rviz.launch
