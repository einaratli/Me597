import rclpy
from rclpy.node import Node
from task_2_interfaces.srv import JointState
import sys


class MinimalClient(Node):
    def __init__(self):
        super().__init__('minimal_client')
        self.cli = self.create_client(JointState, 'joint_service')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = JointState.Request()

    def send_request(self, x, y,z):
        self.req.x = x
        self.req.y = y
        self.req.z = z
        return self.cli.call_async(self.req)

def main(args=None):
    rclpy.init(args=args)

    minimal_client = MinimalClient()
    future = minimal_client.send_request(float(sys.argv[1]), float(sys.argv[2]),float(sys.argv[3]))
    rclpy.spin_until_future_complete(minimal_client, future)
    response = future.result()
    minimal_client.get_logger().info(
        'Result: x=%f, y=%f, z=%f -> valid=%s' %
        (float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), response.valid))
    minimal_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()