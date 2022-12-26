import discord 
import random



def ramudusita(arg):
  client=arg
  @client.command()
  async def join( ctx, *members: discord.Member):
  
    players=[]
  
    members=list(members)
    members.append(ctx.author)
  
    assets=['rama','seeta','lakshma','hanuma']
    data=f""
    for member in members:
      data=data+f" {member.mention}"
      players.append({'name':member,'asset':""})
    await ctx.send(f"{data} have joined the game!")
    @client.command()
    async def start(ctx):
      players_copy=players.copy()
      if ctx.author not in members:
        return
      else:
        for asset in assets  :
          if len(players_copy)>0:
             player=random.choice(players_copy)
             player['asset']=asset
             players_copy.remove(player)
             if player['asset']=='rama':
               ram=player['name']
               await ctx.send(f"{player['name'].mention} is rama! find seeta!")
             if player['asset']=='seeta':
               seeta=player['name']
               print("seeta:",seeta)
               await seeta.send("You are sita")
        @client.command()
        async def sita(ctx,m: discord.Member):
          if ctx.author==ram:
            if m==seeta:
              await ctx.send("congrats")
             
        