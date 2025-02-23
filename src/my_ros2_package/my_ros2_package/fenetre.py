import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class FenetreSubscriber(Node):

    def __init__(self):
        super().__init__('fenetre_subscriber')
        self.subscription = self.create_subscription(
            String,
            'fire_alert', 
            self.listener_callback,
            10)
        self.co2_subscription = self.create_subscription(
            String,
            'co2_level',
            self.co2_listener_callback,
            10)
        self.subscription  
        self.co2_level = None

    def listener_callback(self, msg):
        self.get_logger().info('Alerte reçue : "%s"' % msg.data)

        if msg.data == "Incendie détecté!" and self.co2_level is not None:
            if self.co2_level > 1000:
                self.get_logger().info("Incendie détecté! Ouverture d'urgence des fenêtres.")
            else:
                self.get_logger().info("Air frais respire en 4k alors ")

    def co2_listener_callback(self, msg):
        try:
            co2_level = float(msg.data.split(':')[1].strip().split(' ')[0])
            self.co2_level = co2_level
        except (ValueError, IndexError) as e:
            self.get_logger().error(f'Erreur lors de l\'analyse du niveau de CO2: {e}')


def main(args=None):
    rclpy.init(args=args)

    fenetre_subscriber = FenetreSubscriber()

    rclpy.spin(fenetre_subscriber)

    fenetre_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

