import json, random, time
import paho.mqtt.client as mqtt
THE_BROKER = "localhost"
Sensor1x = "Controller/Sensorwaarde/Joystick/x"
Sensor1y = "Controller/Sensorwaarde/Joystick/y"
Sensor2x = "Controller/Sensorwaarde/Knop/x"
Sensor2y = "Controller/Sensorwaarde/Knop/y"

mqttc=mqtt.Client()
mqttc.connect(THE_BROKER,1883)

while True:
    waarde1 = {"Sensor1 x-waarde": random.randint(0, 180), "Sensor1 y-waarde": random.randint(0, 180)}
    waarde2 = {"Sensor2 x-waarde": random.randint(0, 180), "Sensor2 y-waarde": random.randint(0, 180)}
    the_msg_str = json.dumps(waarde1) + " " + json.dumps(waarde2)
    print(the_msg_str)
    mqttc.publish(Sensor1x, json.dumps(waarde1["Sensor1 x-waarde"]))
    mqttc.publish(Sensor1y, json.dumps(waarde1["Sensor1 y-waarde"]))
    mqttc.publish(Sensor2x, json.dumps(waarde2["Sensor2 x-waarde"]))
    mqttc.publish(Sensor2y, json.dumps(waarde2["Sensor2 y-waarde"]))
    time.sleep(5)