# This file is placed in the Public Domain.


"table"


import _thread


from .fnc import register
from .obj import Object, get


def __dir__():
    return (
        "Cbs",
        "Cls",
        "Cmd",
        "Dpt",
        "Tbl",
    )


cmdlock = _thread.allocate_lock()


class Cls(Object):

    cls = Object()

    @staticmethod
    def add(clz):
        register(Cls.cls, "%s.%s" % (clz.__module__, clz.__name__), clz)

    @staticmethod
    def full(name):
        name = name.lower()
        res = []
        for cln in Cls.cls:
            if cln.split(".")[-1].lower() == name:
                res.append(cln)
        return res

    @staticmethod
    def get(nm):
        return get(Cls.cls, nm)


class Cmd(Object):

    cmd = Object()
    errors = []

    @staticmethod
    def add(cmd):
        register(Cmd.cmd, cmd.__name__, cmd)

    @staticmethod
    def dispatch(e):
        e.parse()
        f = Cmd.get(e.cmd)
        if f:
            f(e)
            e.show()

    @staticmethod
    def handle(e):
        try:
            Cmd.dispatch(e)
        except Exception as ex:
            e.errors.append(ex)
            Cmd.errors.append(ex)
        finally:
            e.ready()

    @staticmethod
    def get(cmd):
        f =  get(Cmd.cmd, cmd)
        return f

class Dpt(Object):

    cbs = Object()

    @staticmethod
    def add(name, cb):
        register(Dpt.cbs, name, cb)

    @staticmethod
    def dispatch(clt, e):
        e.parse()
        cb = Dpt.get(e.command)
        if cb:
            cb(clt, e)
        e.ready()

    @staticmethod
    def get(cmd):
        return get(Dpt.cbs, cmd)


class Tbl(Object):

    mod = Object()

    @staticmethod
    def add(o):
        Tbl.mod[o.__name__] = o

    @staticmethod
    def get(nm):
        return get(Tbl.mod, nm, None)
