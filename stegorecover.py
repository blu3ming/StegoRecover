#!/usr/bin/python

import commands
import sys, os, signal
import time
from pwn import *

def def_handler(sig, frame):
	log.failure("Exiting...")
	sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

print("\n")
log.info("StegoRecover (by blu3ming)")
print(r"""
						 .       .
                        / `.   .' \
                .---.  <    > <    >  .---.
                |    \  \ - ~ ~ - /  /    |
                 ~-..-~             ~-..-~
             \~~~\.'                    `./~~~/
              \__/                        \__/
               /                  .-    .  \
        _._ _.-    .-~ ~-.       /       }   \/~~~/
    _.-'q  }~     /       }     {        ;    \__/
   {'__,  /      (       /      {       /      `. ,~~|   .     .
    `''''='~~-.__(      /_      |      /- _      `..-'   \\   //
                / \   =/  ~~--~~{    ./|    ~-.     `-..__\\_//_.-'
               {   \  +\         \  =\ (        ~ - . _ _ _..---~
               |  | {   }         \   \_\
              '---.o___,'       .o___,'       -r.millward-""")
print("\n")

if len(sys.argv) != 3:
	print("\n")
	log.info("Usage: python " + str(sys.argv[0]) + " steg_file wordlist")
	print("\n")
	log.failure("Exiting...")
	sys.exit(1)

else:
	line_count = sum(1 for line in open(sys.argv[2]))
	log.info("%d Passwords loaded" % line_count)
	time.sleep(2)

	p1 = log.progress("Recovering steg password...")
	p2 = log.progress("Password")
	time.sleep(2)
	with open(str(sys.argv[2])) as wordlist:
		for password in wordlist:
			p2.status("%s" % password)
			rc, out = commands.getstatusoutput("steghide extract -sf " + str(sys.argv[1]) + " -p " + str(password) + " >/dev/null 2>&1")
			if "wrote extracted" in out:
				p1.success("Password found!")
				p2.success("%s" % password)
				print("\n")
				log.info("%s" % out)
				wordlist.close()
				sys.exit(0)

	p1.failure("Password not found!")
	print("\n")
	log.info("Password not found in wordlist file... Exiting...")
	wordlist.close()
	sys.exit(1)
