
aio.config usage
================


Config finder
-------------

>>> import os
>>> import tempfile
>>> import aio.config


Lets create a directory with an "aio.conf" file in

aio.config.find_config should find it

>>> with tempfile.TemporaryDirectory() as tmp:
...     config = os.path.join(tmp, "aio.conf")
...     with open(config, "w") as conf:
...         res = conf.write("")
...     
...     aio.config.find_config(app_dir=tmp) == config
True


Lets create a directory with an "etc/aio.conf" file in

aio.config.find_config should find it

>>> with tempfile.TemporaryDirectory() as tmp:
...     os.mkdir(os.path.join(tmp, "etc"))
...     config = os.path.join(tmp, "etc", "aio.conf")
...     with open(config, "w") as conf:
...         res = conf.write("")
...     
...     aio.config.find_config(app_dir=tmp) == config
True


Lets create a directory with both a "aio.conf" and an "etc/aio.conf" file in

aio.config.find_config should find the "aio.conf" file

>>> with tempfile.TemporaryDirectory() as tmp:
...     os.mkdir(os.path.join(tmp, "etc"))
...     config = os.path.join(tmp, "aio.conf")
...     etc_config = os.path.join(tmp, "etc", "aio.conf")
...     with open(config, "w") as conf:
...         res = conf.write("")
...     
...     aio.config.find_config(app_dir=tmp) == config
True


Lets create a directory with an "custom.conf" file in

aio.config.find_config should find it when passed the filename= arg

>>> with tempfile.TemporaryDirectory() as tmp:
...     config = os.path.join(tmp, "custom.conf")
...     with open(config, "w") as conf:
...         res = conf.write("")
...     
...     aio.config.find_config(
...         app_dir=tmp, filename="custom.conf") == config
True


Module config
-------------

aio.config.gather_config gathers configurations from modules


Lets create a function for creating some fake eggs

>>> def fake_egg(folder, name):
...     egg_folder = os.path.join(folder, name)
...     os.mkdir(egg_folder)
...     egg_init = os.path.join(egg_folder, "__init__.py")
...     with open(egg_init, "w") as init:
...         res = init.write("")

>>> import sys
>>> from zope.dottedname.resolve import resolve

Add a couple of fake eggs and add aio.conf files to the module path

Gather config should find these conf files

>>> with tempfile.TemporaryDirectory() as tmp:
...     fake_egg(tmp, "example_egg_1")
...     fake_egg(tmp, "example_egg_2")
...     egg_1_conf = os.path.join(tmp, "example_egg_1", "aio.conf")
...     egg_2_conf = os.path.join(tmp, "example_egg_2", "aio.conf")
...     sys.path.append(tmp)
...     with open(egg_1_conf, "w") as init:
...         res = init.write("[foo]\neggs = eggs")
...     with open(egg_2_conf, "w") as init:
...         res = init.write("[bar]\nspam = spam")
...     (aio.config.gather_config(
...         [resolve("example_egg_1"), resolve("example_egg_2")])
...      == [egg_1_conf, egg_2_conf])
True
