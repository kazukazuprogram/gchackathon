#!/usr/bin/env python3
#coding: utf-8

from sys import argv as a
from lib import *
from time import sleep

print(a)
PressKey(eval(a[1]))
sleep(0.5)
ReleaseKey(eval(a[1]))
# SendString(k, interval=0.5)
