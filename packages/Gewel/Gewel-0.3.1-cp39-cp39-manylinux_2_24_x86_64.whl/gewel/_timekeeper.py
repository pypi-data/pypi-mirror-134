from typing import Iterable, Protocol, Union

import tvx


# noinspection PyPropertyDefinition
class TimekeeperProtocol(Protocol):
    @property
    def time(self) -> float: ...

    def set_time(self, time: float): ...

    def _manage_time(self, duration: float, update_time: bool): ...


class TimekeeperMixin:
    """
    This mixin is used by classes that need to keep track
    of a next-action time during the scripting phase. Next-action
    time is the time that the next action, for example, the motion
    created by the next call to :py:meth:`~XYDrawable.move_to`, will
    begin.

    See :ref:`draw_update_time` for more on next-action time.
    """

    def _manage_time(self: 'TimekeeperProtocol', duration: float, update_time: bool):
        if update_time:
            self.set_time(self.time + duration)

    def wait(self, duration: float) -> None:
        """
        Wait for a specified amount of time. This updates
        the object's next-action time by adding a constant
        amount of time to it.

        See :ref:`draw_update_time` for more on next-action time.

        Parameters
        ----------
        duration
            How long to wait, in seconds.
        """
        self._manage_time(duration, True)

    def wait_until(self: 'TimekeeperProtocol', at_least: float) -> None:
        """
        Update the next-action time so that it is at least
        the given time. If it is already greater than that,
        change nothing.

        See :ref:`draw_update_time` for more on next-action time.

        Parameters
        ----------
        at_least
            The minimum new next-action time.
        """
        if at_least > self.time:
            self._manage_time(at_least - self.time, True)

    def wait_for(
            self,
            other: Union['TimekeeperMixin', Iterable['TimekeeperMixin']]
    ) -> None:
        """
        Wait for another object to finish whatever action it is currently
        doing. This method us used at scripting time to ensure that an
        object updates its next-action time so that it is no earlier than
        the next-action time of another object.

        See :ref:`draw_update_time` for more on next-action time.

        Parameters
        ----------
        other
            The object to wait for. Or, an iterable collection of
            objects. If iterable, then wait for the one with the
            latest time.
        """
        if isinstance(other, TimekeeperMixin):
            self.wait_until(getattr(other, 'time'))
        else:
            for o in other:
                self.wait_for(o)

    def ramp_attr_to(
            self: 'TimekeeperProtocol',
            name: str,
            to: float,
            duration: float,
            update_time: bool = True
    ) -> None:
        """
        Change the value of an attribute of the object from the
        value it has at the current next-action time to a new value
        by ramping it linearly between the old and new values over
        the course of a given duration.

        See :ref:`draw_update_time` for more on next-action time.

        Parameters
        ----------
        name
            Name of the attribute to update.
        to
            Value to change to.
        duration
            Time in seconds over which the value ramps from the
            old to the new value.
        update_time
            If ``True``, update the object's next-action time so
            that it is ``duration`` later than it was.
        """
        frm = getattr(self, name)
        if isinstance(frm, tvx.Tvf):
            frm_val = frm(self.time)
        else:
            frm_val = frm
        rmp = tvx.ramp(frm_val, to, self.time, duration)
        ct = tvx.cut(frm, self.time, rmp)
        setattr(self, name, ct)
        self._manage_time(duration, update_time)


def sync(tks: Iterable[Union[TimekeeperMixin, TimekeeperProtocol]]) -> None:
    """
    Synchronize objects so that all of their next-action times are
    set to the latest next-action time of any of them.

    See :ref:`draw_update_time` for more on next-action time.

    Parameters
    ----------
    tks
        The objects to synchronize.
    """
    if not isinstance(tks, list):
        tks = list(tks)
    max_time = max([tk.time for tk in tks])
    for tk in tks:
        tk.wait_until(max_time)


def all_wait_for(waiters: Iterable[TimekeeperMixin], waited_on: TimekeeperMixin) -> None:
    """
    Have all of the objects in a group wait for the latest
    of the objects in another group.

    Parameters
    ----------
    waiters
        Objects that should wait.
    waited_on
        Objects that should be waited on.
    """
    for w in waiters:
        w.wait_for(waited_on)
