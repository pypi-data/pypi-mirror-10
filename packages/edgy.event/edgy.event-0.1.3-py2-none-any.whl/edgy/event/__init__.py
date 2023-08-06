from __future__ import absolute_import

import operator


class Event(object):
    propagation_stopped = False

    def stop_propagation(self):
        self.propagation_stopped = True


class EventDispatcher(object):
    def __init__(self):
        self._listeners = {}
        self._sorted = {}

    def dispatch(self, event_name, event = None):
        if event is None:
            event = Event()

        event.dispatcher = self
        event.name = event_name

        if not event_name in self._listeners:
            return event

        self.do_dispatch(self.get_listeners(event_name), event_name, event)

        return event

    def get_listeners(self, event_name=None):
        if event_name is not None:
            if not event_name in self._sorted:
                self.sort_listeners(event_name)

            return self._sorted[event_name]

        for event_name in self._listeners:
            if not event_name in self._sorted:
                self.sort_listeners(event_name)

        return self._sorted

    def has_listeners(self, event_name=None):
        return bool(len(self.get_listeners(event_name)))

    def add_listener(self, event_name, listener, priority=0):
        if not event_name in self._listeners:
            self._listeners[event_name] = {}
        if not priority in self._listeners[event_name]:
            self._listeners[event_name][priority] = []
        self._listeners[event_name][priority].append(listener)

        if event_name in self._sorted:
            del self._sorted[event_name]

    def listen(self, event_name, priority=0):
        """
        Decorator that add the decorated functions as one of this instance listeners, for the given event name.

        :param event_name:
        :param priority:
        :return:

        """

        def wrapper(listener):
            self.add_listener(event_name, listener, priority)
            return listener

        return wrapper

    def remove_listener(self, event_name, listener):
        if not event_name in self._listeners:
            return

        for priority, listeners in self._listeners[event_name]:
            if listener in self._listeners[event_name][priority]:
                # pylint: disable=filter-builtin-not-iterating
                self._listeners[event_name][priority] = filter(
                    lambda l: l != listener,
                    self._listeners[event_name][priority]
                )
                if event_name in self._sorted:
                    del self._sorted[event_name]

    def do_dispatch(self, listeners, event_name, event):
        for listener in listeners:
            listener(event)
            if event.propagation_stopped: break

    def sort_listeners(self, event_name):
        self._sorted[event_name] = []
        if event_name in self._listeners:
            self._sorted[event_name] = [
                listener for listeners in sorted(
                    self._listeners[event_name].items(), key=operator.itemgetter(0)
                ) for listener in listeners[1]
            ]


__all__ = [
    Event,
    EventDispatcher
]
