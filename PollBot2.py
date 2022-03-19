import discord
from discord.ext import commands

from random import randrange

f = open('token.txt','r')
token = f.read()

bot = commands.Bot(command_prefix='jbot ')

emojis = ['<:jbotone:935711058457423882>','<:jbottwo:935711121812361246>','<:jbotthree:935711157380079657>','<:jbotfour:935711194491256832>','<:jbotfive:935711229912170566>','<:jbotsix:935711265731514459>','<:jbotseven:935711297801191474>','<:jboteight:935711328289562714>','<:jbotnine:935711357758763059>']

@bot.command(brief='Creates a poll with up to 9 options, place a space between each option.', description='To create a poll, type the following format: "jbot create option1 option2" where the options are the desired voting sections.')
async def poll(ctx,*args):      
    args_list = list(args)
    for x in range(len(args_list)):
        args_list[x] = '{}. {}'.format(x+1, args_list[x])
    args = tuple(args_list)
    message = await ctx.send('{} voting options:\n{}'.format(len(args), '\n'.join(args)))
    for y in range(len(args)):
        await message.add_reaction(emojis[y])

@bot.command(brief='Rolls a dice of your choosing.', description='To roll a dice, type the following format: "jbot roll #" where # is any number.')
async def roll(ctx,*args):
    results = []
    for x in args:
        x = int(x)
        results.append(randrange(x)+1)
        
        
    message = await ctx.send('You rolled: {}'.format(results))
bot.run(token)


