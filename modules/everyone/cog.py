from nextcord.ext import commands

class Everyone(commands.Cog, name="everyone"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog... Ready! \t| preventing @everyone")

    @commands.Cog.listener()
    async def on_message(self, message):
        print("messsage", message)
        if message.mention_everyone:
            print("message.content:", message.content)
            channel = message.channel
            await message.delete(delay=None)
            # await channel.send(content='Send @ everyone messages in the announcements channel')
    
    @commands.command()
    async def everyone(self, ctx: commands.Context):
        await ctx.send("pong")
 
def setup(bot: commands.Bot):
    bot.add_cog(Everyone(bot))   
    
# You will block people from sending the @ everyone ping outside the #announcments channel;
# and private message the user that they can not send the @ everyone ping in blank channel []
# Extra credit to also temporally stop the @ everyone message in #annoucnemnts
# and force the user to acknowledge they are @'ing blank members in the discord;
# OR either a running tally of how many times a user has been blocked from sending 
# it or an audit log channel telling people they have tried to @ everyone 
# in __ channel extra extra at a time