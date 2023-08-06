"""Class implementation for the animation_pause interface.
"""

from apysc._type.variable_name_interface import VariableNameInterface


class AnimationPauseInterface(VariableNameInterface):

    def animation_pause(self) -> None:
        """
        Stop the all animations.

        References
        ----------
        - animation_pause and animation_play interfaces document
            - https://bit.ly/3m2Xh8Y
        """
        import apysc as ap
        with ap.DebugInfo(
                callable_=self.animation_pause, locals_=locals(),
                module_name=__name__, class_=AnimationPauseInterface):
            expression: str = (
                f'{self.variable_name}.timeline().pause();'
            )
            ap.append_js_expression(expression=expression)
