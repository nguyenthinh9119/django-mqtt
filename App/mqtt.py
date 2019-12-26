from paho.mqtt import client as mqtt
import time
from .views import get_data
import json
import ssl
import socket


message=False
def on_connect(client,userdata, flags, rc,msg):
    global message
    message = msg.payload.decode()
    data=json.loads(message)
    data = get_data(data)
    data= json.dumps(data)
    message=True
    print("connected",message)
    message=True

awshost = "a36j9zqtwkxh63-ats.iot.ap-southeast-1.amazonaws.com"
awsport = 8883

caPath = "./AmazonRootCA1.pem" # Root certificate authority, comes from AWS with a long, long name
certPath = "./2430284d92-certificate.pem.crt"
keyPath = "./2430284d92-private.pem.key"

def message(client,userdata,level,buf):
    print("buffer",buf)

def on_disconnect(client,userdata,rc):
    print("client disconnect ok")

client1 = mqtt.Client("control1")       #create client object
client1.message=message
client1.tls_set(caPath,
            certfile=certPath, 
            keyfile=keyPath, 
            cert_reqs=ssl.CERT_REQUIRED, 
            tls_version=ssl.PROTOCOL_TLSv1_2, 
            ciphers=None)
client1.on_connect=on_connect
# client1.on_disconnect=on_disconnect
client1.connect(awshost,awsport,keepalive=120)      #establish connection

while not message:
    time.sleep(1)
    print("waiting",message)
    client1.loop()

time.sleep(3)
print("publishing",message)
client1.publish("test","The first test for MQTT amazon server")
time.sleep(2)
client1.loop()
time.sleep(2)
client1.disconnect()









