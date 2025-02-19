import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('chauffage_subscriber')
        self.subscription = self.create_subscription(
            String,
            'temperature',
            self.listener_callback,
            10)
        self.subscription

    def listener_callback(self, msg):
        
        
        
        try:
            temperature = float(msg.data.split(':')[1].strip().split(' ')[0]) 
            
            if temperature < 23:
                self.get_logger().info('Chauffage activé')
            else :
                self.get_logger().info('pas de chauffage')
        except (ValueError, IndexError) as e:
            self.get_logger().error(f'Erreur lors de l\'analyse du message: {e}')


def main(args=None):
    rclpy.init(args=args)

    chauffage_subscriber = MinimalSubscriber()

    rclpy.spin(chauffage_subscriber)

    chauffage_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

