"""
Python script sends windows toast notifications
displaying pre-loaded motivational quotes. The duration
of the notification can be edited in the code.
"""
from win10toast import ToastNotifier
import os, os.path
from PIL import Image
import PIL
n = ToastNotifier()

quoteList = ("It is well to remind ourselves that anxiety signifies a conflict, and so long as a conflict is going on, a constructive solution is possible.", "Courage doesn't always roar. Sometimes courage is the quiet voice at the end of the day saying 'I will try again tomorrow.","Great things are not done by impulse, but by a series of small things brought together.","It's not about perfect. It's about effort.","Don't try to be perfect. Just try to be better than you were yesterday.","It never gets easier. You just get better.","The pain you feel today will be the strength you feel tomorrow.","If you are not willing to risk the usual, you will have to settle for the ordinary.","Your education will take you to places you never thought were possible.","Work hard now so that you can rest later.")

import random
import time

n.show_toast("Inspiration Quote", random.choice(quoteList), icon_path = "b4164365747b5d60259fcc6af93db6cf.ico", duration= 10)

