#include <ESP8266WiFi.h>
#include <PubSubClient.h>

const char* ssid = "goodmorningpapi";         // Replace with your WiFi SSID
const char* password = "pakibros"; // Replace with your WiFi Password
const char* mqtt_server = "10.0.0.242"; // IP address of your MQTT broker

WiFiClient espClient;
PubSubClient client(espClient);

void setup_wifi() {
  delay(10);
  Serial.println("Connecting to WiFi...");
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("Connected to WiFi");
}

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message received on topic: ");
  Serial.print(topic);
  Serial.print(" Message: ");
  String message;
  for (int i = 0; i < length; i++) {
    message += (char)payload[i];
  }
  Serial.println(message);

  if (String(topic) == "control/sensor") {
    if (message == "ON") {
      // Code to activate sensor
      Serial.println("Sensor turned ON");
    } else if (message == "OFF") {
      // Code to deactivate sensor
      Serial.println("Sensor turned OFF");
    }
  }
}

void reconnect() {
  while (!client.connected()) {
    Serial.print("Connecting to MQTT...");
    if (client.connect("ESP8266Client")) {
      Serial.println("connected");
      client.subscribe("control/sensor");
    } else {
      Serial.print("Failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      delay(5000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  // Example of sending sensor data
  float sensorData = analogRead(A0); // Read analog sensor data
  String payload = String(sensorData);
  client.publish("sensor/data", payload.c_str());
  delay(1000);
}
