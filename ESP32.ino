#include <WiFi.h>
#include <PubSubClient.h>
#include <Adafruit_Sensor.h>
#include <DHT.h>

// WiFi and MQTT Broker settings
const char* ssid = "MyTTK_24G_149F";
const char* password = "******";
const char* mqtt_server = "raspberrypi.local";
const char* mqtt_username = "atc-festu";
const char* mqtt_password = "00000";
const char* clientID = "ESP32Client"; // MQTT client ID


// DHT settings
#define DHTPIN 4
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

// Relay settings
#define RELAY_PIN 5

WiFiClient espClient;
PubSubClient client(mqtt_server, 1883, espClient);

void setup_wifi() {
  delay(10);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }
}

void callback(char* topic, byte* message, unsigned int length) {
  String messageTemp;
  
  for (int i = 0; i < length; i++) {
    messageTemp += (char)message[i];
  }
  
  if (String(topic) == "esp32/relay") {
    if(messageTemp == "on"){
      digitalWrite(RELAY_PIN, HIGH);
      Serial.println("Relay turned ON");
    }
    else if(messageTemp == "off"){
      digitalWrite(RELAY_PIN, LOW);
      Serial.println("Relay turned OFF");
    }
  }
}

void reconnect() {
  while (!client.connected()) {
    if (client.connect(clientID, mqtt_username, mqtt_password)) {
      client.subscribe("esp32/relay");
    } else {
      delay(5000);
    }
  }
}

void setup() {
  // Initialize Serial
  Serial.begin(115200);

  pinMode(RELAY_PIN, OUTPUT);
  dht.begin();
  setup_wifi();

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  float h = dht.readHumidity();
  float t = dht.readTemperature();

  if (isnan(h) || isnan(t)) {
    return;
  }

  String temp = String(t);
  String hum = String(h);
  char tempBuf[50];
  char humBuf[50];
  temp.toCharArray(tempBuf, 50);
  hum.toCharArray(humBuf, 50);

  client.publish("esp32/temperature", tempBuf);
  client.publish("esp32/humidity", humBuf);
  
  // Print temperature with units
  Serial.println("----------------------------------");
  Serial.print("Temperature: ");
  Serial.print(t);
  Serial.println(" °C");

  // Print humidity with units
  Serial.print("Humidity: ");
  Serial.print(h);
  Serial.println(" %");

  // Print relay status
  if (digitalRead(RELAY_PIN) == HIGH) {
    Serial.println("Relay status: ON");
  } else {
    Serial.println("Relay status: OFF");
  }
  Serial.println("----------------------------------");
  delay(5000); // Publish temperature and humidity every 5 seconds
}
