"""Class implementation for the timer event.
"""

from apysc._event.event import Event
from apysc._time import timer


class TimerEvent(Event):
    """
    Timer event class.

    References
    ----------
    - TimerEvent class document
        - https://simon-ritchie.github.io/apysc/timer_event.html
    """

    _this: 'timer.Timer'

    def __init__(self, this: 'timer.Timer') -> None:
        """
        Timer event class.

        Parameters
        ----------
        this : Timer
            Target timer instance.

        References
        ----------
        - TimerEvent class document
            - https://simon-ritchie.github.io/apysc/timer_event.html
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=TimerEvent):
            from apysc._expression import var_names
            super(TimerEvent, self).__init__(
                this=this, type_name=var_names.TIMER_EVENT)

    @property
    def this(self) -> 'timer.Timer':
        """
        Get a timer instance that listening this event.

        Returns
        -------
        this : TImer
            Instance that listening this event.

        References
        ----------
        - TimerEvent class document
            - https://simon-ritchie.github.io/apysc/timer_event.html
        """
        return self._this
