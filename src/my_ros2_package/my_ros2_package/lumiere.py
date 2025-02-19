import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random
import math

class LumierePublisher(Node):

    def __init__(self):
        super().__init__('lumiere_publisher')
        self.publisher_ = self.create_publisher(String, 'lumiere', 10)
        self.time_step = 0  
        self.total_steps = 100  
        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        lumiere = int((1 + math.sin(math.pi * 3 * (self.time_step / self.total_steps)))*20000)  
        self.time_step = (self.time_step + 1) % self.total_steps  
        msg = String()
        msg.data = f"Lumiere : {lumiere} lux"
        self.publisher_.publish(msg)
        self.get_logger().info(f"Publie : {msg.data}")

def main(args=None):
    rclpy.init(args=args)

    lumiere_publisher = LumierePublisher()

    rclpy.spin(lumiere_publisher)

    lumiere_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

