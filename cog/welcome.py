import discord
from discord.ext import commands

import datetime


class Welcome(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = member.guild

        # Guilds
        titogang = self.bot.get_guild(786392734377967676)
        neet = self.bot.get_guild(804077562087079936)

        # TitoGvng
        if guild == titogang:
            embed = discord.Embed(
                color=discord.Color.red(),
                timestamp=datetime.datetime.utcnow()
            )
            embed.add_field(
                name='Β‘Te doy la bienvenida!',
                value='Tenemos mucha suerte de encontrate aquΓ­,'
                      f'{member.mention}, '
                      'Β‘espero que te diviertas!'
            )
            embed.set_image(
                url='https://bestanimations.com/Nature/Water/'
                    'lake/lake-nature-animated-gif-7.gif'
            )
            embed.set_footer(text='Bienvenida de RoboTito')
            await self.bot.get_channel(786393328924098580).send(embed=embed)

        # NEET
        elif guild == neet:
            embed = discord.Embed(
                color=discord.Colour.from_rgb(202, 21, 180),
                timestamp=datetime.datetime.utcnow()
            )
            embed.add_field(
                name='Β‘π»π πππππ ππ πππππππππ@!',
                value=f'π©ππππππππ@ {member.mention} π '
                      f'{member.guild.name} πΉπππππππ ππππ '
                      'πππ ππππππ π πππ πππππ πππ πππππ '
                      'πππ πππππ ππ ππππ ππππππ'
            )
            embed.set_image(
                url='https://images-ext-2.discordapp.net/'
                    'external/Z-_ALisndUqmon'
                    'TIDdOi2MrkBNFgFsWU_'
                    'aZvGapnXgQ/https/p4.wallpaperbetter.com/'
                    'wallpaper/416/977/172/'
                    'anime-otaku-hd-wallpaper-preview.jpg'
            )
            embed.set_footer(text='Bienvenida de RoboTito')
            await self.bot.get_channel(815375493541003276).send(embed=embed)

        else:
            return


def setup(bot):
    bot.add_cog(Welcome(bot))
