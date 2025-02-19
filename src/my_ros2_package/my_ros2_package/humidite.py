import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random

class HumidityPublisher(Node):
    def __init__(self):
        super().__init__('humidity_publisher')
        self.publisher_ = self.create_publisher(String, 'humidity', 10)
        timer_period = 1.0
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        humidity = random.uniform(40, 80)
        msg = String()
        msg.data = f"Humidité : {humidity:.2f}%" 
        self.publisher_.publish(msg)
        self.get_logger().info(f"Publication : {msg.data}")
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    humidity_publisher = HumidityPublisher()
    rclpy.spin(humidity_publisher)
    humidity_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

