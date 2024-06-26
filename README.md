# Coverter QMAIL - Dovecot Mailbox to MBOX Apple format

Convert Dovecot Mail / QMail mail box to APPLE MBOX format so you can import and continue using it in your favorite program.

# Install

It is recommended to create a virtual environment

`virtualenv ./venv && . ./venv/bin/activate`

or 

`python -m venv venv` and for activate it just run `. ./venv/bin/activate`

after that install dependencies with this command `pip install -r requirements.txt`

# Usage

In current folder run `python md2mb.py [maildir_path] [mbox_filename]`

After completing the conversion process you can import it into your favorite program.

## Credits
> [!IMPORTANT]
>***This code has been modified, previously the previous authors are:***  
>* Frédéric Grosshans, 19 January 2012 (https://gist.github.com/lftbrts/249f034a439d3eb2e008f73506cacc2d)
>* Nathan R. Yergler, 6 June 2010