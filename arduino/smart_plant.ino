const int sensorPin = A0;

void setup()
{
    Serial.begin(9600);
    Serial.println("Smart Plant Monitoring Started");
}

void loop()
{
    int sensorValue = analogRead(sensorPin);

    int moisture = map(sensorValue, 1023, 350, 0, 100);

    if (moisture > 100)
        moisture = 100;

    if (moisture < 0)
        moisture = 0;

    Serial.print("Moisture:");
    Serial.print(moisture);
    Serial.println("%");

    if (moisture < 30)
    {
        Serial.println("STATUS:VERY_DRY");
    }
    else if (moisture < 60)
    {
        Serial.println("STATUS:DRY");
    }
    else
    {
        Serial.println("STATUS:HEALTHY");
    }

    delay(1000);
}
