<?xml version="1.0"?>
<launch>
  <!-- Launch empty Gazebo world -->
  <include file="$(find gazebo_ros)/launch/empty_world.launch">
    <arg name="paused" value="false"/>
    <arg name="use_sim_time" value="true"/>
    <arg name="gui" value="true"/>
  </include>

  <!-- Load Kinect Xacro/URDF into parameter server -->
  <param name="robot_description" 
         command="$(find xacro)/xacro '$(find kinect_perception)/urdf/kinect_sensor.urdf.xacro'" />

  <!-- Spawn Kinect sensor model into Gazebo -->
  <node name="spawn_kinect" 
        pkg="gazebo_ros" 
        type="spawn_model" 
        args="-urdf -param robot_description -model kinect_camera -x 0 -y 0 -z 1.0" 
        output="screen" />

  <!-- Publish robot state and transforms -->
  <node name="robot_state_publisher" 
        pkg="robot_state_publisher" 
        type="robot_state_publisher" />
</launch>
