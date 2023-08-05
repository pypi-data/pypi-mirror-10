Pypackage is a collection of python packaging applications including:

    py-build
    py-develop
    py-install
    py-setup
    py-test

The main goal of Pypackage is to make python packaging easier and faster.

Wouldn't it be nice if you could just write some python, run a command, and
have a distributable package? Well now you can!

# Example, "Hello World" application:

```bash
$ mkdir hello_world
$ cd hello_world
$ vim hello_world.py   # write your python here... :)
$ py-build -is
```

The `py-build -is` command will take you through an interactive py-build
session and save the setup.py to disk after creating it, but will not run it.

You can also use the `py-setup` command at any time to print what Pypackage
would use as a setup.py in the current directory's context.

Metadata can be mixed in with site-wide defaults from $HOME/.pypackage if you
want to fill in some common attributes for all your projects.

Pypackage also provides three different test runners to automatically find and
run your tests with `python setup.py test`, you can use any of pytest, nose or
unittest.

To be clear though: pypackage does not intend on replacing setuptools, pip, or
really anything at all in the python packaging tool-chain, it only attempts to
compliment those utilities and make getting started with python packaging a
little easier.

In my utopian perfect dream world, I'd see projects not having a setup.py under
source control, instead only a static metadata file, then having the inverse
relationship being true in the distribution version of the package.

