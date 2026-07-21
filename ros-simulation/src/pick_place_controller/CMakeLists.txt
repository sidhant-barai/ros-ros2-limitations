cmake_minimum_required(VERSION 3.0.2)
project(pick_place_controller)

find_package(catkin REQUIRED COMPONENTS
  rospy
  moveit_commander
  geometry_msgs
  std_msgs
)

catkin_python_setup()

# Install Python executable scripts so rosrun can discover them
catkin_install_python(PROGRAMS
  scripts/pick_place_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
