from setuptools import setup, find_packages

setup(
    name="Pybitly",
    version="1.0",
    packages=find_packages(),
    scripts = ['pybitly'],
    author="Bernardo Fontes",
    author_email="falecomigo@bernardofontes.net",
    long_description="The objectve of this project is to create a client to the Bit.ly API. It already exists a Python project to serve as such a client but there is no command line tool. It's just a Python module that you can use it to consume the API inside your project. Besides that, I'm using this project to practise, get more confident with Python programming and learn more about it.",
    license="LGPL",
    keywords="bitly url short python",
    url="http://www.github.com/berinhard/pybitly"
)
