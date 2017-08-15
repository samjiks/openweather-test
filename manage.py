from owmapi.owmapi import OWMForecastHTTPAPI
import argparse

if __name__ == "__main__":
    owmapi = OWMForecastHTTPAPI()
    owmapi.api_key = '0e83edfb1541cb66a71db49f12ac7e98'
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--city", help="Get the forecast data of a city", required=True)
    parser.add_argument("-f", "--filter", help="Filter Response of forecast data", action='store_true')
    parser.add_argument("-i", "--full", help="Full Response of forecast data", action='store_true')
    args = parser.parse_args()
    response = None

    if args.city:
        response = owmapi.get_forecast_for_city(args.city)

    if args.full:
        print(response)

    if args.filter:
        print(owmapi.filter_response())

