import sys

def get_weather(city):
    # 模拟天气数据
    data = {
        "Beijing": "Sunny, 25°C",
        "Shanghai": "Rainy, 19°C",
        "Shenzhen": "Cloudy, 28°C"
    }
    return data.get(city, "Weather data not found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py [City]")
    else:
        city = sys.argv[1]
        print(f"Weather in {city}: {get_weather(city)}")
