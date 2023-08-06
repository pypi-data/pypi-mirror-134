from abc import ABC as _ABC, abstractmethod as _abstractmethod
from collections import deque as _deque
from itertools import cycle as _cycle

import numpy as _np


class Synchronization(_ABC):

    _signal_seq = None

    @_abstractmethod
    def signal(self):
        """sending signal"""

    @_abstractmethod
    def leading(self):
        '''leading model'''

    @_abstractmethod
    def supporting(self):
        '''supporting model'''

    def set_model(self, shift=0):
        dq = _deque([self.leading, self.supporting])
        dq.rotate(shift)
        self._cyc =_cycle(dq)
        return self._cyc

    def _sync(self):
        return next(self._cyc)

    def get_signal(self):
        if self._signal_seq is None:
            self._signal_seq = []

        signal = self.signal()
        self._signal_seq.append(signal)
        return signal

    @property
    def signal_seq(self):
        return _np.array(self._signal_seq)

    @property
    def sync(self):
        try:
            return next(self._cyc)
        except AttributeError:
            raise AttributeError(f'need {self.__class__.__name__}.set_model()')

from inspect import getfullargspec as _getfullargspec

def _check_oscillator(oscillators):
    for o in oscillators:
        if not isinstance(o, Synchronization):
            raise TypeError(
                f'{o.__class__.__name__} need to have Synchronization')


def _func_checker(func, params):
    signals = _getfullargspec(func).args
    for r in ['t', 'u', 'self']:
        signals.remove(r)
    params = {s:p for s, p in zip(signals, params)}
    params['f'] = func

    return params

def connection_in_one_direction(o1, o2, N):
    _check_oscillator([o1, o2])

    for _ in range(N):
        signal1 = o1.get_signal()
        signal2 = o2.get_signal()

        p1 = _func_checker(o1.leading, [signal2])
        p2 = _func_checker(o2.supporting, [signal1])

        o2.solve(*o2.internal_state, **p2)
        o1.solve(*o1.internal_state, **p1)

    return o1, o2


def connection_in_switching(o1, o2, N):
    _check_oscillator([o1, o2])

    o1.set_model()
    o2.set_model(1)

    for _ in range(N):
        signal1 = o1.get_signal()
        signal2 = o2.get_signal()

        p1 = _func_checker(o1.sync, [signal2])
        p2 = _func_checker(o2.sync, [signal1])

        o1.solve(*o1.internal_state, **p1)
        o2.solve(*o2.internal_state, **p2)

    return o1, o2

def _test_plot_error(Ocs):
    from itertools import cycle

    import matplotlib as mpl
    import numpy as np

    from ..utils._draw import Drawing

    def make(u1, u2):
        o1 = Ocs()
        o1.u = u1

        o2 = Ocs()
        o2.u = u2
        o2.r=28.1

        return o1, o2

    u1 = Ocs.on_attractor().u
    u2 = u1 - 10

    d = Drawing(2, 1)

    color = cycle(mpl.rcParams['axes.prop_cycle'])

    for func in [connection_in_one_direction,
                 connection_in_switching]:
        c = next(color)['color']

        o1, o2 = make(u1, u2)

        func(o1, o2, 2000)

        label = func.__name__[11:].replace('_', ' ')

        for i in range(1,3):
            d_ = np.abs(o1.u_seq[:,i]-o2.u_seq[:,i])
            d[i-1,0].plot(d_, label=label, color=c, linewidth=0.5)
            d[i-1,0].plot([len(d_)-500, len(d_)],
                          [np.average(d_[-500:]) for _ in range(2)],
                          color=c, linestyle='dashed', linewidth=1)

    for i, a in enumerate(['y', 'z']):
        d[i,0].set_axis_label('step', f'|{a}_1-{a}_2|')
        d[i,0].set_yscale('log')
        d[i,0].set_ylim(10**(-16), 100)

    d[0,0].legend()
    d[0,0].set_title(f'${Ocs.__name__}$')
    d.show()
    d.close()

    return make(u1, u2)

if __name__ == '__main__':
    from ..equations import Lorenz

    class Difusion(Lorenz, Synchronization):
        def signal(self):
            self.signal_sent = self.u[0]
            return self.u[0]

        def leading(self, t, u, signal_received):
            s, r, b = self.s, self.r, self.b

            x, y, z = u

            x_dot = s*(y - x) - 100*(x-signal_received)
            y_dot = r*x  - y - x*z
            z_dot = x *y - b*z

            return x_dot, y_dot, z_dot

        def supporting(self, t, u, signal_received):
            return self.leading(t, u, signal_received)

    o1, o2 = connection_in_one_direction(Difusion.on_attractor(), Difusion.on_attractor(), 100)

    print(o1.u_seq)
