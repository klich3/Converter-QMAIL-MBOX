# Coverter QMAIL - Dovecot Mailbox to MBOX Apple format

Convert Dovecot Mail / QMail mail box to APPLE MBOX format so you can import and continue using it in your favorite program.

# Install

Python version: ***3.12.3***

It is recommended to create a virtual environment

`virtualenv ./venv && . ./venv/bin/activate`

or 

`python -m venv venv` and for activate it just run `. ./venv/bin/activate`

after that install dependencies with this command `pip install -r requirements.txt`

# Usage

In current folder run `python md2mb.py [maildir_path] [mbox_path_and_filename]`

_Sample:_
`python md2mb.py /var/qmail/<domain_name>/<user>/Mailbox /home/domina_converted_file`

After completing the conversion process you can import it into your favorite program.

---

***Mail box / QMAIL folder structure***

```text
<Domain>
    |-<Username>
        |-@attachments
        |-Maildir
            |-.Spam
            |-...
            |-cur
            |-tmp
            |-new
            |-...
            
```

---

## Credits
> [!IMPORTANT]
>***This code has been modified, previously the previous authors are:***  
>* Frédéric Grosshans, 19 January 2012 (https://gist.github.com/lftbrts/249f034a439d3eb2e008f73506cacc2d)
>* Nathan R. Yergler, 6 June 2010

---

## Contribute

If you want to contribute you can always make a comment or make a pull-request, changes will be valued.


In case of an error you can also open an issue [HERE](https://github.com/klich3/Converter-QMAIL-MBOX/issues). 

---

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=klich3/Converter-QMAIL-MBOX&type=Date)](https://star-history.com/#klich3/Converter-QMAIL-MBOX&Date)