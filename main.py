import requests
import json
import time

def get_weather_alerts(latitude, longitude):
  """
  Gets weather alerts for a given latitude and longitude.

  Args:
      latitude: The latitude of the location.
      longitude: The longitude of the location.

  Returns:
      A list of weather alert dictionaries.
  """

  url = f"https://api.weather.gov/alerts/active?point={latitude},{longitude}"
  response = requests.get(url)
  response.raise_for_status()  # Raise an exception for non-200 status codes

  data = json.loads(response.text)
  return data["features"]

if __name__ == "__main__":
  # Replace with your latitude and longitude
  latitude = LATITUDE
  longitude = LONGITUDE

  chatId = TELEGRAMCHATID
  botToken = BOTTOKEN


  # Get the initial list of alerts
  initial_alerts = get_weather_alerts(latitude, longitude)

  requests.get(f"https://api.telegram.org/bot{botToken}/sendMessage?chat_id={chatId}&text=Bot Is Ready!")
  

  # Print the initial alerts
  if initial_alerts:
    print("Initial weather alerts:")
    for alert in initial_alerts:
      # Print relevant details from each alert dictionary
      print(f" - Event: {alert['properties']['event']}")
      print(f"   Description: {alert['properties']['description']}")
      print(f"   Urgency: {alert['properties']['urgency']}")
      print(f"   Severity: {alert['properties']['severity']}")
      print()
      requests.get(f"https://api.telegram.org/bot{botToken}/sendMessage?chat_id={chatId}&text=*{alert['properties']['event']}*\nUrgency: {alert['properties']['urgency']}\nSeverity: {alert['properties']['severity']} ```{alert['properties']['description']}\n```&parse_mode=MarkdownV2")

  # Set the previous alerts to the initial alerts
  previous_alerts = initial_alerts

  while True:
    # Get the current list of alerts
    current_alerts = get_weather_alerts(latitude, longitude)

    # Check if there are new alerts
    if current_alerts != previous_alerts:
      print("New weather alerts:")
      for alert in current_alerts:
        # Print relevant details from each alert dictionary
        print(f" - Event: {alert['properties']['event']}")
        print(f"   Description: {alert['properties']['description']}")
        print(f"   Urgency: {alert['properties']['urgency']}")
        print(f"   Severity: {alert['properties']['severity']}")
        print()
        requests.get(f"https://api.telegram.org/bot{botToken}/sendMessage?chat_id={chatId}&text=*{alert['properties']['event']}*\nUrgency: {alert['properties']['urgency']}\nSeverity: {alert['properties']['severity']} ```{alert['properties']['description']}\n```&parse_mode=MarkdownV2")

      # Update the previous alerts
      previous_alerts = current_alerts

    time.sleep(60)  # Check for updates every 1 minute
