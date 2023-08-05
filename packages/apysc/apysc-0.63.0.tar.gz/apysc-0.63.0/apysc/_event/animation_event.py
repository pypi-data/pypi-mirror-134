"""Class implementation for the animation event.
"""

from typing import Generic
from typing import TypeVar

from apysc._animation import animation_base
from apysc._event.event import Event
from apysc._type.variable_name_interface import VariableNameInterface

_T = TypeVar('_T', bound=VariableNameInterface)


class AnimationEvent(Event, Generic[_T]):
    """
    Animation event class.
    """

    _this: 'animation_base.AnimationBase[_T]'

    def __init__(
            self, *,
            this: 'animation_base.AnimationBase[_T]') -> None:
        """
        Animation event class.

        Parameters
        ----------
        this : AnimationBase
            Animation setting instance.
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_='__init__', locals_=locals(),
                module_name=__name__, class_=AnimationEvent):
            from apysc._expression import var_names
            super(AnimationEvent, self).__init__(
                this=this, type_name=var_names.ANIMATION_EVENT)

    @property
    def this(self) -> 'animation_base.AnimationBase[_T]':
        """
        Get a animation setting instance that linstening this event.

        Returns
        -------
        this : AnimationBase
            Instance that linstening this event.
        """
        return self._this
