import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe("/#")  # $SYS/#

def on_message(client, userdata, msg):
    print(msg.topic +" "+ str(msg.payload))

    if(msg.topic == "/MTN/LT1/UMUM/NH3IN/PRESS"):
        print("NH3 INPUT NIHH GESS")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("158.140.163.173", 1883, 60)

client.loop_forever()