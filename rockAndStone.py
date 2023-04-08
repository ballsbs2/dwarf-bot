import discord
import random

from apiKey import apiKey
from dwarfLines import rockAndStone, wereRich

class dwarfBot(discord.Client):
    async def on_message(self, message):
        #don't respond to self
        if message.author == self.user:
            return        

        content = message.content.lower()
        if "rock" in content or "stone" in content:
            await self.rockAndStone(message)
        elif "gold" in content or "rich" in content:
            await self.wereRich(message)

    async def rockAndStone(self, message):
        #select random salute from list
        returnMessage = rockAndStone[random.randint(0, len(rockAndStone) - 1)]
        await message.channel.send(returnMessage)

    async def wereRich(self, message):
        #select random "we're rich" line from list
        await message.channel.send(wereRich[random.randint(0, len(wereRich) - 1)])

dwarf = dwarfBot()
dwarf.run(apiKey)