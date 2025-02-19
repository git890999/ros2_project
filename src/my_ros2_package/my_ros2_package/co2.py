import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random

class CO2Publisher(Node):

    def __init__(self):
        super().__init__('co2_publisher')
        self.publisher_ = self.create_publisher(String, 'co2_level', 10)
        self.fire_alert_publisher = self.create_publisher(String, 'fire_alert', 10)  # 
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        co2_level = random.uniform(350, 1500) 
        msg = String()
        msg.data = f'Niveau de CO2 : {co2_level:.2f} ppm'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publication: "{msg.data}"')

        if co2_level > 1000:
            fire_alert_msg = String()
            fire_alert_msg.data = "Incendie détecté!"  # Alerte incendie
            self.fire_alert_publisher.publish(fire_alert_msg)
            self.get_logger().info("Alerte incendie envoyée!")

def main(args=None):
    rclpy.init(args=args)

    co2_publisher = CO2Publisher()

    rclpy.spin(co2_publisher)

    co2_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

