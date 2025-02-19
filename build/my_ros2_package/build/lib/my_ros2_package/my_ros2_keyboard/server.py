import rclpy
from rclpy.node import Node
from example_interfaces.srv import Trigger


class KeyboardServer(Node):

    def __init__(self):
        super().__init__('keyboard_server')
        self.srv = self.create_service(Trigger, 'keyboard_service', self.handle_request)
        self.get_logger().info("Serveur pret")

    def handle_request(self,request,response):
        key = input("Appuie sur 'o' ou 'c' : ").strip().lower()
        if key == 'o':
            response.message = "Bravo, t'as 0/20 " 
        elif key == 'c':
            response.message = "T'es cosmique "
        else :
            response.message = "des problemes de vue ???????"
        response.success = True
        return response
            


def main():
    rclpy.init()
    node = KeyboardServer()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
