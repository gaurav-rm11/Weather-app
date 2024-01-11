import os
import requests

if __name__ == '__main__':
    api_key = '002154d2c12b4b958c4125424241001'
    city = input("Enter the city name: ")

    base_url = 'https://api.weatherapi.com/v1/current.json'
    params = {
        'key': api_key,
        'q': city
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()

        print(f"Weather in {city}:")
        print(f"Temperature: {weather_data['current']['temp_c']}°C")
        temp = weather_data['current']['temp_c']
        command = (f'powershell.exe -Command "Add-Type -AssemblyName System.Speech;'
                   f' $synthesizer = New-Object -TypeName System.Speech.Synthesis.SpeechSynthesizer;'
                   f' $synthesizer.Speak(\'The current temperature in {city} is {temp}\')"')
        os.system(command)

        print(f"Condition: {weather_data['current']['condition']['text']}")
        cond = weather_data['current']['condition']['text']
        command = (f'powershell.exe -Command "Add-Type -AssemblyName System.Speech; '
                   f'$synthesizer = New-Object -TypeName System.Speech.Synthesis.SpeechSynthesizer; '
                   f'$synthesizer.Speak(\'current weather condition is {cond}\')"')
        os.system(command)
    else:
        print(f"Failed to retrieve weather data. Status code: {response.status_code}")
