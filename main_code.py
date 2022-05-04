# ----> Начало импортов
import discord
from discord_components import Select, SelectOption, ComponentsBot
from discord.ext import commands
import logging
from all_models import Coin_flip, Rock_paper_sizors, Roll_dice
import requests
# ----> Конец импортов

# ----> Начало логгирования
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
# ----> Конец логгрирования

# ----> Подготовка к началу работы
intents = discord.Intents.default()
intents.members = True

TOKEN = "OTY0NTEwNjA3MTcwNzQwMjI0.YllsgA.kzsvokUIdj4HApOQdm-B_M3lzAU"

games = []
list_of_games = {1: '"Подброс монетки 1 на 1"',
                 2: '"Камень, ножницы, бумага"',
                 3: '"Подброс двух кубиков"'}
# ----> Конец подготовки


# ----> Начало "тела" бота
class Main(commands.Cog):
    globals()

    @commands.command(name='new')
    async def all_games(self, ctx):
        a = 'id: название'
        for i in list_of_games.keys():
            a = a + '\n' + str(i) + ': ' + list_of_games[i]
        await ctx.send('Выберите игру', components=[Select(placeholder='Выберите какую игру хотите', options=[
            SelectOption(label='Подброс монетки 1 на 1', value='Подброс монетки 1 на 1'),
            SelectOption(label='Камень, ножницы, бумага', value='Камень, ножницы, бумага'),
            SelectOption(label='Подброс двух кубиков', value='Подброс двух кубиков')
        ], custom_id='select1')])

        interaction = await bot.wait_for(
            "select_option", check=lambda inter: inter.custom_id == "select1")

        a = interaction.values[0]

        await interaction.send(content=f"{a} selected!")
        await ctx.channel.purge(limit=1)
        await ctx.send(self.new_game(ctx, a))

    def new_game(self, ctx, game_id):
        g = 0
        if game_id == 'Подброс монетки 1 на 1':
            games.append(Coin_flip([ctx.author]))
            g = 1
        elif game_id == 'Камень, ножницы, бумага':
            games.append(Rock_paper_sizors([ctx.author]))
            g = 2
        elif game_id == 'Подброс двух кубиков':
            games.append(Roll_dice([ctx.author]))
            g = 3
        return "{} начинает игру {}, id игры {}".format(ctx.author, list_of_games[g], len(games))

    @commands.command(name='join')
    async def join(self, ctx, id):

        a = games[int(id)-1].join_(ctx.author, ctx, id)
        await ctx.send(a)

        print(games[int(id)-1])

    @commands.command(name='del')
    async def delete(self, ctx, col):
        await ctx.channel.purge(limit=int(col))

    @commands.command(name='choice')
    async def test2(self, ctx, id):
        await ctx.send(
            "Selects!",
            components=[
                Select(
                    placeholder="Select something!",
                    options=[
                        SelectOption(label="Камень", value="rock"),
                        SelectOption(label="Ножницы", value="scissors"),
                        SelectOption(label='Бумага', value="paper")
                    ],
                    custom_id="select1",
                )
            ],
        )

        interaction = await bot.wait_for(
            "select_option", check=lambda inter: inter.custom_id == "select1"
        )
        values = interaction.values[0]
        user = interaction.user

        await interaction.send(content=f"{values} selected!")

        await ctx.channel.purge(limit=1)

        b = games[int(id)-1].choice(user, values)

        if b != -1:
            await ctx.send(b)
        else:
            await ctx.send('Ждём второго')

    @commands.command(name="cat")
    async def cat_giver(self, ctx):
        request = "https://api.thecatapi.com/v1/images/search"
        response = requests.get(request)
        ras = response.json()

        await ctx.send(ras[0]['url'])

    @commands.command(name="dog")
    async def dog_giver(self, ctx):
        request = "https://dog.ceo/api/breeds/image/random"
        response = requests.get(request)
        ras = response.json()

        await ctx.send(ras["message"])
# ----> Конец "тела" бота


# ----> Начало работы
bot = ComponentsBot(command_prefix='$$', intents=intents)
bot.add_cog(Main(bot))

bot.run(TOKEN)
# ----> Конец работы
