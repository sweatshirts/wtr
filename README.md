
# wtr - a water noticer

A small and practically useless junk code that reminds me (or you) to drink some water, cos most of us simply just forget.

## FAQ
* ***Why is the .exe over 7MB?***<br /> 
    * I've used [Auto-py-to-exe](https://github.com/brentvollebregt/auto-py-to-exe) to make an .exe file, which includes some of the python libraries, so the potential end user doesn't have to install python to run this.<br />
    * If you're skeptical, just download the source .py file and run it yourself<br />
* ***The clock in console is not correct!*** <br />
    * I've opted to use UTC time by default despite it not being my timezone either. To get correct (current) time in the console output, you need to replace the ``gmtime()`` with ``time.localtime()`` in the source .py file. Unfortunately, the .exe release is hardcoded with the universal time. 




