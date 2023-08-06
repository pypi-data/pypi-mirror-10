mkterm - Spawn Terminals
========================

mkterm is a project to create a userscript on POSIX systems that allows the 
user to create multiple terminal emulators (for instance, 3 different xterms).

Install
-------

Clone the repo and run the following (may require sudo privileges)

  ~$ python setup.py install

Or you can install it from pip with (again, may need sudo)

  ~$ pip install mkterm

Usage
-----

You can run mkterm via normal shell environment once it's installed. Feed it a 
number and it'll spawn multiple instances of a terminal (defaults to xterm)

If you want to change the terminal emulator, look for a .mkterm file in your 
$HOME directory and change the terminal to your preferred emulator

  terminal=urxvt

You can use xterm, rxvt, rxvt-unicode, terminator, xfce4-terminal, anything.

Help
----

If you want to see additional features, help out, track bugs, feel free to do so.
Submit issues on Github, send me an email if you want to discuss the application.

