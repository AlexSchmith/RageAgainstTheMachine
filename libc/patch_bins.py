import os
from pwn import *

if args.LD:
   LD = args.LD
else:
   LD = '/opt/ld-2.27.so'

if args.LIBC:
   LIBC = args.LIBC
else:
   LIBC = '/opt/libc.so.6'

if args.BIN_DIR:
   BIN_DIR = args.BIN_DIR
else:
   #BIN_DIR = '/home/solardebris/development/RageAgainstTheMachine/bins/'
   BIN_DIR="/bins/"

for bin in os.listdir(BIN_DIR):
    filename = "%s%s" %(BIN_DIR,bin)
    log.info("Patching %s" %filename)
    patch_cmd="pwninit --bin %s --ld %s --libc %s --no-template" %(filename,LD,LIBC)
    print(patch_cmd)
    os.system(patch_cmd)

    if args.REPLACE:
        log.info("Replacing %s with %s_patched" %(filename,filename))
        repl_cmd="mv %s_patched %s" %(filename,filename)
        os.system(repl_cmd)

