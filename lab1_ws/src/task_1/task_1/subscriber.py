import rclpy
from rclpy.node import Node

from std_msgs.msg import Float64

class Subscriber(Node):
    def __init__(self):
        super().__init__('basic_subscriber')
        self.subcription=self.create_subscription(Float64,"my_first_topic",self.listener_callback,10)
        self.subcription
    def listener_callback(self,msg):
        message_double=msg.data*2
        self.get_logger().info('Time elapsed: "%f", Double the time: "%f"' % (msg.data,message_double))
def main(args=None):
    rclpy.init(args=args)
    basic_subscriber=Subscriber()
    rclpy.spin(basic_subscriber)

    basic_subscriber.destroy_node()
    rclpy.shutdown()
if __name__=='__main__':
    main()

