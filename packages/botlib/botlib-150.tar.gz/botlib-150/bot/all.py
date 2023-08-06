# This file is placed in the Public Domain.


"bot package modules"

from bot.tbl import Tbl


from bot import bus
from bot import cfg
from bot import clt
from bot import dbs
from bot import evt
from bot import fnc
from bot import hdl
from bot import jsn
from bot import krn
from bot import prs
from bot import spc
from bot import tbl
from bot import thr
from bot import tms


Tbl.add(bus)
Tbl.add(cfg)
Tbl.add(clt)
Tbl.add(dbs)
Tbl.add(evt)
Tbl.add(fnc)
Tbl.add(hdl)
Tbl.add(jsn)
Tbl.add(krn)
Tbl.add(prs)
Tbl.add(tbl)
Tbl.add(thr)
Tbl.add(tms)


from bot import bsc
from bot import irc
from bot import rss
from bot import udp


Tbl.add(bsc)
Tbl.add(irc)
Tbl.add(rss)
Tbl.add(udp)
