import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883

# subscribe ke beberapa topik tertentu (tanpa wildcard)
TOPICS = [
    ("smartroom/room1/temperature", 0),
    ("smartroom/room1/humidity",    0),
    ("smartroom/room1/motion",      0),
]

def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print(f"Terhubung ke broker {BROKER}:{PORT}")
        client.subscribe(TOPICS)        # subscribe banyak topik sekaligus
        for t, q in TOPICS:
            print(f"  Subscribe: {t}")
        print("  (room2/temperature sengaja TIDAK di-subscribe)\n")

def on_message(client, userdata, msg):
    print(f"[DITERIMA] {msg.topic} -> {msg.payload.decode()}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, PORT, 60)
client.loop_forever()