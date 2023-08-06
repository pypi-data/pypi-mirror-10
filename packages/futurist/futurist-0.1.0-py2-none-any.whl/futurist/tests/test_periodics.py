# -*- coding: utf-8 -*-

# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import contextlib
import functools
import threading
import time

import eventlet
from eventlet.green import threading as green_threading
import testscenarios

import futurist
from futurist import periodics
from futurist.tests import base


@periodics.periodic(1)
def every_one_sec(cb):
    cb()


@periodics.periodic(0.5)
def every_half_sec(cb):
    cb()


@contextlib.contextmanager
def create_destroy_thread(run_what, *args, **kwargs):
    t = threading.Thread(target=run_what, args=args, kwargs=kwargs)
    t.daemon = True
    t.start()
    try:
        yield
    finally:
        t.join()


@contextlib.contextmanager
def create_destroy_green_thread(run_what, *args, **kwargs):
    t = eventlet.spawn(run_what, *args, **kwargs)
    try:
        yield
    finally:
        t.wait()


class TestPeriodicsStrategies(base.TestCase):
    def test_invalids(self):
        self.assertRaises(ValueError,
                          periodics.PeriodicWorker, [],
                          schedule_strategy='not_a_strategy')


class TestPeriodics(testscenarios.TestWithScenarios, base.TestCase):
    scenarios = [
        ('sync', {'executor_cls': futurist.SynchronousExecutor,
                  'executor_kwargs': {},
                  'create_destroy': create_destroy_thread,
                  'sleep': time.sleep,
                  'worker_kwargs': {}}),
        ('thread', {'executor_cls': futurist.ThreadPoolExecutor,
                    'executor_kwargs': {'max_workers': 2},
                    'create_destroy': create_destroy_thread,
                    'sleep': time.sleep,
                    'worker_kwargs': {}}),
        ('green', {'executor_cls': futurist.GreenThreadPoolExecutor,
                   'executor_kwargs': {'max_workers': 10},
                   'sleep': eventlet.sleep,
                   'create_destroy': create_destroy_green_thread,
                   'worker_kwargs': {'cond_cls': green_threading.Condition,
                                     'event_cls': green_threading.Event}}),
    ]

    def test_add_on_demand(self):
        called = set()

        def cb(name):
            called.add(name)

        callables = []
        for i in range(0, 10):
            i_cb = functools.partial(cb, '%s_has_called' % i)
            callables.append((every_half_sec, (i_cb,), {}))

        leftover_callables = list(callables)
        w = periodics.PeriodicWorker([], **self.worker_kwargs)
        with self.create_destroy(w.start, allow_empty=True):
            # NOTE(harlowja): if this never happens, the test will fail
            # eventually, with a timeout error..., probably can make it fail
            # slightly faster in the future...
            while len(called) != len(callables):
                if leftover_callables:
                    cb, args, kwargs = leftover_callables.pop()
                    w.add(cb, *args, **kwargs)
                self.sleep(0.1)
            w.stop()

    def test_worker(self):
        called = []

        def cb():
            called.append(1)

        callables = [
            (every_one_sec, (cb,), None),
            (every_half_sec, (cb,), None),
        ]
        executor_factory = lambda: self.executor_cls(**self.executor_kwargs)
        w = periodics.PeriodicWorker(callables,
                                     executor_factory=executor_factory,
                                     **self.worker_kwargs)
        with self.create_destroy(w.start):
            self.sleep(2.0)
            w.stop()

        am_called = sum(called)
        self.assertGreaterEqual(am_called, 4)
