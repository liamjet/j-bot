import discord
from discord.ext import commands

f = open('token.txt','r')
token = f.read()

bot = commands.Bot(command_prefix='jbot ')

emojis = ['<:jbotone:935711058457423882>','<:jbottwo:935711121812361246>','<:jbotthree:935711157380079657>','<:jbotfour:935711194491256832>','<:jbotfive:935711229912170566>','<:jbotsix:935711265731514459>','<:jbotseven:935711297801191474>','<:jboteight:935711328289562714>','<:jbotnine:935711357758763059>']

@bot.command(brief='Creates a poll with up to 9 options, place a space between each option.', description='To create a poll, type the following format: "jbot create option1 option2" where the options are the desired voting sections.')
async def create(ctx,*args):
    poll_options = list(args)
    #poll_options = [None] * (len(args)-1)
    #for x in args:
        #i = 0
        #poll_options[i] = str(i+1) + ': ' + args[i] 
    #poll_options = tuple(poll_options)
        
        
    message = await ctx.send('{} options: {}'.format(len(args), ', '.join(poll_options)))
    for x in range(len(args)):
        await message.add_reaction(emojis[x])
        
bot.run(token)


