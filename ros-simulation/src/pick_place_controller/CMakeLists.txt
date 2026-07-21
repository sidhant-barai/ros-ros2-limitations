cmake_minimum_required(VERSION 3.0.2)
project(pick_place_controller)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  moveit_ros_planning_interface
  tf2_geometry_msgs
)

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)

# Build C++ Executable
add_executable(ur10e_pick_place_cpp src/ur10e_pick_place.cpp)
target_link_libraries(ur10e_pick_place_cpp ${catkin_LIBRARIES})

# Install Python scripts & C++ node
catkin_install_python(PROGRAMS
  scripts/pick_place_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(TARGETS ur10e_pick_place_cpp
  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
