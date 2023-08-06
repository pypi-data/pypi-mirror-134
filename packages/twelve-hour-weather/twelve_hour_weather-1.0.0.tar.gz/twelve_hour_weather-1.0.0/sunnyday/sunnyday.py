import requests
import pprint

# url = "http://api.openweathermap.org/data/2.5/forecast?" \
#       "q=launceston,australia&units=metric&appid=617f784a85a288644b8b093dc5bd138b"
#
# res = requests.get(url=url)
# print(res.json())


class Weather(object):
    """
    Creates a Weather object getting an apikey as input
    and either a city name or lat and lon coordinates.

    Package use example:

    # Create a weather object using a city name:
    # The api key below is not guarenteed to work.
    # Get your own api key from https://openweathermap.org
    # And wait for a couple of hours for the api key to be activated

    # >>> weather1 = Weather(apikey=617f784a85a288644b8b093dc5bd13243, city="Launceston")

    # Using latitude and longitude coordinates
    # >>> weather2 = Weather(apikey=617f784a85a288644b8b093dc5bd13243, lat=40.5, lon=5.3)

    # Get complete weather data for the next 12 hours:
    # >>> weather.next_12h()

    # Simplified data for the next 12 hours:
    # >>> weather1.next_12h_simplified()

    """
    base_url = "http://api.openweathermap.org/data/2.5/forecast?"
    units = "metric"

    def __init__(self, api_key, city=None, lat=None, lon=None):
        if city:
            res = requests.get(url=f"{self.base_url}q={city}&units={self.units}&appid={api_key}")
            self.data = res.json()
        elif lat and lon:
            res = requests.get(url=f"{self.base_url}lat={lat}&lon={lon}&units={self.units}&appid={api_key}")
            self.data = res.json()
        else:
            raise TypeError("Provide either a city or lat and lon arguments")
        if self.data["cod"] != "200":
            raise ValueError(self.data["message"].title())

    def get_data(self):
        if self.data:
            return self.data
        return "No data to display"

    def next_12h(self):
        """
        Returns 3-hour data for the next 12 hours as a dict.
        """
        return self.get_data()["list"][:4]

    def next_12h_simplified(self):
        """
        Returns simplified 3-hour data for the next 12 hours as a list of tuples.
        """
        # pprint.pprint(self.get_data()["list"][0])
        data = []
        for d in self.get_data()["list"][:4]:
            data.append((d["dt_txt"], d["main"]["temp"],
                         d["weather"][0]["description"]))
        return data
