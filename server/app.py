from decimal import ROUND_DOWN
from server.services.generateServices import CustomService
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from .config import config
import sys



def create_app():
    # app
    app = Flask(__name__)

    # services
    service = CustomService()

    def getAndSendFoodInfo():
        for i in range(service.db.numUsers):
            row = service.db.getInfoGivenId(i)
            message = service.princeton_service.get_meal_info(row[3])
            if message != '':
                service.discord_service.display_message('<@' + row[2] + '>\n' + message)
    

    # scheduler
    scheduler = BackgroundScheduler()
    scheduler.add_job(getAndSendFoodInfo, trigger='cron', day='*')
    scheduler.start()


    @app.route('/')
    def index():

        return 'running?'


    return app
