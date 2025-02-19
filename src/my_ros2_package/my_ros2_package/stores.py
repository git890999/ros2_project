import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class StoresSubscriber(Node):

    def __init__(self):
        super().__init__('stores_subscriber')
        self.subscription = self.create_subscription(
            String,
            'lumiere',
            self.listener_callback,
            10)
        self.subscription
    def listener_callback(self, msg):
        self.get_logger().info('lumiere : "%s" lux ' % msg.data)
        
        try:
            lumiere = int(msg.data.split(':')[1].strip().split(' ')[0])

            if lumiere > 5000 and lumiere < 30000:
                self.get_logger().info('stores ouverts : debut de journee')
            elif lumiere >= 30000:
                self.get_logger().info('stores fermees : trop de soleil')
            else:
                self.get_logger().info('stores fermees : nuit')
        except (ValueError, IndexError) as e:
            self.get_logger().error(f'Erreur lors de l\'analyse du message: {e}')


def main(args=None):
    rclpy.init(args=args)

    stores_subscriber = StoresSubscriber()

    rclpy.spin(stores_subscriber)

    stores_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

