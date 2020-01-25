#include <Servo.h>
#include <ESP8266WiFi.h>
#include <WiFiClientSecure.h>
#include <UniversalTelegramBot.h>

Servo p2dServo;

// Initialize Wifi connection to the router
char ssid[] = "your_ssid";     // your network SSID (name)
char password[] = "your_password"; // your network key

// Initialize Telegram BOT
#define BOTtoken "your_bot_token"  // your Bot Token (Get from Botfather)

const char* node_name = "Lamp";
const char* action1 = "Turn on";
const char* action2 = "Turn off";
const char* action3 = "";

WiFiClientSecure client;
UniversalTelegramBot bot(BOTtoken, client);

int Bot_mtbs = 1000; //mean time between scan messages
long Bot_lasttime;   //last time messages' scan has been done

void handleNewMessages(int numNewMessages) {
  Serial.println("handleNewMessages");
  Serial.println(String(numNewMessages));

  for (int i = 0; i < numNewMessages; i++) {
    String chat_id = String(bot.messages[i].chat_id);
    String text = bot.messages[i].text;

    String from_name = bot.messages[i].from_name;
    if (from_name == "") from_name = "Guest";

    if (text == action1) {
      p2dServo.write(120);
      delay(2000);
      p2dServo.write(90);
      bot.sendMessage(chat_id, String(action1) + ": done!", "");
    }

    if (text == action2) {
      p2dServo.write(60);
      delay(2000);
      p2dServo.write(90);
      bot.sendMessage(chat_id, String(action2) + ": done!", "");
    }

    if (text == "/start") {
      String welcome = "Welcome to P2D, " + from_name + "!\n";
      bot.sendMessage(chat_id, welcome, "Markdown");

      String keyboardJson = "[[\"" + String(action1) + "\", \"" + String(action2) + "\"]]";
      bot.sendMessageWithReplyKeyboard(chat_id, "Choose from the keyboard the action you want perform for your " + String(node_name) + "!", "", keyboardJson, true);
    }
  }
}

void setup() {
  p2dServo.attach(2);
  p2dServo.write(90);

  Serial.begin(115200);

  // Set WiFi to station mode and disconnect from an AP if it was Previously connected
  // WiFi.mode(WIFI_STA);
  // WiFi.disconnect();
  // delay(100);

  // attempt to connect to Wifi network:
  Serial.print("Connecting Wifi: ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  if (millis() > Bot_lasttime + Bot_mtbs)  {
    int numNewMessages = bot.getUpdates(bot.last_message_received + 1);

    while (numNewMessages) {
      Serial.println("got response");
      handleNewMessages(numNewMessages);
      numNewMessages = bot.getUpdates(bot.last_message_received + 1);
    }
    Bot_lasttime = millis();
  }
}
