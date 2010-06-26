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

Check the mock project at [http://pypi.python.org/pypi/mock/](http://pypi.python.org/pypi/mock/)


Installation
------------
To download pybitly and add the project path to your ~/.bashrc, just execute:

    cd
    wget http://github.com/turicas/pybitly/tarball/master -O pybitly.tar.gz
    tar xfz pybitly.tar.gz
    rm pybitly.tar.gz
    mv *-pybitly-* pybitly
    echo 'PATH="$PATH:'$(pwd)'/pybitly"' >> .bashrc
    . .bashrc



Usage
-----

    pybitly http://big-url-to-be-shorten/

The short URL will be shown on the terminal.
Enjoy! :-)
