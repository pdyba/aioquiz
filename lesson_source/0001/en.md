Installation
============

For our workshop, we will need a Python 3.4 interpreter. Below are some
directions on how to check if you already have the interpreter and how
to install it along with some other tools.

Windows
-------

You can download Python for Windows directly from [python.org]. After
downloading the file `*.msi`, open it and follow the instructions. It is
important to remember the path of installation – the directory – as we
will need this information during the
installation of tools &lt;tools&gt;.

Linux (Ubuntu, Fedora, etc.) or Mac
-----------------------------------

In order to check our version of Python, enter the following in the
command line:

    :::bash
    $ python --version
    Python 3.5.0


If the `python` command is not available or the wrong version appears:

### Ubuntu

Enter in the command line:

    :::bash
    sudo apt-get install python3.4


### Fedora

Enter in the command line:

    :::bash
    sudo yum install python3.4
****

### OS X

Download and install the package for your system version from
[python.org] .

### Other

Use the system of packages adequate for your distribution. If there is
no adequate system or you cannot find python, you can install it using
the sources on the [python.org]. website. A compiler and readline
library will be required.

Unofficially, we assume that the users of less popular (but not worse!)
distributions will manage the task without any problem :).

Tools
-----

### Windows command line

We will do most of our work on the command line. To activate the command
line in Windows, press `Win+R`. In the open window, type `cmd` and click
`OK`. A new window will appear with white text on a black background:

    :::bash
    Microsoft Windows [Version 6.1.7601]
    Copyright (c) 2009 Microsoft Corporation. All rights reserved.


    C:\Users\Name>


Text may be different depending on the version of Windows you use.

`C:\Users\Name>` is a prompt. It informs us of the directory (or folder)
in which we currently are and waits for a command. Later during the
workshop `C:\Users\Name>` we will refer to it with `~$`, independently
of your operating system (Windows, Linux, MacOS).

Using the command line, you can move around the contents of the disc (in
the same way as in `My Computer`). You can do that by entering commands
and pressing `Enter`. Use the following commands:

`dir`

Displays the contents of the current directory. For example, if the
`prompt` shows `C:\Users\Name`, the `dir` command displays the
contents of our home directory.

`cd directory`

Changes the current directory. For example, if you are in
`C:\Users\Name`, you can access the directory with your documents by
entering `cd Documents`. If you execute the `dir` command, you will
see something familiar. The command `cd..` will move you one level
up in the directory tree, that is, to the directory that cont

    :::python3
    from sanic import Sanic
    from sanic.response import json

    app = Sanic()

    @app.route("/")
    async def test(request):
        return json({"hello": "world"})

    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=8000)

[python.org](http://python.org)