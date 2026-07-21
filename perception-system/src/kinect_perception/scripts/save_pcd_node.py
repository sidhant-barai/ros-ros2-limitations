#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2 as pc2

class PointCloudLogger:
    """
    Subscribes to Gazebo Kinect PointCloud2 topics and processes spatial data.
    """
    def __init__(self):
        rospy.init_node('kinect_pcd_logger', anonymous=True)
        
        # Subscribe to incoming point cloud stream from Gazebo
        self.sub = rospy.Subscriber('/kinect/depth/points', PointCloud2, self.cloud_callback)
        self.points_captured = False
        
        rospy.loginfo("Kinect PCD Logger Node initialized. Listening on /kinect/depth/points...")

    def cloud_callback(self, msg):
        if not self.points_captured:
            rospy.loginfo(f"Received PointCloud2 Frame! Width: {msg.width}, Height: {msg.height}")
            
            # Read 3D coordinates (X, Y, Z) from sensor stream
            point_list = list(pc2.read_points(msg, field_names=("x", "y", "z"), skip_nans=True))
            rospy.loginfo(f"Successfully processed {len(point_list)} valid 3D point cloud entries.")
            
            # Log sampling completed
            self.points_captured = True
            rospy.loginfo("Point Cloud frame logged successfully.")

if __name__ == '__main__':
    try:
        logger = PointCloudLogger()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
