#include <ESP8266WiFi.h>
#include <PubSubClient.h>
 
const char* ssid = "YOUR_SSID";
const char* password =  "YOUR_PASS";
const char* mqttServer = "YOUR_RPI_IP";
const int mqttPort = 1883;
long lastReconnectAttempt = 0;
 
WiFiClient espClient;
PubSubClient client(espClient);
 
void setup() {

  pinMode(D2,OUTPUT);
  digitalWrite(D2,LOW);
  Serial.begin(115200);
 
  WiFi.begin(ssid, password);
  reconnect();
  
 
}
 
void callback(char* topic, byte* payload, unsigned int length) {
    Serial.println(topic);
    digitalWrite(D2,HIGH);
    delay(10000);
    digitalWrite(D2,LOW);
}

boolean reconnect() {
while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("Connecting to WiFi..");
  }
  Serial.println("Connected to the WiFi network");
 
  client.setServer(mqttServer, mqttPort);
  client.setCallback(callback);
 
  while (!client.connected()) {
    Serial.println("Connecting to MQTT...");
 
    if (client.connect("ESP8266Client")) {
 
      Serial.println("connected");  
 
    } else {
 
      Serial.print("failed with state ");
      Serial.print(client.state());
      delay(2000);
 
    }
  }
  client.publish("esp/test","Hello From ESP");
  client.subscribe("esp/lock");
  return client.connected();
}
 
void loop() {
   if (!client.connected()) {
    long now = millis();
    if (now - lastReconnectAttempt > 5000) {
      lastReconnectAttempt = now;
      // Attempt to reconnect
      if (reconnect()) {
        lastReconnectAttempt = 0;
      }
    }
  } else {
    // Client connected

    client.loop();
  }

}
