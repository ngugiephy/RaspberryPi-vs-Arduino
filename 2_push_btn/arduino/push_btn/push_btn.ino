int btn = 8;
int led = 7;
int button_state = 0;

void setup() {
  pinMode(btn, INPUT);
  pinMode(led, OUTPUT);
//  digitalWrite(led, LOW);
}

void loop() {
  button_state = digitalRead(btn);

  if(button_state == HIGH){
    digitalWrite(led, HIGH);
  }else if(button_state == LOW){
    digitalWrite(led, LOW);
  }

}
