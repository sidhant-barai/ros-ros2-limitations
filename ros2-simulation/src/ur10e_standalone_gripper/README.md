# ROS 2 Standalone Gripper & Cobot Stack

This subdirectory contains the ROS 2 (Humble/Foxy) pipeline developed to address end-effector integration without reliance on full MoveIt 2 motion planning packages.

## 💡 Engineering Highlights
- **Direct Flange Attachment:** Integrated a **Robotiq 2F-140** gripper to the UR10e `tool0` frame directly through modular Xacro macro files.
- **Lightweight Kinematic Validation:** Enables real-time TF publishing and joint state control inside RViz2 using `robot_state_publisher` and dynamic GUI sliders.
- **Decoupled Architecture:** Bypasses complex MoveIt 2 controller manager configurations for lightweight, rapid hardware validation.

---

## 📸 Simulation Screenshots
All visual outputs, URDF trees, and RViz displays for this section are archived in the root repository media folder:

- **ROS 2 Standalone Assembly:** `../media/ros2_standalone_gripper.png`

---

## 🚀 Execution & Command Reference

To launch the ROS 2 standalone description and inspect TF trees:

```bash
# Source ROS 2 workspace
source colcon_ws/install/setup.bash

# Launch UR10e + Robotiq standalone visualization
ros2 launch ur10e_standalone_gripper standalone_gripper.launch.py
