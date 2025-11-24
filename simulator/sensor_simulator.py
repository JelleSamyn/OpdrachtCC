import paho.mqtt.client as mqtt
<<<<<<< Updated upstream
import json, random, time, os
from datetime import datetime

MQTT_BROKER = os.getenv('MQTT_BROKER', 'mosquitto')
MQTT_PORT = int(os.getenv('MQTT_PORT', 1883))
PUBLISH_INTERVAL = int(os.getenv('PUBLISH_INTERVAL', 2))
TOPIC_JOYSTICK = 'sensor/controller/joystick'
TOPIC_BUTTONS = 'sensor/controller/buttons'

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

client = mqtt.Client("sensor_simulator")
client.on_connect = on_connect
client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_start()

while True:
    # Simulate Joystick
    x = round(random.uniform(-1, 1), 3)
    y = round(random.uniform(-1, 1), 3)
    magnitude = round((x**2 + y**2)**0.5, 3)
    joystick_payload = {'x': x, 'y': y, 'magnitude': magnitude, 'timestamp': datetime.now().isoformat()}
    client.publish(TOPIC_JOYSTICK, json.dumps(joystick_payload), qos=1)
    print(f"Published joystick: {joystick_payload}")

    # Simulate Buttons
    pressed_count = random.randint(0, 6)
    buttons_payload = {'pressed_count': pressed_count, 'timestamp': datetime.now().isoformat()}
    client.publish(TOPIC_BUTTONS, json.dumps(buttons_payload), qos=1)
    print(f"Published buttons: {buttons_payload}")

    time.sleep(PUBLISH_INTERVAL)
=======
import random, time
import json

MQTT_BROKER = "mosquitto"
MQTT_PORT = 1883
TOPIC_JOYSTICK = 'sensor/controller/joystick'  # 1 topic voor alles
TOPIC_BUTTONS = 'sensor/controller/buttons'

mqttc = mqtt.Client()
mqttc.connect(MQTT_BROKER, MQTT_PORT)

while True:
    # Simuleer joystick waarden
    x = random.randint(0, 255)
    y = random.randint(0, 255)
    magnitude = round((x**2 + y**2)**0.5, 3)
    pressed_count = random.randint(0, 6)

    # Bouw JSON payload
    joystick_payload = json.dumps({
        "x": x,
        "y": y,
        "magnitude": magnitude
    })

    # Publiceer joystick als één JSON op één topic
    mqttc.publish(TOPIC_JOYSTICK, joystick_payload)

    # Publiceer buttons apart
    mqttc.publish(TOPIC_BUTTONS, str(pressed_count))

    time.sleep(5)
>>>>>>> Stashed changes
