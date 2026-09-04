import rclpy
from rclpy.node import Node
from task_2_interfaces.srv import JointState

class MinimalService(Node):
    def __init__(self):
        super().__init__('minimal_service')
        self.srv = self.create_service(JointState, 'joint_service', self.callback)# create service called joints service
    def callback(self,request,response):
        
        if request.x + request.y + request.z >= 0:#if sum of x y z is above zero then valid else not valid
            response.valid = True
        else:
            response.valid = False
        self.get_logger().info('Incoming request\nx: %d y: %d z: %d, above zero: %s' % (request.x, request.y, request.z, response.valid))
        return response# return response for client to recive
def main():
    rclpy.init()

    minimal_service = MinimalService()

    rclpy.spin(minimal_service)#keeps service alive

    rclpy.shutdown()


if __name__ == '__main__':
    main()
