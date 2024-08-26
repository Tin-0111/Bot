pip install discrod

import discord

Token = '<MTI3NzUwODEwMTM0MzU0MzM2Nw.Ga8AJK.FXkOxc7khezQCLG3D6VgPZTIrkzQOj1yZ58Aac>'
CHANNEL_ID = '<897313821398552588>'

class MyClient(discord.Client):
  async def on_ready(self):
    channel = 
self.get_channel(int(CHANNEL_ID))
        await channel.send('Hello World")

intents = discord.Intents.default()
intents.gessage_content = True
client = MyClient(intents=intents)
client.run(TOKEN)
