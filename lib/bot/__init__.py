from discord import Intents 
from apscheduler.schedulers.asyncio import  AsyncIOScheduler
from discord.ext.commands import Bot as BotBase
from dotenv import load_dotenv
from discord import Embed
import os
load_dotenv()

PREFIX ="%"
OWNER_IDS = [759826655400951808]

class Bot(BotBase):
    s=2
    d=43
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild=None
        # self.guild = None
        self.scheduler = AsyncIOScheduler()

        super().__init__(command_prefix=PREFIX,
        owner_ids=OWNER_IDS,
        intents=Intents.all(),
        )

    # def run(self):
    #     with open("./lib/bot/token","r",encoding="utf-8") as tf:
    #         self.TOKEN=tf.read()
    #     print(self.TOKEN)
    #     super().run(self.TOKEN,reconnect=True)


    def run(self):
        # self.VERSION=version
        self.TOKEN=os.getenv("dcToken")
        print("Running KiM3X...")
        super().run(self.TOKEN,reconnect=True)

    async def on_connet(self):
        print("HE::O")
    
    async def on_disconnet(self):
        print("Bot Disconnect")

    async def on_ready (self):
        if not self.ready:
            self.ready=True
            # self.guild=self.get_guild(839558990060191794)
            print("BOT READY")
            
            channel = self.get_channel(848126501735890965)
            await channel.send("Now online")

            embed = Embed(title="Now Online",description="KiM3X is online to Have fun")
            fields= [("Name", "Value", "True"),
                     ("Another Field", "Just another field is this", "True"),
                     ("non-line","This is non inline fields","False")]

            for name, value, inline in fields:
                embed.add_field(name=name, value=value,inline=inline)


            await channel.send(embed=embed)


        else:
            print("Bot RECONNECTED")


    async def on_message(self,messgae):
        pass

KiM3X = Bot()
# KiM3X.run()