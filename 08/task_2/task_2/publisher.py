import rclpy
from rclpy.node import Node
from task_2_interfaces.msg import JointData
from geometry_msgs.msg import Point32
class Publisher(Node):
    def __init__(self):
        super().__init__('joint_publisher')
                        
        self.publisher=self.create_publisher(JointData,'joint_topic',10)#publisher sends JointData message to joint topic
        time=0.25 #4hz
        self.timer=self.create_timer(time,self.timer_callback)
        
    def timer_callback(self):
        
        
        msg=JointData()# holds x y and z for center
        point=Point32()
        point.x=1.0
        point.y=2.0
        point.z=3.0
        msg.center=point
        msg.vel=2.0
        self.publisher.publish(msg)
        self.get_logger().info(f'Point: x={msg.center.x}, y={msg.center.y}, z={msg.center.z}, vel={msg.vel}')
        
def main(args=None):
    rclpy.init(args=args)

    publisher = Publisher()

    rclpy.spin(publisher)# keeps node running
    publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
