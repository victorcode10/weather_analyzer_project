# weather_analyzer.py
# Weather Data Analysis Functions
# Author: [Your Name]
# Date: [Today's Date]

def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit
    
    Args:
        celsius (float): Temperature in Celsius
    
    Returns:
        float: Temperature in Fahrenheit
    """
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius
    
    Args:
        fahrenheit (float): Temperature in Fahrenheit
    
    Returns:
        float: Temperature in Celsius
    """
    return (fahrenheit - 32) * 5/9


def analyze_temperature(temperatures):
    """
    Analyze temperature data
    
    Args:
        temperatures (list): List of temperatures
    
    Returns:
        dict: Dictionary with analysis results
    """
    if not temperatures:
        raise ValueError("Cannot analyze empty temperature list!")
    
    return {
        'max': max(temperatures),
        'min': min(temperatures),
        'average': sum(temperatures) / len(temperatures),
        'range': max(temperatures) - min(temperatures),
        'count': len(temperatures)
    }


def categorize_weather(temperature_c):
    """
    Categorize weather based on temperature (Celsius)
    
    Args:
        temperature_c (float): Temperature in Celsius
    
    Returns:
        str: Weather category
    """
    if temperature_c < 0:
        return "Freezing"
    elif temperature_c < 10:
        return "Cold"
    elif temperature_c < 20:
        return "Cool"
    elif temperature_c < 30:
        return "Warm"
    else:
        return "Hot"


def find_extreme_days(weather_data):
    """
    Find days with extreme temperatures
    
    Args:
        weather_data (dict): Dictionary with days as keys and temps as values
    
    Returns:
        dict: Dictionary with hottest and coldest days
    """
    if not weather_data:
        raise ValueError("No weather data provided!")
    
    hottest_day = max(weather_data.items(), key=lambda x: x[1])
    coldest_day = min(weather_data.items(), key=lambda x: x[1])
    
    return {
        'hottest': {'day': hottest_day[0], 'temp': hottest_day[1]},
        'coldest': {'day': coldest_day[0], 'temp': coldest_day[1]}
    }


def calculate_heat_index(temperature_f, humidity):
    """
    Calculate heat index (feels like temperature)
    Simplified formula for temperature >= 80°F
    
    Args:
        temperature_f (float): Temperature in Fahrenheit
        humidity (float): Relative humidity (0-100)
    
    Returns:
        float: Heat index in Fahrenheit
    """
    if temperature_f < 80:
        return temperature_f
    
    # Simplified Steadman formula
    heat_index = -42.379
    heat_index += 2.04901523 * temperature_f
    heat_index += 10.14333127 * humidity
    heat_index -= 0.22475541 * temperature_f * humidity
    heat_index -= 6.83783e-3 * temperature_f**2
    heat_index -= 5.481717e-2 * humidity**2
    heat_index += 1.22874e-3 * temperature_f**2 * humidity
    heat_index += 8.5282e-4 * temperature_f * humidity**2
    heat_index -= 1.99e-6 * temperature_f**2 * humidity**2
    
    return round(heat_index, 1)


def main():
    """
    Main function to test weather analysis functions
    """
    print("=" * 70)
    print("WEATHER DATA ANALYZER")
    print("=" * 70)
    
    # Sample weekly temperature data (Celsius)
    weekly_temps = {
        'Monday': 25,
        'Tuesday': 28,
        'Wednesday': 22,
        'Thursday': 30,
        'Friday': 27,
        'Saturday': 24,
        'Sunday': 26
    }
    
    print("\n🌡️  WEEKLY TEMPERATURE DATA (°C):")
    for day, temp in weekly_temps.items():
        temp_f = celsius_to_fahrenheit(temp)
        category = categorize_weather(temp)
        print(f"   {day:12s}: {temp:3d}°C ({temp_f:.1f}°F) - {category}")
    
    # Temperature analysis
    temps = list(weekly_temps.values())
    analysis = analyze_temperature(temps)
    
    print(f"\n📊 WEEKLY ANALYSIS:")
    print(f"   Maximum:  {analysis['max']}°C")
    print(f"   Minimum:  {analysis['min']}°C")
    print(f"   Average:  {analysis['average']:.1f}°C")
    print(f"   Range:    {analysis['range']}°C")
    
    # Find extreme days
    extremes = find_extreme_days(weekly_temps)
    print(f"\n🔥 EXTREME TEMPERATURES:")
    print(f"   Hottest:  {extremes['hottest']['day']} ({extremes['hottest']['temp']}°C)")
    print(f"   Coldest:  {extremes['coldest']['day']} ({extremes['coldest']['temp']}°C)")
    
    # Heat index calculation
    print(f"\n💧 HEAT INDEX EXAMPLE:")
    temp_f = 95
    humidity = 60
    heat_idx = calculate_heat_index(temp_f, humidity)
    print(f"   Temperature: {temp_f}°F")
    print(f"   Humidity: {humidity}%")
    print(f"   Feels like: {heat_idx}°F")
    
    # Temperature conversion examples
    print(f"\n🔄 TEMPERATURE CONVERSIONS:")
    print(f"   0°C = {celsius_to_fahrenheit(0):.1f}°F (Freezing)")
    print(f"   100°C = {celsius_to_fahrenheit(100):.1f}°F (Boiling)")
    print(f"   32°F = {fahrenheit_to_celsius(32):.1f}°C (Freezing)")
    print(f"   98.6°F = {fahrenheit_to_celsius(98.6):.1f}°C (Body temp)")
    
    print("\n" + "=" * 70)
    print("Weather analysis completed successfully!")
    print("=" * 70)


if __name__ == "__main__":
    main()
