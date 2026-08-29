import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
class Publisher(Node):
    def __init__(self):
        super().__init__('basic_publisher')
                        
        self.publisher=self.create_publisher(Float64,'my_first_topic',10)
        self.start_time = self.get_clock().now()
        time=0.25
        self.timer=self.create_timer(time,self.timer_callback)
        
    def timer_callback(self):
        current_time = self.get_clock().now()
        elapsed = current_time - self.start_time
        msg=Float64()
        elapsed_seconds = elapsed.nanoseconds / 1e9
        msg.data = elapsed_seconds
        self.publisher.publish(msg)
        self.get_logger().info(f'Time since activated: {msg.data:.2f}')
        
def main(args=None):
    rclpy.init(args=args)

    publisher = Publisher()

    rclpy.spin(publisher)
    publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()