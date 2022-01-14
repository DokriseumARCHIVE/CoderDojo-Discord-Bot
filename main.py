import os

import discord
import os

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):

        if message.author.id == 916645891862048788:
            return
        else:
            print('Message from {0.author}: Hi'.format(message))
            channel = client.get_channel(916648708655951887) # .channel.id)
            await channel.send(f"Hallo\n")


project_dir = os.path.dirname(os.path.realpath(__file__))
print(f'project dir: {project_dir}')
with open(f"{project_dir}/config/key.txt", "r") as file:
    key = file.read().replace("\n", "")

client = MyClient()
client.run(key)
