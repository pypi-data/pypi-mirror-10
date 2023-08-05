r"""ssfsm is a finite-state-machine implementation with the most simple syntax
I could come up with."""

VERSION = "0.6.0"

def Machine(*nargs, **kwargs):
    """Returns a new :py:class:`FSM_Machine`"""
    return FSM_Machine(*nargs, **kwargs)

class FSM_Machine(object):
    """The machine"""

    __states = None
    __active_state = None
    __initial_state = None
    __alphabet = None

    def __init__(self, initial_state=None):
        self.__states = {}
        self.__alphabet = frozenset()
        if not (initial_state is None):
            self().reset(self[initial_state])

    def __get_state(self, name):
        if name in self:
            return self.__states[name]
        return self.__create_state(name)

    def __contains__(self, item):
        return item in self.__states

    def __len__(self):
        return len(self.__states)

    def __nonzero__(self):
        return bool(self.__active_state.accepting)

    def __bool__(self):
        return bool(self.__active_state.accepting)

    def __create_state(self, name):
        if name in self:
            raise ValueError("State allready created")
        new_state = FSM_State(self, name)
        self.__states[name] = new_state
        return new_state

    def __deepcopy(self):
        copy = FSM_Machine()
        copy().alphabet = self.__alphabet
        for key in self.__states:
            copy[key] = self.__states[key].accepting
            if self.__initial_state is self.__states[key]:
                copy().reset(copy[key])
            if self.__active_state is self.__states[key]:
                copy().state = copy[key]
        for key in self.__states:
            for transition in self.__states[key].transitions:
                copy[key][transition] = copy[self.__states[key][transition].name]
        return copy

    def __deepcopy__(self, _):
        return self.__deepcopy()

    def __enter__(self):
        return self.__deepcopy()

    def __exit__(self, _type, value, traceback):
        pass

    def __eq__(self, other):
        raise NotImplementedError()

    def __call__(self, transition=None):
        if transition is None:
            machine = self
            class FSM_Machine_Controller(object):
                def __init__(self, parent):
                    self.parent = parent

                def __call__(self):
                    # @TODO Is this the expected behaviour?
                    return self.state

                @property
                def accepting(self):
                    return bool(machine)

                @property
                def states(self):
                    return frozenset(machine._FSM_Machine__states.values())

                @property
                def states_names(self):
                    return frozenset(s.name for s in self.states)

                @property
                def state(self):
                    return machine._FSM_Machine__active_state

                @state.setter
                def state(self, state):
                    machine._FSM_Machine__change_state(state)

                @property
                def deterministic(self):
                    from itertools import product
                    return (machine._FSM_Machine__initial_state in self.states) and all((trans in state) for (state, trans) in product(self.states, self.alphabet))

                def reset(self, initial_state=None):
                    if initial_state is None:
                        machine._FSM_Machine__change_state(machine._FSM_Machine__initial_state)
                    else:
                        if initial_state.parent is self.parent:
                            machine._FSM_Machine__initial_state = initial_state
                            self.reset()
                        else:
                            raise ValueError("States are not in the same machine")

                @property
                def alphabet(self):
                    s = machine._FSM_Machine__alphabet
                    for state in self.states:
                        s = s | state.transitions
                    return s

                @alphabet.setter
                def alphabet(self, val):
                    to_delete = self.alphabet - frozenset(val)
                    machine._FSM_Machine__alphabet = frozenset(val)
                    for state in self.states:
                        for d in to_delete:
                            if d in state:
                                del state[d]

                @property
                def transitions(self):
                    def __transitions():
                        for fro in self.states:
                            for trans in fro.transitions:
                                yield (fro, trans, fro[trans])
                    return frozenset(__transitions())

                def polyfill(self, target=None):
                    for state in self.states:
                        for transition in self.alphabet:
                            if not transition in state:
                                if not target:
                                    state[transition] = state
                                else:
                                    state[transition] = target

            return FSM_Machine_Controller(self)

        try:
            for t in transition:
                self.__change_state(self.__active_state(t))
        except TypeError:
            try:
                self.__change_state(self.__active_state(transition))
            except TypeError:
                raise ValueError('No State initialized. Set an initial state with Machine().reset(state).')
        return self().state

    def __change_state(self, state):
        if not state.parent is self:
            raise ValueError("States are not in the same machine")
        self.__active_state = state
        return state

    def __getitem__(self, key):
        if key == '_':
            return self()
        return self.__get_state(key)

    def __setitem__(self, key, value):
        self.__get_state(key).accepting = value

    def __delitem__(self, key):
        name = key
        if name in self:
            state = self.__states[name]
            if self.__active_state is state:
                self.__active_state = None
            del self.__states[name]
            for o_name in self.__states:
                self.__states[o_name].delete(state)
        else:
            raise KeyError('State doesn\'t exist in this machine')

    def __getattr__(self, name):
        return self[name]

    def __delattr__(self, name):
        del self[name]

    def __setattr__(self, name, value):
        if name.startswith('_'):
            return object.__setattr__(self, name, value)
        self[name] = value

class FSM_State(object):
    """State of a finite state machine"""

    def __init__(self, parent, name):
        self.__parent = parent
        self.__following = {}
        self.__name = name
        self.__accepting = False

    def __call__(self, transition):
        return self.__following[transition]

    @property
    def accepting(self):
        return self.__accepting

    @accepting.setter
    def accepting(self, value):
        if value is True or value is False:
            self.__accepting = value
        else:
            raise TypeError("Accepting must be True or False")

    @property
    def parent(self):
        return self.__parent

    @property
    def name(self):
        return self.__name

    @property
    def transitions(self):
        return frozenset(self.__following.keys())

    def delete(self, f_state):
        to_delete = set()
        for key, value in self.__following.items():
            if value is f_state:
                to_delete.add(key)
        for key in to_delete:
            del self[key]

    def __contains__(self, item):
        return item in self.__following

    def __str__(self):
        return '<state.%s>' % self.name

    def __setitem__(self, key, value):
        if not isinstance(value, FSM_State):
            raise TypeError("Transition target must be a state")
        elif not value.parent is self.parent:
            raise ValueError("States are not in the same machine")
        try:
            for v in key:
                self.__following[v] = value
        except TypeError:
            self.__following[key] = value

    def __getitem__(self, key):
        return self.__following[key]

    def __delitem__(self, key):
        del self.__following[key]


def emmit_before(machine, transition):
    def __emmit(func):
        from functools import wraps
        @wraps(func)
        def wrapper(*args, **kwargs):
            machine(transition)
            return func(*args, **kwargs)
        return wrapper
    return __emmit
emmit = emmit_before

def emmit_after(machine, transition):
    def __emmit(func):
        from functools import wraps
        @wraps(func)
        def wrapper(*args, **kwargs):
            tmp = func(*args, **kwargs)
            machine(transition)
            return tmp
        return wrapper
    return __emmit
