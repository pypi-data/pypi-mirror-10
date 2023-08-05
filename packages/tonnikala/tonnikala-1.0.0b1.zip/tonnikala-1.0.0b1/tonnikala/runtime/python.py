from __future__ import absolute_import, division, print_function, unicode_literals

NoneType = type(None)

from collections import Mapping
from ..helpers import escape as strescape
from ..compat import text_type, PY3
from collections import deque

from markupsafe import escape


class _TK_buffer(object):
    def __init__(self):
        self._buffer = buffer = []
        e = buffer.extend
        a = buffer.append

        def do_output(*objs):
            for obj in objs:
                if obj.__class__ is _TK_buffer:
                    e(obj._buffer)
                else:
                    a(text_type(obj))

        self.output = do_output
        def output_boolean_attr(name, value):
            t = type(value)
            if t in (bool, NoneType):
                if bool(value):
                    do_output(' ' + name + '="' + name + '"')

                # skip on false, None
                return

            do_output(' ' + name + '="')
            do_output(escape(value))
            do_output('"')

        self.output_boolean_attr = output_boolean_attr


    def __call__(self, *a):
        self.output(*a)


    def __html__(self):
        return self


    def join(self):
        return ''.join(self._buffer)


    if PY3:
        __str__ = join

    else:
        __unicode__ = join
        def __str__(self):
            return self.join().encode('UTF-8')

Buffer = _TK_buffer

try:
    from ._buffer import Buffer as _Buffer, _set_escape_method
    _set_escape_method(escape)
    Buffer = _Buffer
    del _Buffer
    del _set_escape_method
except ImportError as e:
    pass


def output_attrs(values):
    if not values:
        return ''

    if not isinstance(values, Mapping):
        values = iter(values)
    else:
        values = values.items()

    rv = Buffer()
    for k, v in values:
        if v in (True, False, None):
            if v:
                v = k
            else:
                continue

        rv(' ')
        rv(k)
        rv('="')
        rv(escape(v))
        rv('"')

    return rv


def import_defs(href):
    return {}


def bind(context, block=False):
    """
    Given the context, returns a decorator wrapper;
    the binder replaces the wrapped func with the
    value from the context OR puts this function in
    the context with the name.
    """

    if block:
        def decorate(func):
            name = func.__name__.replace('__TK__block__', '')
            if name not in context:
                context[name] = func
            return context[name]

        return decorate

    def decorate(func):
        name = func.__name__
        if name not in context:
            context[name] = func
        return context[name]

    return decorate


class ImportedTemplate(object):
    def __init__(self, name):
        self.__name = name

    def __repr__(self):
        return "<ImportedTemplate '%r'>" % self.name


class TonnikalaRuntime(object):
    bind         = staticmethod(bind)
    Buffer       = staticmethod(Buffer)
    output_attrs = staticmethod(output_attrs)
    escape       = staticmethod(escape)

    def __init__(self):
        self.loader = None

    def load(self, href):
        return self.loader.load(href)

    def import_defs(self, context, href):
        modified_context = context.copy()
        self.loader.load(href).bind(modified_context)
        container = ImportedTemplate(href)

        for k, v in modified_context.items():
            # modified
            if k in context and context[k] is v:
                continue

            setattr(container, k, v)

        return container
