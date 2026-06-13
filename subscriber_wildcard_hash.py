import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC = "smartroom/room1/#"   # # = semua level di bawah room1

def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print(f"Terhubung ke broker {BROKER}:{PORT}")
        client.subscribe(TOPIC)
        print(f"Subscribe ke: {TOPIC}")
        print("(menangkap SEMUA sensor di room1)\n")

def on_message(client, userdata, msg):
    print(f"[DITERIMA] {msg.topic} -> {msg.payload.decode()}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, PORT, 60)
client.loop_forever()