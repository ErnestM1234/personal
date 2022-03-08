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
        headers = { 'Authorization': 'Bot OTMzMTI0MTgxNzQ5NTM0Nzcw.Yec9nQ.lm63YV4R_aoTFIYNZAx4Wb6KHmE'}

        # send request
        response = requests.post(url, headers=headers, json=data)

        print(response)

        return response

