#!/usr/bin/ python-
# -*- coding: utf-8 -*-
import telepot
import sys
import os
import time
import pprint
import unicodedata
import string
import pywikibot

TOKEN = '[YOUR-TOKEN]'
bot = telepot.Bot(TOKEN)

def on_chat_message(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
	if content_type == 'text' and chat_id == [YOUR-ID]:
		site = pywikibot.Site()
		print "received"
		name = msg["from"]["first_name"]
		txt = msg['text']
		helab = str(unicodedata.normalize('NFKD', txt).encode('ascii','ignore'))
		helab2 = helab + "[SUFFIX]"
		page = pywikibot.Page(site,helab2) #or nothing, if you aren't using suffix
		page.text = u"""
    [REPETITIVE STUFF]
"""
		page.save(u"[EDIT SUMMARY]")
		print "Sent: %s"%helab2
		bot.sendMessage(chat_id, "Created")
bot.message_loop(on_chat_message)
while 1:
	time.sleep(5)
