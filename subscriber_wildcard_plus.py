import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC = "smartroom/+/temperature"   # + = satu level bebas (ruangan mana pun)

def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print(f"Terhubung ke broker {BROKER}:{PORT}")
        client.subscribe(TOPIC)
        print(f"Subscribe ke: {TOPIC}")
        print("(menangkap temperature dari SEMUA ruangan)\n")

def on_message(client, userdata, msg):
    print(f"[DITERIMA] {msg.topic} -> {msg.payload.decode()} °C")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, PORT, 60)
client.loop_forever()