from pushover import init, Client

import json
import pprint
import sys
import urllib2

userKey = "USER_KEY"
apiKey = "API_KEY"

def get_data(url):
    try:
        response = urllib2.urlopen(url)
    except urllib2.HTTPError:
        return None
    return json.loads(response.read())

def send_message(message):
    init(apiKey)
    Client(userKey).send_message(message, title="Weather Forecast")

def main():
    url = "http://metservice.com/publicData/localforecast"
    city = "Hamilton"
    if len(sys.argv) == 2:
        city = sys.argv[1]

    weather = get_data(url + city)
    if weather is None:
        send_message("HTTP error has occured with weather forecast")
        sys.exit()
        
    today = weather['days'][0]
    tomorrow = weather['days'][1]
    message = "The weather for {tomoro} the {date} is {forecast} with a high of {high}, today's overnight low is {low}".format(tomoro=tomorrow['dow'], date=tomorrow['date'], forecast=tomorrow['forecast'], high=tomorrow['max'], low=today['min'])
    send_message(message)

if __name__ == "__main__":
    main()
