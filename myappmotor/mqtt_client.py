import paho.mqtt.client as mqtt

# Define the MQTT client
client = mqtt.Client()

# Define the broker address and port
BROKER_ADDRESS = "localhost"  # Change this if using a remote broker
PORT = 1883

# Define a callback function for message receipt
def on_message(client, userdata, message):
    print(f"Message received: {message.payload.decode()}")

# Setup the client
client.on_message = on_message

def connect_to_broker():
    client.connect(BROKER_ADDRESS, PORT, 60)
    client.loop_start()  # Start the loop to process received messages

def disconnect_from_broker():
    client.loop_stop()  # Stop the loop
    client.disconnect()
