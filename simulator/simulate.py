import paho.mqtt.client as mqtt
import time
import random

mqtt_broker = "sg_mosquitto"
mqtt_port = 1883

client = mqtt.Client()
client.connect(mqtt_broker, mqtt_port, 60)
client.loop_start()

button_states = ["pressed", "released"]

try:
    while True:
        button = random.choice(button_states)
        client.publish("controller/button", button)

        joystick = random.uniform(-100, 100)
        client.publish("controller/joystick", f"{joystick:.2f}")

        print(f"Published button: {button}, joystick: {joystick:.2f}")

        time.sleep(2)
except KeyboardInterrupt:
    pass
finally:
    client.loop_stop()
    client.disconnect()
