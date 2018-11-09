import face_recognition
import paho.mqtt.client as paho

mqttClient = paho.Client()

host = "hung-laptop"
port = 3000

def on_connect(mosq, obj, rc):
   print("on_connect() "+str(rc))

mqttClient.on_connect = on_connect

print("Connecting to " + host)
mqttClient.connect(host, port, 60)


def main():
    recognized = face_recognition.main()
    print(recognized)
    if recognized != "unknown":
       mqttClient.publish("toEsp/control/device/3", "on")
       print("Done!")

main()

