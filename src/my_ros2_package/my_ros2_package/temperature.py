import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random 

class TemperaturePublisher(Node):  
    def __init__(self):
        super().__init__('temperature_publisher')
        self.publisher_ = self.create_publisher(String, 'temperature', 10)
        timer_period = 0.5 
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        temperature = random.uniform(15, 35) 
        msg = String()
        msg.data = f'Température de la pièce: {temperature:.2f} °C'  
        self.publisher_.publish(msg)
        self.get_logger().info('Publication: "%s"' % msg.data)
        self.i += 1

def main(args=None):
    rclpy.init(args=args)

    temperature_publisher = TemperaturePublisher()  
    rclpy.spin(temperature_publisher)  

    temperature_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

