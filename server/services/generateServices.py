from server.services.dbService import db
from server.services.discordService import DiscordService
from server.services.princetonService import PrincetonService


class CustomService:
    def __init__(self):
        self.db = db()
        self.princeton_service = PrincetonService()
        self.discord_service = DiscordService()