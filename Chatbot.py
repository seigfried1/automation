from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('Bot')
trainer = ListTrainer(bot)

path = 'Absolute path of the file where chatterbot corpus is stored'

# Comment this part after running training the bot.
# Uncomment it if new corpus is added.
for files in os.listdir(path):
	data = open(path + files, 'r').readlines()
	trainer.train(data)

while True:
	message = input('You: ')
	if message.strip() != 'Bye':
		reply = bot.get_response(message)
		print('Chatbot: ', reply)
	if message.strip() == 'Bye':
		print('Chatbot: Bye')
		break