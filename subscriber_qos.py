import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC = "smartroom/room1/temperature"

def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print(f"Terhubung ke broker {BROKER}:{PORT}")
        client.subscribe(TOPIC, qos=2)   # minta QoS maksimal
        print(f"Subscribe ke {TOPIC} (QoS 2)\n")

def on_message(client, userdata, msg):
    # msg.qos = QoS efektif pesan yang diterima
    print(f"[DITERIMA] QoS {msg.qos} | {msg.topic} -> {msg.payload.decode()} °C")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, PORT, 60)
client.loop_forever()