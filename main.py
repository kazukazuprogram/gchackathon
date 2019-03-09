#!/usr/bin/env python3
#coding: utf-8

from gevent import monkey
monkey.patch_all()

from bottle import route, run
from lib import PressKey,ReleaseKey,SendString
from os import system as sys

@route("/gamepad/play/<num>")
def play(num):
    print("play",num)

@route("/gamepad/dpad/<pad>")
def dpad(pad):
    print("dpad",pad)

@route("/gamepad/btn/<num>")
def btn(num):
    print("btn", {"1":"X","2":"O","9":"ST"}[num])

@route("/gamepad/position/<num>")
def position(num):
    global movestatus
    print("position",num)
    oldms = movestatus
    kdict = {"r":0x44,"l":0x41}
    num=int(num)-1
    if num == 0: # Right : 0x44
        print("R",end=" ")
        if movestatus == "":
            print("Press R")
            PressKey(0x44)
            movestatus = "r"
        elif movestatus == "l":
            print("Release L")
            ReleaseKey(0x41)
            movestatus=""
        elif movestatus == "r":
            print("Release R")
            ReleaseKey(0x44)
            movestatus=""
    else: # Left : 0x39
        print("L",end=" ")
        if movestatus == "":
            print("Press L")
            PressKey(0x41)
            movestatus = "l"
        elif movestatus == "l":
            print("Release L")
            ReleaseKey(0x41)
            movestatus=""
        elif movestatus == "r":
            print("Release L")
            ReleaseKey(0x44)
            movestatus=""
        else:
            print("ELSE")
    print(oldms,"=>",movestatus)

@route("/<user>/wrist/<num>")
def punch(user,num):
    print("{} Punch {}".format(user,num))
    num = int(num)
    if num==1: # パンチ
        k="t"
    elif num==2:
        k="y"
    elif num==3:
        k="u"
    SendString(k)

@route("/<user>/leg/<num>")
def kick(user,num):
    print("{} Kcik {}".format(user,num))
    num=int(num)
    if num==1:
        k="0x53"#"s"
    elif num==2:
        k="0x57"#"w"
    sys("start /B python jump.py "+k)
    return "OK"

if __name__ == '__main__':
    movestatus = ""
    print("Start Loop.")
    run(host='10.0.230.67', port=8080,debug=False)
