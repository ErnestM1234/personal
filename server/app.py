from decimal import ROUND_DOWN
from sqlite3 import Row
from server.services.generateServices import CustomService
from flask import Flask
#from APScheduler.schedulers.background import BackgroundScheduler


def create_app():
    # app
    app = Flask(__name__)

    # services
    service = CustomService()

    print(service.princeton_service.get_curr_meal())

    def getAndSendFoodInfo():
        meals = service.princeton_service.get_meals()

        for i in range(service.db.numUsers):
            row = service.db.getInfoGivenId(i)
            message = service.princeton_service.get_meal_info(meals, row[3])
            if message != '':
                service.discord_service.display_message('<@' + row[2] + '>\n' + message)
    

    # # scheduler
    # scheduler = BackgroundScheduler()
    # # breakfast
    # scheduler.add_job(getAndSendFoodInfo, trigger='cron', second='*/3')
    # scheduler.start()
    getAndSendFoodInfo()


    @app.route('/')
    def index():

        return 'running?'


    return app
