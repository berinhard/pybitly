Introduction
------------
pybitly is a tool to consume the Bit.ly API.

The objectve of this project is to create a client to the Bit.ly API.
It already exists a Python project to serve as such a client but there is no command line tool.
It's just a Python module that you can use it to consume the API inside your project.
Besides that, I'm using this project to practise, get more confident with Python programming and learn more about it.


Dependencies
------------
To run the tests you need the "mock" module. To install "mock", execute:

    sudo pip install mock

or

    sudo easy_install mock

Check the mock project at: http://pypi.python.org/pypi/mock/


Usage
-----
To use the command "pybitly" directly, put the path to this project on your $PATH.
Add this line to the end of the ~/.bashrc file:

    PATH="$PATH:/path/to/pybitly/repository"

So, to load this new ~/.bashrc, open a new bash session or execute:

    . ~/.bashrc

And then you can use it from any directory in your bash:

    pybitly http://big-url-to-be-shorten/

So the short URL will be shown on the terminal. Enjoy! :-)
