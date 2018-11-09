import face_recognition
import paho.mqtt.client as paho

mqttClient = paho.Client("RPi")

host = "hung-laptop"
port = 3000

def on_connect(mosq, obj, rc):
   print("on_connect() "+str(rc))


def main():
   mqttClient.on_connect = on_connect
   print("Connecting to " + host)
   mqttClient.connect(host, port, 60)

   #get returned ID from face_recognition
   recognized_id = face_recognition.main()
   if recognized_id != "unknown":
    mqttClient.publish("toEsp/control/device/3", "on")
    print("Person regconized: " + recognized_id)

if __name__ == "__main__":
    main()


