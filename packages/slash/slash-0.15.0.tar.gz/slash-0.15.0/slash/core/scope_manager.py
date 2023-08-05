import functools

import logbook

from ..utils.python import call_all_raise_first

_logger = logbook.Logger(__name__)

class ScopeManager(object):

    def __init__(self, session):
        super(ScopeManager, self).__init__()
        self._session = session
        self._scopes = []
        self._last_module = self._last_test = None

    def begin_test(self, test):
        test_module = test.__slash__.module_name
        if self._last_module is None:
            self._push_scope('session')
            self._push_scope('module')
        elif self._last_module != test_module:
            self._push_scope('module')
        self._last_module = test_module
        self._push_scope('test')
        self._last_test = test

    def end_test(self, test, next_test, exc_info):
        assert test == self._last_test

        exc_type = exc_info[0]
        kw = {'in_failure': exc_type is not None, 'in_interruption': exc_type is KeyboardInterrupt}

        self._pop_scope('test', **kw)
        if next_test is None or next_test.__slash__.module_name != self._last_module:
            self._pop_scope('module', **kw)
        if next_test is None:
            self._pop_scope('session', **kw)


    def _push_scope(self, scope):
        self._scopes.append(scope)
        self._session.fixture_store.push_scope(scope)
        self._session.cleanups.push_scope(scope)

    def _pop_scope(self, scope, **kw):
        assert self._scopes.pop() == scope
        call_all_raise_first([self._session.cleanups.pop_scope, self._session.fixture_store.pop_scope],
                             scope, **kw)

    def flush_remaining_scopes(self, **kw):
        call_all_raise_first([functools.partial(self._pop_scope, s)
                              for s in self._scopes[::-1]], **kw)
