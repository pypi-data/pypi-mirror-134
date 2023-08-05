from typing import Optional
from qns.simulator.simulator import Simulator
from qns.simulator.event import Event
from qns.simulator.ts import Time
from qns.entity.entity import Entity


class Timer(Entity):
    """
    A `Timer` is an `Entity` that trigger the function `trigger_func` one-shot or periodically.
    """
    def __init__(self, name: str, start_time: float, end_time: float = 0,
                 step_time: float = 1, trigger_func=None):
        """
        Args:
            name: the timer's name
            start_time (float): the start time of the first event
            end_time (float): the time of the final trigger event.
                If `end_time` is 0, it will be trigger only once.
            step_time (float): the period of trigger events. Default value is 1 second.
            trigger_func: the function that will be triggered.
        """
        super().__init__(name=name)
        self.start_time = start_time
        self.end_time = end_time
        self.step_time = step_time
        self.trigger_func = trigger_func

    def install(self, simulator: Simulator) -> None:

        if not self._is_installed:
            self._simulator = simulator

            time_list = []
            if self.end_time == 0:
                time_list.append(Time(sec=self.start_time))
            else:
                t = self.start_time
                while t <= self.end_time:
                    time_list.append(t)
                    t += self.step_time

            for t in time_list:
                time = self._simulator.time(sec=t)
                event = TimerEvent(timer=self, t=time)
                self._simulator.add_event(event)
            self._is_installed = True

    def trigger(self):
        if self.trigger_func is not None:
            self.trigger_func()
        else:
            raise NotImplementedError


class TimerEvent(Event):
    """
    TimerEvent is the event that triggers the Timer's `trigger_func`
    """
    def __init__(self, timer: Timer, t: Optional[Time] = None, name: Optional[str] = None):
        super().__init__(t=t, name=name)
        self.timer = timer

    def invoke(self) -> None:
        self.timer.trigger()
