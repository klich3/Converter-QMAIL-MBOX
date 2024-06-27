#!/usr/bin/env python 
"""
█▀ █▄█ █▀▀ █░█ █▀▀ █░█
▄█ ░█░ █▄▄ █▀█ ██▄ ▀▄▀

Author: <Anton Sychev> (anton at sychev dot xyz)
md2mb.py (c) 2024
Created:  2024-06-26 20:09:24 
Desc: 
    Original code: https://gist.github.com/lftbrts/249f034a439d3eb2e008f73506cacc2d
    
    Frédéric Grosshans, 19 January 2012
    Nathan R. Yergler, 6 June 2010

    This file does not contain sufficient creative expression to invoke
    assertion of copyright. No warranty is expressed or implied; use at
    your own risk.

Documentation;
    Uses Python's included mailbox library to convert mail archives from
    maildir [http://en.wikipedia.org/wiki/Maildir] to 
    mbox [http://en.wikipedia.org/wiki/Mbox] format, icluding subfolder.

    See http://docs.python.org/library/mailbox.html#mailbox.Mailbox for 
    full documentation on this library.

Sample: 
    To run, save as md2mb.py and run:

    $ python md2mb.py [maildir_path] [mbox_path_and_filename]

    [maildir_path] should be the the path to the actual maildir (containing new, 
    cur, tmp, and the subfolders, which are hidden directories with names like 
    .subfolde.subsubfolder.subsubsbfolder);

    [mbox_filename] will be newly created, as well as a [mbox_filename].sbd the 
    directory.
"""

import sys
import os
import mailbox
import email
from email import policy

firstInit = True

def mailFactory(fp):
    '''
    Internal function to adapt the mailbox.Maildir class to the email.message_from_binary_file function
    '''
    return email.message_from_binary_file(fp)

def maildir2mailbox(mailboxPath, mboxPathAndFilename):
    global firstInit

    # Remove lock file if an error occurs
    if firstInit == True:
        lockFilePath = os.path.join(mboxPathAndFilename+".lock")
        if os.path.exists(lockFilePath):
            os.remove(lockFilePath)
            os.remove(mboxPathAndFilename)
            print(f"Lock file has been removed now I will try again...")
            firstInit = False

    for essential_dir in ['new', 'cur', 'tmp']:
        if not os.path.exists(os.path.join(mailboxPath, essential_dir)):
            print(f"The essential directory '{essential_dir}' does not exist in '{mailboxPath}'. Skipping...")
            return  # O considera continuar con el siguiente directorio esencial

    
    maildir = mailbox.Maildir(
        dirname=mailboxPath, 
        factory=mailFactory
    )
    mbox = mailbox.mbox(mboxPathAndFilename)

    # lock the mbox
    # comment out mbox.lock() if u run this script on a local machine
    mbox.lock()

    # iterate over messages in the maildir and add to the mbox
    try:
        for msg in maildir:
            try:
                msg_as_string = msg.as_string(policy=policy.SMTPUTF8)
                mbox.add(msg_as_string)
            
            except UnicodeEncodeError:
                msg_as_bytes = msg.as_bytes(policy=policy.SMTPUTF8)
                mbox.add(msg_as_bytes)  
                print("UnicodeEncodeError: Message added as bytes. ")
                print(msg)
                print("------- skip email")
                continue
            
            except ValueError as e:
                print("ValueError: ", e)
                print("------- skip email")

                if "String input must be ASCII-only" in str(e):
                    msg_as_bytes = msg.as_bytes(policy=policy.SMTPUTF8)
                    mbox.add(msg_as_bytes)  # Corregido para añadir msg_as_bytes en lugar de msg_as_string
                else: 
                    print(f"Error message: {e}")
                    print("------- skip email")
                    continue
            
    except FileNotFoundError as e:
        print(f"Error message: {e}")
    finally:
        mbox.close()
        maildir.close()

#Creates the main mailbox
dirname = sys.argv[-2]
mboxname = sys.argv[-1]

print("Converting:" + dirname + ' to -> ' + mboxname)

mboxdirname = mboxname+'.sbd'
maildir2mailbox(dirname, mboxname)

if not os.path.exists(mboxdirname): os.makedirs(mboxdirname)

listofdirs = [dn for dn in next(os.walk(dirname))[1] if dn not in ['new', 'cur', 'tmp']]

for curfold in listofdirs:
    curlist = [mboxname]+curfold.split('.')
    curpath = os.path.join(*[dn+'.sbd' for dn in curlist if dn])
    
    if not os.path.exists(curpath): os.makedirs(curpath)
    
    print(' | ' + curfold + ' -> ' + curpath[:-4])
    maildir2mailbox(os.path.join(dirname, curfold), curpath[:-4])

print('Done')
print('Now you con import this MBOX file into OSX Mail App or other mail client.')