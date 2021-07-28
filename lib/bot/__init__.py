from discord import Intents 
from apscheduler.schedulers.asyncio import  AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from discord.ext.commands import Bot as BotBase
from dotenv import load_dotenv
from discord import Embed
import os
from datetime import datetime
from discord.ext.commands import Bot as BotBase
from discord.ext.commands import CommandNotFound
import dotenv
# from six import create_bound_method
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
    
    async def on_error(self,err,*args,**kwargs):
        if err== "on_command_error":
            await args[0].send("ERRROOOR")

        channel = self.get_channel(848126501735890965)
        await channel.send("error occuired")
        raise

    async def on_command_error(self, context, exception):
        if isinstance(exception,CommandNotFound):
            pass
        elif hasattr(exception,"original"):
            raise exception.original
        else:
            raise exception
        # return await super().on_command_error(context, exception)

    async def on_ready (self):
        if not self.ready:
            print("BOT READY")
            self.ready=True
            self.scheduler.add_job(self.print_msg,CronTrigger(day_of_week=0,hour=12,minute=0,second=0))
            self.scheduler.start()
            # self.guild=self.get_guild(839558990060191794)
            
            channel = self.get_channel(848126501735890965)
            await channel.send("Now online")

            # embed = Embed(title="Now Online",description="KiM3X is online to Have fun",color=0xFF0000,timestamp=datetime.utcnow())
            # fields= [("Name", "Value", "True"),
            #          ("Another Field", "Just another field is this", "True"),
            #          ("non-line","This is non inline fields","False")]

            # for name, value, inline in fields:
            #     embed.add_field(name=name, value=value,inline=inline)
            # embed.set_author(name="Ashish")
            # embed.set_footer(text="morancium")
            # embed.set_image(url="https://ggsc.s3.amazonaws.com/images/made/images/uploads/Jan_and_Maisie_200_266_int_c1-1x.jpg")
            # embed.set_thumbnail(url="https://images.unsplash.com/photo-1627366247844-b4b5df8854d8?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=334&q=80")

            # await channel.send(embed=embed)


        else:
            print("Bot RECONNECTED")


    async def on_message(self,messgae):
        pass

    async def print_msg(self):
        channel = self.get_channel(848126501735890965)
        await channel.send("Timed Notification")

KiM3X = Bot()
# KiM3X.run()