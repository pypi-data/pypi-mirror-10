==========================
jinja2rst
==========================
--------------------------------------------------------------------------
A Simple Tool and Python-Module for Documenting Jinja2 Template-Files
--------------------------------------------------------------------------

:Author:    Hartmut Goebel <h.goebel@crazy-compilers.com>
:Copyright: 2015 by Hartmut Goebel
:Licence:   GNU General Public Licence v3 or later (GPLv3+)


This tool allows you writing documentation directly into jinja2
template-files as comments. These comments will then be converted to
text and the template-code goes into literal blocks.

This is some kind of `literate programming`, except that you do not
write code into your text, but text into your code. This difference
allows to use the template-file directly without any pre-processing.


Usage::

  jinja2rst [-h] infile outfile

  positional arguments:
    infile      jinja2-template-file to read (`-` for stdin)
    outfile     rst-file to write (`-` for stdout)

  optional arguments:
    -h, --help  show this help message and exit


How it works
----------------

This script takes all lines beginning with :literal:`#\ ` (and lines
consisting of only a ``#``) as text-lines. Everything else will be
treated as "code". The text-lines will get the :literal:`#\ ` removed
and the "code" will get spaces prepended.

Additionally at the start and at the end of a "code"-block, lines are
added as required by reStructuredText. Also at the begin of a
"code"-block, a ``::`` is added if required.


Examples
-------------

You can find example jinja2-input, rst-output and generated html in the
examples directory. You may also view the generated html online at
https://rawgit.com/htgoebel/jinja2rst/develop/examples/main.html.

..
 Local Variables:
 mode: rst
 ispell-local-dictionary: "american"
 End:
