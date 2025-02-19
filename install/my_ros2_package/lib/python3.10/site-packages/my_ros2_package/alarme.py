import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import pygame

class TemperatureSubscriber(Node):

    def __init__(self):
        super().__init__('temperature_subscriber')
        self.subscription = self.create_subscription(
            String,
            'temperature',
            self.listener_callback,
            10)
        self.subscription
        pygame.mixer.init()

    def listener_callback(self, msg):
        self.get_logger().info('Température : "%s"°C' % msg.data)

        try:
            temperature = float(msg.data.split(':')[1].strip().split(' ')[0])
            if temperature > 30:
                self.get_logger().info('Température trop élevée ! Alarme activée.')
                self.play_alarm()

        except (ValueError, IndexError) as e:
            self.get_logger().error(f'Erreur lors de l\'analyse du message: {e}')

    def play_alarm(self):
        alarm_file = 'alarm.mp3'

        try:
            pygame.mixer.music.load(alarm_file)  
            pygame.mixer.music.play()
            self.get_logger().info('Joue l\'alarme...')
        except pygame.error as e:
            self.get_logger().error(f"Erreur lors de la lecture du fichier MP3: {e}")


def main(args=None):
    rclpy.init(args=args)
    temperature_subscriber = TemperatureSubscriber()
    rclpy.spin(temperature_subscriber)
    temperature_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

