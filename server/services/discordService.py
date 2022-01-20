from flask import jsonify
import requests


class DiscordService:
    def __init__(self) -> None:
        pass

    def display_message(self, message) -> requests.Response:
        """
        prints the given discord message in the discord chat
        """
        # request info
        url = 'https://discord.com/api/channels/933126407620534292/messages'
        data = { 'content': message }
        headers = { 'Authorization': 'Bot OTMzMTYyMjMwMTc2OTcyODAy.YedhDA.IyV3xxXfcaU8zAgagaD5x_yU0Ho'}

        # send request
        response = requests.post(url, headers=headers, json=data)

        return response

