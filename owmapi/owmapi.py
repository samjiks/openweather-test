import requests
import json
from copy import deepcopy

from collections import defaultdict
from abc import abstractmethod

BASE_URL = 'http://api.openweathermap.org/'


class OWMAPI(object):
    def __init__(self, base_url):
        self.base_url = base_url

    @abstractmethod
    def _get(self):
        raise NotImplementedError


class OWMForecastHTTPAPI(OWMAPI):
    def __init__(self, base_url=BASE_URL, city='London', unit='metric', country=14):
        super().__init__(base_url)
        self._api_key = None
        self._city = city
        self._unit = unit
        self._country = country
        self._set_response = None

    def _get(self):
        return getattr(requests, 'get')

    @property
    def api_key(self):
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        self._api_key = api_key

    def prepare_request(self):
        '''
        Response to Open Weather Forecast 16 day
        :return: Successful Request response
        '''
        try:
            if self._city and self._unit and self._country:
                self.url = ''.join([self.base_url, "data/2.5/forecast/daily?q={0}&units={1}&cnt={2}&APPID={3}".
                                   format(self._city, self._unit, self._country, self.api_key)])
            else:
                raise Exception('Need to set city, country, and units and api_keys')
        except TypeError as e:
            raise "Type Error %s" % e

    def create_response(self):
        try:
            response = self._get()(url=self.url)
        except ConnectionError as e:
            raise 'Connection Error %s' % e
        except AttributeError as e:
            raise 'Missing attribute url %s' % e

        else:
            if response.status_code == 200:
                self._set_response = response.text
            elif response.status_code == 401:
                raise Exception('Unauthorized, Invalid API Key')
            elif response.status_code == 400:
                raise Exception('Bad Request Created, Please check your request parameters')

    @property
    def _get_response(self):
        if hasattr(self, '_set_response'):
            return json.loads(self._set_response)

    def get_forecast_for_city(self, city):
        self._city = city
        self.prepare_request()
        self.create_response()
        return self._pretty_print(self._get_response)

    def _pretty_print(self, result):
        return json.dumps(result, indent=4)

    def filter_response(self):
        data = defaultdict(dict)
        result = []

        try:
            for key in self._get_response:
                if key == 'list':
                    for forecasted_dates in self._get_response[key]:
                        data = deepcopy(data)
                        if 'dt' in forecasted_dates:
                            data['dt'] = forecasted_dates['dt']
                        if 'weather' in forecasted_dates:
                            weathers = forecasted_dates['weather']
                            data['weather'] = [
                                                {
                                                 "main": weather['main'],
                                                 "description": weather['description']
                                                 }
                                                for weather in weathers
                                            ]
                        if 'temp' in forecasted_dates:
                            temp = forecasted_dates['temp']
                            data['temp']['max'] = temp['max'] if 'max' in temp else ''
                            data['temp']['min'] = temp['min'] if 'min' in temp else ''
                        result.append(data)
        except KeyError as e:
            print("Key Error %s", e)
        return self._pretty_print(result)

