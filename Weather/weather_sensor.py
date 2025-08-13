def default_sensor_stub():
    """Default values of sensor"""
    return {
        'temperatureInC': 50,
        'precipitation': 70,
        'humidity': 26,
        'windSpeedKMPH': 52
    }

def high_precipitation_stub():
    """Sensor values under high precipitation"""
    return {
        'temperatureInC': 30,  # Upper 25 Celsius
        'precipitation': 70,   # High precipitation(>60)
        'humidity': 80,
        'windSpeedKMPH': 80    # Low wind speed(<50)
    }
    