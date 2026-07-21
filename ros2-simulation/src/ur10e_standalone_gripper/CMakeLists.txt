cmake_minimum_required(VERSION 3.8)
project(ur10e_standalone_gripper)

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

find_package(ament_cmake REQUIRED)

# Install directories for ROS 2 launch files and URDF Xacros
install(DIRECTORY
  launch
  urdf
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
