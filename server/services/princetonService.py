
import datetime
from http.client import responses
import json
import logging
from flask import jsonify
import requests


import json

class Generic:
    @classmethod
    def from_dict(cls, dict):
        obj = cls()
        obj.__dict__.update(dict)
        return obj


class PrincetonService:
    def __init__(self) -> None:
        pass

    def get_curr_meal(self):
        hour = datetime.datetime.now().hour
        minute = datetime.datetime.now().minute
    

        if (hour > 17):
            return 'dinner'

        if (hour > 11 and minute > 30):
            return 'lunch'

        if (hour > 7):
            return 'breakfast'



    def get_meals(self):
        # get meals 
        url = 'https://campus.dailyprincetonian.com/api/menus'
        response = requests.get(url).json()
        return response

    # def get_chicken_info(self, response, food) -> str:
    #     # get times
    #     today = datetime.date.today()
    #     todayYMD = today.strftime("%Y-%m-%d")
    #     tomorrow = today + datetime.timedelta(days = 1)
    #     tomorrowYMD = tomorrow.strftime("%Y-%m-%d")
    #     curr_meal = self.get_curr_meal()


    #     # parse json
    #     x = json.loads(response, object_hook=Generic.from_dict)

    #     f




    #     return

    def get_meal_info(self, response, food) -> str:
        """
        """

        # get times
        today = datetime.date.today()
        todayYMD = today.strftime("%Y-%m-%d")
        tomorrow = today + datetime.timedelta(days = 1)
        tomorrowYMD = tomorrow.strftime("%Y-%m-%d")
        curr_meal = self.get_curr_meal()

        # parse output
        output = ''
        for entry in response:
            if entry['date'] != tomorrowYMD:
                continue
            for meal in entry:
                if meal == 'date' or meal != curr_meal:
                    continue

                for location in entry[meal]:

                    for entree in location['entrees']:

                        for item in entree['items']:

                            if food in item:
                                output = output + 'On ' + entry['date'] +', ' + location['name'] + '\'s ' + entree['header'] + ' for ' +  meal + ' is ' + item + '!\n'
        return output