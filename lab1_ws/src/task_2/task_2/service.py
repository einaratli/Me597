import rclpy
from rclpy.node import Node
from task_2_interfaces.srv import JointState

class MinimalService(Node):
    def __init__(self):
        super().__init__('minimal_service')
        self.srv = self.create_service(JointState, 'joint_service', self.callback)
    def callback(self,request,response):
        
        if request.x + request.y + request.z >= 0:
            response.valid = True
        else:
            response.valid = False
        self.get_logger().info('Incoming request\nx: %d y: %d z: %d, above zero: %s' % (request.x, request.y, request.z, response.valid))
        return response
def main():
    rclpy.init()

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()