def generate_weather_report(sensor_reader):
    """
    Parameter:
    sensor_reader is the function for reading sensor data

    Return:
        str: The string of weather
    """
    readings = sensor_reader()
    weather = "Sunny Day"

    if readings['temperatureInC'] > 25:
        if readings['precipitation'] >= 20 and readings['precipitation'] < 60:
            weather = "Partly Cloudy"
        elif readings['windSpeedKMPH'] > 50:
            weather = "Alert, Stormy with heavy rain"
    return weather
    