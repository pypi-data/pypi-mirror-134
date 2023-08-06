from chogame import CHOgame
from techdemo2 import chogame as chogame2
chogame = CHOgame()
@chogame.title
def title(ctx):
	print('Hello, welcome to chogame tech demo')
	return ctx.choice()
@title.option('Choices', id='choices')
def choices(ctx):
	print('Pick one')
	return ctx.choice()
title.add_chogame_as_option(chogame2, 'Adding another chogame script')
@choices.option('Letters', id='choices.letters')
def choices_letters(ctx):
	return ctx.choice()
choices_letters.option(id='choices', key='A')
choices_letters.option(id='choices', key='B')
choices_letters.option(id='choices', key='C')

@choices.option('Numbers', id='choices.numbers')
def choices_numbers(ctx):
	return ctx.choice()
choices_numbers.option(id='choices')
choices_numbers.option(id='choices')
choices_numbers.option(id='choices')

@choices.option('Random', id='choices.random')
def choices_random(ctx):
	return ctx.choice()
choices_random.option(id='choices', key="#")
choices_random.option(id='choices', key='=')
choices_random.option(id='choices', key='\\')

@chogame.room('vip')
def vip(ctx):
	print('You enter the vip lounge.\nWhat do you do?')
	return ctx.choice()
@vip.option('Disco', id='vip.party')
def party(ctx):
	disco = list(range(30, 38))
	i = 0
	try:
		while True:
			print(f'\033[1;{disco[i]}mDisco')
			i+=1
			if i == len(disco):
				i = 0
	except KeyboardInterrupt:
		return ctx.back()
@vip.option('Go to the dressing room.', id='vip.dressing_room')
def dressing_room(ctx):
	clothing = []
	clothing.append(input('What top will you be wearing\n> '))
	clothing.append(input('What leggings\n> '))
	ans = input('Any hats [Y/N]\n> ')[0].lower()
	if ans=='y':
		clothing.append(input("What hat?\n> "))
	elif ans=='n':
		print('Ok.')
	else:
		print('...No hats then.')
	print("This is what you are wearing:")
	print(*clothing, sep='\n')
	input('Press enter to go back. ')
	return ctx.back()
@title.option('Rooms', id='rooms')
def rooms(ctx):
	e = '\n'
	room = input(f'''Enter a room id
Here is a list:
{e.join(list(chogame.rooms.keys()))}
> ''')
	if room=='':
		return ctx.back()
	return ctx.goto_room(room)
chogame()