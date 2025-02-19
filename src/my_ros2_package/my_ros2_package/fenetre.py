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
        self.subscription  

    def listener_callback(self, msg):
        self.get_logger().info('Alerte reçue : "%s"' % msg.data)

        if msg.data == "Incendie détecté!":
            self.get_logger().info("Les fenêtres s'ouvrent pour aérer !")

def main(args=None):
    rclpy.init(args=args)

    fenetre_subscriber = FenetreSubscriber()

    rclpy.spin(fenetre_subscriber)

    fenetre_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

