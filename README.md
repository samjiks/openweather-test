# Get Open Weather Data

Get the Forecasted data of a city

## Getting Started

These instructions will get you a copy of the project up and running on
your local machine for development and testing purposes.

## Prerequisites

Requires Python 3 and above. While developing I used python 3.4. 

## Installing

Step 1: Make the virtual environment with python3.4

virtualenv .venv

Step 2: Activate the virtual environment

pip install -r requirements.txt

## Running the program

Command: python manage.py -c London,UK -f

-f will get the filtered response
-i will give the whole response that comes from the api
-c is required field to search for a city

Output:

    ```[
        {
            "dt": 1502798400,
            "weather": [
                {
                    "main": "Rain",
                    "description": "light rain"
                }
            ],
            "temp": {
                "max": 23,
                "min": 12.79
            }
        },
        {
            "dt": 1502884800,
            "weather": [
                {
                    "main": "Rain",
                    "description": "light rain"
                }
            ],
            "temp": {
                "max": 21.69,
                "min": 10.33
            }
        },
        {
            "dt": 1502971200,
            "weather": [
                {
                    "main": "Rain",
                    "description": "heavy intensity rain"
                }
            ],
            "temp": {
                "max": 18.68,
                "min": 16.28
            }
        },
        {
            "dt": 1503057600,
            "weather": [
                {
                    "main": "Rain",
                    "description": "moderate rain"
                }
            ],
            "temp": {
                "max": 16.83,
                "min": 13.78
            }
        },
        {
            "dt": 1503144000,
            "weather": [
                {
                    "main": "Rain",
                    "description": "light rain"
                }
            ],
            "temp": {
                "max": 18.05,
                "min": 11.63
            }
        },
        {
            "dt": 1503230400,
            "weather": [
                {
                    "main": "Rain",
                    "description": "moderate rain"
                }
            ],
            "temp": {
                "max": 18.84,
                "min": 14.16
            }
        },
        {
            "dt": 1503316800,
            "weather": [
                {
                    "main": "Rain",
                    "description": "light rain"
                }
            ],
            "temp": {
                "max": 20.18,
                "min": 16.03
            }
        },
        {
            "dt": 1503403200,
            "weather": [
                {
                    "main": "Rain",
                    "description": "light rain"
                }
            ],
            "temp": {
                "max": 19.74,
                "min": 15.83
            }
        },
        {
            "dt": 1503489600,
            "weather": [
                {
                    "main": "Clear",
                    "description": "sky is clear"
                }
            ],
            "temp": {
                "max": 21.81,
                "min": 16.9
            }
        },
        {
            "dt": 1503576000,
            "weather": [
                {
                    "main": "Clear",
                    "description": "sky is clear"
                }
            ],
            "temp": {
                "max": 20.27,
                "min": 13.69
            }
        },
        {
            "dt": 1503662400,
            "weather": [
                {
                    "main": "Clear",
                    "description": "sky is clear"
                }
            ],
            "temp": {
                "max": 19.58,
                "min": 11.88
            }
        },
        {
            "dt": 1503748800,
            "weather": [
                {
                    "main": "Rain",
                    "description": "light rain"
                }
            ],
            "temp": {
                "max": 18.81,
                "min": 11.08
            }
        },
        {
            "dt": 1503835200,
            "weather": [
                {
                    "main": "Clear",
                    "description": "sky is clear"
                }
            ],
            "temp": {
                "max": 20.76,
                "min": 8.33
            }
        },
        {
            "dt": 1503921600,
            "weather": [
                {
                    "main": "Rain",
                    "description": "light rain"
                }
            ],
            "temp": {
                "max": 20.94,
                "min": 9.89
            }
        }
    ]```

## Help 

usage: manage.py [-h] -c CITY [-f] [-i]

optional arguments:
  -h, --help            show this help message and exit
  -c CITY, --city CITY  Get the forecast data of a city
  -f, --filter          Filter Response of forecast data
  -i, --full            Full Response of forecast data