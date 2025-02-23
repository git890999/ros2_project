import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import pygame
import os
from flask import Flask, render_template, jsonify
from threading import Thread


temperature = None
humidity = None
co2_level = None
fire_alert = None
fenetre_state = None  
luminosite = None  
stores_state = None  
alarm_state = None  

app = Flask(__name__)

class WebInterfaceNode(Node):
    def __init__(self):
        super().__init__('web_interface_node')
        self.temperature_subscription = self.create_subscription(
            String,
            'temperature',
            self.temperature_callback,
            10
        )
        self.humidity_subscription = self.create_subscription(
            String,
            'humidity',
            self.humidity_callback,
            10
        )
        self.co2_subscription = self.create_subscription(
            String,
            'co2_level',
            self.co2_callback,
            10
        )
        self.fire_alert_subscription = self.create_subscription(
            String,
            'fire_alert',
            self.fire_alert_callback,
            10
        )
        self.lumiere_subscription = self.create_subscription(
            String,
            'lumiere',
            self.lumiere_callback,
            10
        )
        self.stores_subscription = self.create_subscription(
            String,
            'lumiere',  
            self.stores_callback,
            10
        )
        self.alarm_subscription = self.create_subscription(
            String,
            'temperature', 
            self.alarm_callback,
            10
        )

    def temperature_callback(self, msg):
        global temperature
        temperature = msg.data
        if temperature:
            try:
                temp_value = float(temperature.split(':')[1].strip().split(' ')[0])
                if temp_value > 30:
                    self.get_logger().info('Température trop élevée ! Alarme activée.')
                    global alarm_state
                    alarm_state = "Alarme activée"
                else:
                    alarm_state = "Température normale"
            except (ValueError, IndexError) as e:
                self.get_logger().error(f'Erreur lors de l\'analyse du message de température: {e}')

    def humidity_callback(self, msg):
        global humidity
        humidity = msg.data
        
        if humidity:
            self.get_logger().info(f"Humidité : {humidity}")

    def co2_callback(self, msg):
        global co2_level, fire_alert, fenetre_state
        co2_level = msg.data
        
        if co2_level:
            try:
                co2_value = float(co2_level.split(':')[1].strip().split(' ')[0])
                if co2_value > 1000:
                    fire_alert = "Incendie détecté!"
                    fenetre_state = "Fenêtres ouvertes (urgence)"
                else:
                    fire_alert = "Niveau de CO2 normal"
                    fenetre_state = "Fenêtres fermées"
            except (ValueError, IndexError) as e:
                self.get_logger().error(f'Erreur lors de l\'analyse du niveau de CO2: {e}')

    def fire_alert_callback(self, msg):
        global fire_alert, fenetre_state
        fire_alert = msg.data
        if fire_alert == "Incendie détecté!" and co2_level is not None:
            co2_value = float(co2_level.split(':')[1].strip().split(' ')[0])
            if co2_value > 1000:
                fenetre_state = "Fenêtres ouvertes (urgence)"
            else:
                fenetre_state = "Fenêtres fermées"
        else:
            fenetre_state = "Fenêtres fermées"

    def lumiere_callback(self, msg):
        global luminosite
        luminosite = msg.data
        if luminosite:
            self.get_logger().info(f"Luminosité : {luminosite}")

    def stores_callback(self, msg):
        global stores_state

        try:
            lumiere = int(msg.data.split(':')[1].strip().split(' ')[0])
            if lumiere > 5000 and lumiere < 30000:
                stores_state = "Stores ouverts : début de journée"
            elif lumiere >= 30000:
                stores_state = "Stores fermés : trop de soleil"
            else:
                stores_state = "Stores fermés : nuit"
        except (ValueError, IndexError) as e:
            self.get_logger().error(f'Erreur lors de l\'analyse du message de luminosité: {e}')

    def alarm_callback(self, msg):
        global alarm_state
        try:
            temperature = float(msg.data.split(':')[1].strip().split(' ')[0])
            if temperature > 30:
                alarm_state = "Alarme activée"
            else:
                alarm_state = "Température normale"
        except (ValueError, IndexError) as e:
            self.get_logger().error(f'Erreur lors de l\'analyse de l\'état de l\'alarme: {e}')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data')
def data():
    global temperature, humidity, co2_level, fire_alert, fenetre_state, luminosite, stores_state, alarm_state

    return jsonify({
        'temperature': temperature,
        'humidity': humidity,
        'co2_level': co2_level,
        'fire_alert': fire_alert,
        'fenetre_state': fenetre_state,
        'luminosite': luminosite,
        'stores_state': stores_state,
        'alarm_state': alarm_state 
    })


def run_web_server():
    app.run(host='0.0.0.0', port=5000)

def main(args=None):
    rclpy.init(args=args)

    web_interface_node = WebInterfaceNode()


    web_thread = Thread(target=run_web_server)
    web_thread.daemon = True
    web_thread.start()


    rclpy.spin(web_interface_node)

    web_interface_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

