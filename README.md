# ROS vs. ROS 2 Comparative Analysis & Industrial Manipulator Stack

[![ROS 1](https://img.shields.io/badge/ROS-Noetic-blue.svg)](http://wiki.ros.org/noetic)
[![ROS 2](https://img.shields.io/badge/ROS2-Humble%2FFoxy-brightgreen.svg)](https://docs.ros.org/)
[![MoveIt](https://img.shields.io/badge/MoveIt-1%20%26%202-orange.svg)](https://moveit.ros.org/)
[![Gazebo](https://img.shields.io/badge/Gazebo-Simulation-blueviolet.svg)](https://gazebosim.org/)

## 📌 Executive Summary
This repository contains the complete implementation, configuration, and comparative evaluation framework for an **industrial robotic arm manipulation workspace**. Developed as part of a Master's thesis project, this repository compares **ROS 1 (Noetic)** and **ROS 2 (Humble/Foxy)** across trajectory planning execution, end-effector dynamic integration, and 3D perception point-cloud logging.

The target system features a **6-DOF Universal Robots UR10e Cobot**, an integrated **Robotiq 2F-140 Parallel Gripper**, and a simulated **3D Kinect Depth Camera**.

---

## 🏗️ Repository Architecture

```text
.
├── 01-ros1-simulation/        # ROS1 (Noetic) Pick & Place workspace + MoveIt! pipeline
│   └── src/pick_place_controller/
├── 02-ros2-simulation/        # ROS2 Standalone end-effector Xacro & launch architecture
│   └── src/ur10e_standalone_gripper/
├── 03-perception-system/      # 3D Kinect Gazebo plugin & PointCloud2 logging stack
│   └── src/kinect_perception/
└── media/                     # Simulation screenshots, trajectories, and PCD visualizations
