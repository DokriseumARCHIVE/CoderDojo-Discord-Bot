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
            minecraft_servers_all = ["hypixel.net", "gommeHD.net", "antiAC.net", "inTrouble.de"]
            for i in range(len(minecraft_servers_all)):
                minecraft_servers_all[i]="https://"+ minecraft_servers_all[i]

            print('Message from {0.author}: {0.content}'.format(message))
            channel = client.get_channel(916648708655951887) # .channel.id)
            if message.content  == "!server" :
                await channel.send("\n".join(minecraft_servers_all))
            if message.content.startswith("!create"):
                channel_name = message.content.split()[1]
                channel = await message.guild.create_text_channel(channel_name)
            else:
                await channel.send(f"Hallo\n")


project_dir = os.path.dirname(os.path.realpath(__file__))
with open(f"{project_dir}/config/key.txt", "r") as file:
    key = file.read().replace("\n", "")

client = MyClient()
client.run(key)
