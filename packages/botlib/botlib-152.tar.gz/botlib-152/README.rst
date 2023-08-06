B O T L I B
###########


*os level integration of bot technology*


**BOTLIB** is programmable, to program the bot you have to have the code
available as employing your own code requires that you install your own bot as
the system bot. This is to not have a directory to read modules from to add
commands to the bot but include the own programmed modules directly into the
python code, so only trusted code (your own written code) is included and
runnable. Reading random code from a directory is what gets avoided. As
experience tells os.popen and __import__, importlib are avoided, the bot
scans modules from sys.path (for now).

**BOTLIB** stores it's data on disk where objects are time versioned and the
last version saved on disk is served to the user layer. Files are JSON dumps
that are read-only so thus should provide (disk) persistence more change. Files
paths carry the type in the path name what makes reconstruction from filename
easier then reading type from the object. Only include your own written code
**should** be the path to "secure".

code
----

you can fetch the source code (or clone/fork) from git repository.

``git clone https://github.com/bthate/botlib``


or download the tar from https://pypi.org/project/botlib/#files


object programming
------------------

object Programming provides a “move methods to functions”, if you are used
to functional programming you’ll like it (or not):

``obj.method(*args) -> method(obj, *args)``

not:

>>> from bot.obj import Object
>>> o = Object()
>>> o.set("key", "value")
>>> o.key
'value'

but:

>>> from bot.obj import Object, set
>>> o = Object()
>>> set(o, "key", "value")
>>> o.key
'value'

the bot.obj module has the most basic object functions like get, set, update,
load, save etc.

a dict without methods in it is the reason to factor out methods from the base
object, it is inheritable without adding methods in inherited classes. It also
makes reading json from disk into a object easier because you don’t have any
overloading taking place. Hidden methods are still available so it is not a
complete method less object, it is a pure object what __dict__ is
concerned (user defined methods):


>>> import bot
>>> o = bot.Object()
>>> o.__dict__
{}


modules
-------

| bot.bus      event bus
| bot.clt      client
| bot.dbs	database
| bot.dpt	dispatcher
| bot.evt	event
| bot.fnd	find
| bot.hdl	handler
| bot.irc	irc bot
| bot.log	log command
| bot.obj	objects
| bot.ofn	object functions
| bot.opt	output cache
| bot.prs	parsing
| bot.rpt	repeater
| bot.rss	rss poller
| bot.run	runtime
| bot.sys	system commands
| bot.tbl	table
| bot.thr	threads
| bot.tmr	timer
| bot.tms	times
| bot.utl	utils


commands
--------

cd into the extracted directory and add your module to the bot package.

open your module file, in this example it's the hlo (hello) module:

``joe bot/hlo.py``

add your command code to the file.

::

 def hlo(event):
     event.reply("hello!")

then add your module to the all module so it get imported on start.

``joe bot/all.py``

::

 import bot.hlo as hlo
 Tbl.add(hlo)
