import time

from bot import *


bot=WppBot()

bot.conect()
time.sleep(10)
bot.FindContact("Tiago Sanches")
