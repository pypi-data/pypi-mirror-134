from chogame import CHOgame
chogame = CHOgame()
@chogame.title
def title(ctx):
	print('This option came from main2.chogame.')
	return ctx.choice()
@title.option('Print file')
def o(ctx):
	print(__file__)
	input()
	return ctx.back()