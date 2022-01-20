
import datetime
import json
import logging
from flask import jsonify
import requests


class PrincetonService:
    def __init__(self) -> None:
        pass

    def get_meal_info(self, food) -> str:
        """
        """

        # get meals 
        url = 'https://campus.dailyprincetonian.com/api/menus'
        response = requests.get(url).json()

        # get times
        today = datetime.date.today()
        todayYMD = today.strftime("%Y-%m-%d")
        tomorrow = today + datetime.timedelta(days = 1)
        tomorrowYMD = tomorrow.strftime("%Y-%m-%d")

        # parse output
        output = ''
        for entry in response:
            if entry['date'] != tomorrowYMD:
                continue
            print('match')
            for meal in entry:
                if meal == 'date':
                    continue

                for location in entry[meal]:

                    for entree in location['entrees']:

                        for item in entree['items']:

                            if food in item:
                                output = output + 'On ' + entry['date'] +', ' + location['name'] + '\'s ' + entree['header'] + ' for ' +  meal + ' is ' + item + '!\n'
        return output