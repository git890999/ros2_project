import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random  # Importer le module random

class TemperaturePublisher(Node):  # Nom de la classe mis à jour pour être plus explicite

    def __init__(self):
        super().__init__('temperature_publisher')
        self.publisher_ = self.create_publisher(String, 'temperature', 10)
        timer_period = 0.5  # secondes
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        temperature = random.uniform(15, 35)  # Générer une température aléatoire entre 15 et 35
        msg = String()
        msg.data = f'Température de la pièce: {temperature:.2f} °C'  # Formater le message
        self.publisher_.publish(msg)
        self.get_logger().info('Publication: "%s"' % msg.data)
        self.i += 1

def main(args=None):
    rclpy.init(args=args)

    temperature_publisher = TemperaturePublisher()  # Utiliser la bonne instance

    rclpy.spin(temperature_publisher)  # Passer la bonne instance ici

    # Détruire le nœud explicitement
    temperature_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

