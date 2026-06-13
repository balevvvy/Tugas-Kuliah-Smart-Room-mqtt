import paho.mqtt.client as mqtt
import time
import random

BROKER = "localhost"
PORT = 1883
TOPIC = "smartroom/room1/temperature"

def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print(f"Terhubung ke broker {BROKER}:{PORT}\n")
    else:
        print(f"Gagal terhubung, kode: {reason_code}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect

client.connect(BROKER, PORT, 60)
client.loop_start()     # jalankan loop di background

try:
    while True:
        suhu = round(random.uniform(24.0, 32.0), 2)   # sensor disimulasikan
        client.publish(TOPIC, suhu)
        print(f"[DIKIRIM]  {TOPIC} -> {suhu} °C")
        time.sleep(2)
except KeyboardInterrupt:
    print("\nPublisher dihentikan.")
    client.loop_stop()
    client.disconnect()