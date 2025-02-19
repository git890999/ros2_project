import rclpy
from rclpy.node import Node
from example_interfaces.srv import Trigger


class KeyboardClient(Node):

    def __init__(self):
        super().__init__('Keyboard_client')
        self.client= self.create_client(Trigger, 'keyboard_service')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('en attente du service...')
        self.req = Trigger.Request()

    def send_request(self):
        future = self.client.call_async(self.req)
        rclpy.spin_until_future_complete(self, future)
        return future.result()


def main():
    rclpy.init()
    node = KeyboardClient()
    response = node.send_request()
    print(response.message)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
