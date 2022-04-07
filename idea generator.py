from ideas import ideas
from random import choice



print(len(ideas))

for i in range(10):
	idea = choice(ideas)
	print(idea['title'], '---------------', if bool(idea['link']): print(100))
	if not max:
		break
