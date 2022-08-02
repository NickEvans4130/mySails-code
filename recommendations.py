
# Importing libraries
import datapoint

# defining function
def checkweather(longitude,latitude,key,hourly_timestamps):

    # Create connection to DataPoint with your API key
    conn = datapoint.connection(api_key=key)

    # Get the nearest site for my latitude and longitude
    site = conn.get_nearest_forecast_site(latitude, longitude)

    # Get a forecast for my nearest site with 3 hourly timesteps
    forecast = conn.get_forecast_for_site(site.location_id, hourly_timestamps)

    # Get the current timestep from the forecast
    current_timestep = forecast.now()

    # Print out the site and current weather
    print(site.name + "-" + current_timestep.weather.text)


long_input = input("Please enter the longitude of the location | In the format ±xx.xxxx (decimals as apropriate)")
lat_input = input("Please enter the latitude of the location | In the format ±xx.xxxx (decimals as apropriate)")
key_input = "1234-5678-9101112"
hourly_time_input = input("Please enter hourly timestap | In the format xhourly")

checkweather(long_input,lat_input,key_input,hourly_time_input)