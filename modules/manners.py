#!/usr/bin/env python2
"""
manners.py - jenni politeness Module
Copyright 2015, EyeR
Licensed under the Eiffel Forum License 2.

More info:
 * jenni: https://github.com/myano/jenni/
 * Phenny: http://inamidst.com/phenny/
"""

import re

responses = {'Thanks, B0t' : 'You are welcome',
             'Thanks, bot' : 'You are welcome',
             'Thanks, b0t' : 'You are welcome',
             'Thanks bot'  : 'You are welcome',
             'Thanks B0t'  : 'You are welcome',
             'Thanks b0t'  : 'You are welcome',
             'Thankyou b0t'  : 'You are welcome',
             'Thankyou, b0t'  : 'You are welcome',
             'Thank-you b0t'  : 'You are welcome',
             'Thanks-you, b0t'  : 'You are welcome',
             'B0t: thank you' : 'You are welcome',
             'B0t: thanks' : 'You are welcome',
             'B0t: thankyou' : 'You are welcome',
             'B0t: thank-you' : 'You are welcome'}

def manners(jenni, input):
    question = re.sub('[?!]', '', input.groups()[0])
    message = responses[question.lower()]
    message = message.upper() if question.isupper() else message 
    jenni.reply(message)

manners.rule = r'(?i)(^({qs})[\?\!]*$)'.format(qs="|".join(responses.keys()))
manners.priority = 'low'
manners.example = 'thanks bot'
manners.thread = False

if __name__ == '__main__':
    print __doc__.strip()
