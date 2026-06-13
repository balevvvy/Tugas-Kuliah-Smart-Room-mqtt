import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC = "smartroom/room1/temperature"

# paho-mqtt 2.x: callback punya parameter reason_code & properties
def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print(f"Terhubung ke broker {BROKER}:{PORT}")
        client.subscribe(TOPIC)
        print(f"Subscribe ke topik: {TOPIC}\n")
    else:
        print(f"Gagal terhubung, kode: {reason_code}")

def on_message(client, userdata, msg):
    print(f"[DITERIMA] {msg.topic} -> {msg.payload.decode()} °C")

# WAJIB di paho-mqtt 2.x: tentukan CallbackAPIVersion
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.loop_forever()   # blok di sini, terus dengarkan pesan