import paho.mqtt.client as mqtt
import time
import random

BROKER = "localhost"
PORT = 1883
TOPIC = "smartroom/room1/temperature"

def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Terhubung ke broker {BROKER}:{PORT}\n" if reason_code == 0
          else f"Gagal terhubung: {reason_code}")

def on_publish(client, userdata, mid, reason_code, properties):
    print(f"   -> broker konfirmasi publish selesai (mid={mid})")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_publish = on_publish

client.connect(BROKER, PORT, 60)
client.loop_start()
time.sleep(1)   # beri waktu koneksi terbentuk

for qos in [0, 1, 2]:
    suhu = round(random.uniform(24.0, 32.0), 2)
    info = client.publish(TOPIC, suhu, qos=qos)
    print(f"[DIKIRIM] QoS {qos} -> {TOPIC} = {suhu} °C (mid={info.mid})")
    info.wait_for_publish()   # tunggu sampai handshake QoS selesai
    time.sleep(2)

print("\nSelesai mengirim QoS 0, 1, 2.")
client.loop_stop()
client.disconnect()