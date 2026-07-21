# 3D Kinect Perception & Point Cloud Logging

This subdirectory handles the vision stack integration for the industrial manipulator workspace. It simulates a 3D Xbox Kinect depth sensor inside Gazebo to broadcast depth camera telemetry and process 3D spatial Point Cloud Data (`.pcd`).

---

## 🛠️ System Overview
- **Sensor Hardware:** Simulated Microsoft Kinect 3D Depth Camera.
- **Gazebo Plugin:** `libgazebo_ros_openni_kinect.so` producing `/kinect/depth/points` streams.
- **Data Capture:** Custom ROS logger node parsing `sensor_msgs/PointCloud2` array payloads for spatial workspace mapping and target location detection.

---

## 🚀 Execution & Command Reference

### 1. Launch Kinect Sensor in Gazebo
```bash
roslaunch kinect_perception kinect_gazebo.launch
