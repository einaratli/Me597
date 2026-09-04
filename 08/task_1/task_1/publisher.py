import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64 # since using 4hz we to use float
class Publisher(Node):
    def __init__(self):
        super().__init__('basic_publisher')
                        
        self.publisher=self.create_publisher(Float64,'my_first_topic',10)
        self.start_time = self.get_clock().now()# start timer when note is created
        time=0.25 #4hz
        self.timer=self.create_timer(time,self.timer_callback)
        
    def timer_callback(self):
        current_time = self.get_clock().now()# get current time
        elapsed = current_time - self.start_time#find elapsed time from start of node
        msg=Float64()#data is a float number
        elapsed_seconds = elapsed.nanoseconds / 1e9 # Convert elapsed time from nanoseconds to seconds (1 second = 1e9 nanoseconds)
        msg.data = elapsed_seconds
        self.publisher.publish(msg)
        self.get_logger().info(f'Time since node was activated: {msg.data:.3f}')
        
def main(args=None):
    rclpy.init(args=args)

    publisher = Publisher()

    rclpy.spin(publisher)# keeps node running
    publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()