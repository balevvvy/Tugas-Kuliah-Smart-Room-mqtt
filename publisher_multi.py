import paho.mqtt.client as mqtt
import time
import random

BROKER = "localhost"
PORT = 1883

def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Terhubung ke broker {BROKER}:{PORT}\n" if reason_code == 0
          else f"Gagal terhubung: {reason_code}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.connect(BROKER, PORT, 60)
client.loop_start()

try:
    while True:
        suhu1   = round(random.uniform(24.0, 32.0), 2)
        lembab1 = round(random.uniform(40.0, 80.0), 2)
        gerak1  = random.choice(["DETECTED", "NONE"])
        suhu2   = round(random.uniform(24.0, 32.0), 2)

        client.publish("smartroom/room1/temperature", suhu1)
        client.publish("smartroom/room1/humidity",     lembab1)
        client.publish("smartroom/room1/motion",       gerak1)
        client.publish("smartroom/room2/temperature",  suhu2)   # tidak di-subscribe

        print(f"[DIKIRIM] room1/temperature = {suhu1} °C")
        print(f"[DIKIRIM] room1/humidity    = {lembab1} %")
        print(f"[DIKIRIM] room1/motion      = {gerak1}")
        print(f"[DIKIRIM] room2/temperature = {suhu2} °C")
        print("-" * 40)
        time.sleep(3)
except KeyboardInterrupt:
    print("\nPublisher dihentikan.")
    client.loop_stop()
    client.disconnect()