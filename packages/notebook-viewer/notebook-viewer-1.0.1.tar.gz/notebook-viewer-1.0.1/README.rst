nbviewer - making the world a better place, with `gister <https://github.com/tr3buchet/gister>`__
-------------------------------------------------------------------------------------------------

examples
~~~~~~~~

::

    # post a secret gist on github and generate an nbviewer url:
    nbv

    # post a secret gist on github anonymously and generate an nbviewer url:
    nbv -a

    # edit a gist on github and generate an nbviewer url:
    nbv -e rfjw48jofwierfjipw
    nbv -e https://gist.github.com/tr3buchet/rfjw48jofwierfjipw

usage
~~~~~

::

    usage: nbv [-h] [-a] [-e id/url]

    generate ipynb links!

    optional arguments:
      -h, --help            show this help message and exit
      -a, --anonymous       gist will be anonymouseven if you have oauth
                            configured
      -e id/url, --edit id/url
                            edit a gist identified by id or url

usage - editing gists
~~~~~~~~~~~~~~~~~~~~~

editing gists works as such: \* any files gisted with the ``-e`` flag
will be added to the gist unless a file already exists in the gist by
that name, in which case it will be overwritten with the current file's
contents

usage - ipython notebooks
~~~~~~~~~~~~~~~~~~~~~~~~~

ipython notebooks are files with a ``.ipynb`` extension. if all files
specified on the commandline have this extension, a link to the
http://nbviewer.ipython.org url to display your gist will be generated
as well. nbviewer does not store your gist's data permanently, but does
cache it for ~10 minutes

install
~~~~~~~

``pip install notebook-viewer`` or clone the repo and
``python setup.py install``

`gister <https://github.com/tr3buchet/gister>`__ is required so you
might want to pop over and checkout the conguration, not to worry it
will work out of the box, but everything will be created anonymously

if you get an ``InsecurePlatformWarning``,
``pip install requests[security]`` to solve it. I had to install
libffi-devel on my fedora 21 system to get pyOpenSSL rocking

README.rst
~~~~~~~~~~

the ``README.rst`` document was generated from the ``README.md`` using
`pandoc <http://pandoc.org/>`__. it's quite tötes

::

    sudo dnf install pandoc
    pandoc README.md -s -o README.rst
