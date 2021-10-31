#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>

#define SENSORPIN A0

//Wifi 
const char* ssid = "your ssid";
const char* password = "your wifi password";

//Domain name with URL path or IP address with path
const char *serverName = "http://your.ip.addr:8000/insertMoistureLevel/";

//Timer
unsigned long lastTime = 0;
unsigned long timerDelay = 600000;

//Moisture Sensor
const int air = 620;
const int water = 310;
int moistureValue = 0;
int moisturePct = 0;

void setup_wifi() {
  delay(10);
  // We start by connecting to a WiFi network
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  randomSeed(micros());

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
}

int read_sensor() {
  //read and map values
  moistureValue = analogRead(SENSORPIN);
  moisturePct = map(moistureValue, air, water, 0, 100);

  //check edge cases
  if(moisturePct >= 100) {
    moisturePct = 100;
  } 
  
  if(moisturePct <= 0) {
    moisturePct = 0;
  }

  return moisturePct;
}

void post_sensor() {
  unsigned long now = millis();
  if (now- lastTime >= timerDelay) {
    lastTime = millis();
    WiFiClient client;
    HTTPClient http;    //Declare object of class HTTPClient
  
    char postData[80];
    int meter = read_sensor();
  
    //Post Data
    snprintf (postData, 80, "{\"level\": %d}", meter);
    Serial.print("sending: ");
    Serial.println(postData); 
    http.begin(client, serverName);              //Specify request destination
    http.addHeader("Content-Type", "application/json");    //Specify content-type header
  
    int resHttpCode = http.POST(postData);   //Send the request
    String resData = http.getString();    //Get the response payload
  
    Serial.print("Response Status: ");
    Serial.println(resHttpCode);   //Print HTTP return code
    Serial.print("Response data: ");
    Serial.println(resData);    //Print request response payload
  
    http.end();  //Close connection
  }
}

void setup() {
  Serial.begin(115200);
  setup_wifi();
}

void loop() {
  post_sensor();
}
