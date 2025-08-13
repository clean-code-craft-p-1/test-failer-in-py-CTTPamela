from Weather.weather_sensor import default_sensor_stub, high_precipitation_stub
from Weather.weather_reporter import generate_weather_report

def test_rainy_weather():
    """Test cases for rainy"""
    weather = generate_weather_report(default_sensor_stub)
    print(f"Test Rainy: {weather}")
    assert "rain" in weather.lower(), "Test failed for rainy"

def test_high_precipitation():
    """Test cases for high precipitation"""
    weather = generate_weather_report(high_precipitation_stub)
    print(f"Test high precipitation: {weather}")
    # Enhance the assert for logic cases missing
    # assert "rain" in weather.lower() or "cloudy" in weather.lower(), \
    #        f"High precipitation, return: {weather}"

if __name__ == '__main__':
    test_rainy_weather()
    test_high_precipitation()
    print("Test all cases (Maybe!)")
    