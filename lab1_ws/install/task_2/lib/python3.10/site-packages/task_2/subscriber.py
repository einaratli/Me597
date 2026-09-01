import rclpy
from rclpy.node import Node
from task_2_interfaces.msg import JointData


class Subscriber(Node):
    def __init__(self):
        super().__init__('joint_subscriber')
        self.subscription=self.create_subscription(JointData,"joint_topic",self.listener_callback,10)
        self.subscription
    def listener_callback(self,msg):
      self.get_logger().info(f'Received - center: (x={msg.center.x}, y={msg.center.y}, z={msg.center.z}), vel={msg.vel}')
def main(args=None):
    rclpy.init(args=args)
    joint_subscriber=Subscriber()
    rclpy.spin(joint_subscriber)#keeps note active

    joint_subscriber.destroy_node()
    rclpy.shutdown()
if __name__=='__main__':
    main()

