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

responses = {'thanks, b0t' : 'You are welcome',
                                             'thanks, bot' : 'You are welcome',
                                             'thanks b0t'  : 'You are welcome',
                                             'thankyou b0t'  : 'You are welcome',
                                             'thanks-you, b0t'  : 'You are welcome',
                                             'b0t: thank you' : 'You are welcome',
                                             'b0t: thanks' : 'You are welcome',
                                             'b0t: thankyou' : 'You are welcome',
                                             'b0t: thank-you' : 'You are welcome'}
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
