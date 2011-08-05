nose-pynotify
=============
<img src="http://colinfdrake.com/images/nose.png" />

Implements a pynotify-based notification system for nose tests.

Installation
------------
To install nose-pynotify, use easy_install or pip:

    $ easy_install nose-pynotify

    $ pip install nose-pynotify

Or you can get it from the PyPI page/github repo and install it manually with
`setuptools`:

    $ python setup.py install

Usage
-----
After installing, the following options will be added to the nosetests command:

    --with-pynotify      Enable the plugin and produce a notification bubble at
                         the end of testing with the number of successes,
                         errors, and failures listed. Disabled by default.
    --show-each-error    Produce a notification for each error as they are
                         found. Disabled by default.
    --show-each-failure  Produce a notification for each failure as they are
                         found. Disabled by default.

The following environment variables produce the same behavior as their above
counterparts when set:

    NOSE_WITH_PYNOTIFY
    NOSE_SHOW_EACH_ERROR
    NOSE_SHOW_EACH_FAILURE

For example, to enable the plugin's default notification and show each failure
as it is encountered, you could do one of the following:

    $ nosetests --with-pynotify --show-each-failure

Or:

    $ echo "export NOSE_WITH_PYNOTIFY=1" >> ~/.bashrc
    $ echo "export NOSE_SHOW_EACH_ERROR=1" >> ~/.bashrc

    $ ...

    $ nosetests

License
-------
Copyright (c) 2011 Colin Drake

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
