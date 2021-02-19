import logging

def startlogger(loglevel = logging.ERROR):
  logger = logging.getLogger('discord')
  logger.setLevel(loglevel)
  handler = logging.FileHandler(filename='logger/discord.log', encoding='utf-8', mode='w')
  handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
  logger.addHandler(handler)
