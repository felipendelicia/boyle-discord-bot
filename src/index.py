import numbers
import discord
from discord.enums import Status
from discord.ext import commands
import datetime
import os

from mpmath.functions.functions import arg
import chemistry_module
import math_module
import physics_module
import others_module

bot = commands.Bot(command_prefix="*", description="Un bot que te facilita las tareas", help_command=None)
current_path = os.path.dirname(os.path.abspath(__file__))

#Bot-commands

@bot.command()
async def molecular_mass(ctx, formule):
    await ctx.send(chemistry_module.molecularmass(formule))

@bot.command()
async def balance_equations(ctx, *args):

    reaction = ""
    for i in list(args):
        reaction += i

    if "+" in reaction.split("=")[0]:
        reactives = reaction.split("=")[0].split("+")
    else:
        one_reactive = [reaction.split("=")[0]]
        reactives = one_reactive

    if "+" in reaction.split("=")[1]:
        products = reaction.split("=")[1].split("+")
    else:
        one_product = [reaction.split("=")[1]]
        products = one_product

    await ctx.send(chemistry_module.balancereactions(reactives,products))

@bot.command()
async def quadratic_function(ctx, a, b=0, c=0):
        await ctx.send(math_module.quadratic_function(a,b,c))
        await ctx.send(file=discord.File(f'{current_path}\output.png'))
        os.remove(f'{current_path}\output.png')

@bot.command()
async def convert_units(ctx, *args):
    await ctx.send(others_module.convert_units(list(args)))

@bot.command()
async def concentration(ctx, *args): 
    entry = "".join(list(args)).replace(" ","") #"mst=20g,msc=100g"

    arguments = entry.split(",") #["msc=12g","mst=23kg"]
    cont = 0
    #delete spaces:
    for x in arguments:
        arguments[cont] = x.replace(" ","")
        cont = cont + 1

    print (arguments)
    arguments_dictionary = {}

    for i in arguments:
        splitting = i.split("=")
        arg = splitting[0]
        arguments_dictionary.update({arg:splitting[1]})

    dic_keys = []
    for i in arguments_dictionary.keys():
        dic_keys.append(i)

    print(dic_keys)
    print(arguments_dictionary)

    for i in dic_keys:
        if i == "substance": continue
        value = arguments_dictionary[i]
        mag = ""
        unit = ""

        for x in list(value):
            if x.isalpha():
                unit = unit + x
            else:
                mag = mag + x

        mag_unit_list = [mag, unit]
        arguments_dictionary[i] = mag_unit_list

    print(arguments_dictionary)

    call_to_the_function = chemistry_module.concentration(arguments_dictionary)

    for i in call_to_the_function:
        await ctx.send(i)

@bot.command()
async def trition(ctx, cpattern, vpattern, vsample, nOH, nH, baseacid):
    await ctx.send(chemistry_module.trition(cpattern,vpattern,vsample,nOH,nH,baseacid))

@bot.command()
async def help(ctx):
    await ctx.send("""Boyle: Un bot que te facilita las tareas:
    Está en desarrollo, si encontras un bug podes informarme en delicia4581@gmail.com
    Sistema de unidades: https://github.com/hgrecco/pint/blob/master/pint/default_en.txt
    Mi GitHub: https://github.com/1felipo""")
    await ctx.send(file=discord.File(current_path + "\chemistry_commands.txt"))
    await ctx.send(file=discord.File(current_path + "\math_commands.txt"))
    await ctx.send(file=discord.File(current_path + "\physics_commands.txt"))
    await ctx.send(file=discord.File(current_path + "\other_commands.txt"))

@bot.command()
async def ideal_gases(ctx, *args):
    #variable to modify the string:
    x = ""
    params_dic = {}
    out_unit = None
    #making a str from the list:
    for i in list(args):
        x += i

    #deleting the spaces:

    x = x.replace(" ", "")

    #separating the params:

    x = x.split(",")

    #indicating output unit and eliminating these element of the list...

    out_unit = x[len(x)-1][2:]
    x.pop()

    #params_dic:

    for i in x:
        num = ""
        unit = ""
        magnitude = None
        y = i.split("=")

        for t in y[1]:
            if t.isalpha(): unit += t
            else: num+=t

        magnitude = [num,unit]

        params_dic[y[0].lower()] = magnitude

    print(params_dic)
    print(out_unit)

    output = physics_module.ideal_gases(params_dic,out_unit)

    await ctx.send(output)

#Bot-events

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Patricio rey y sus redonditos de ricota"))
    print("The bot has started")

bot.run("ODIyNjE1NDYyNTMzMTM2NDA0.YFU2WQ.tTUq_-QTAAq1UfjD29ua2gmi9qc")