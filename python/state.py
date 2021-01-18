from abc import ABC, abstractmethod


class DisplayState(ABC):
    """
    Display state interface to be implemented by each of the state level
    """

    @abstractmethod
    def turn_on(self) -> None:
        pass

    @abstractmethod
    def turn_off(self) -> None:
        pass


class DisplayStateContext:
    """
    Holds the current state as well as, responsible of changing states
    """

    _state: DisplayState = None

    def __init__(self):
        print(type(self).__name__ + ":" + __name__)

    def set_state(self, state: DisplayState):
        self._state = state
        print(DisplayStateContext.set_state.__qualname__ + ":" + state.__class__.__name__)

    def get_state(self) -> DisplayState:
        return self._state


class DisplayStateCharging(DisplayState):
    """
    A state: While device is charging
    """
    _timeout: int = 5

    def __init__(self):
        print(type(self).__name__ + ":" + __name__)

    def turn_on(self) -> None:
        print(DisplayStateCharging.turn_on.__qualname__)

    def turn_off(self) -> None:
        print(DisplayStateCharging.turn_off.__qualname__)

    def dim_screen(self, brightness_level: int) -> None:
        print(DisplayStateCharging.dim_screen.__qualname__ + "=" + brightness_level)


class DisplayStateNormal(DisplayState):
    """
    A state: while device is enough charged and not connected to charger
    """
    _timeout: int = 4

    def __init__(self):
        print(type(self).__name__ + ":" + __name__)

    def turn_on(self) -> None:
        print(DisplayStateNormal.turn_on.__qualname__)

    def turn_off(self) -> None:
        print(DisplayStateNormal.turn_off.__qualname__)

    def set_timeout(self, timeout):
        self._timeout = timeout

    def dim_screen(self, brightness_level: int) -> None:
        print(type(self).__name__ + ":" + __name__ + "=" + brightness_level)


class DisplayStateLowPower(DisplayState):
    """
    A state: While device is being charged
    """

    def __init__(self):
        print(type(self).__name__ + ":" + __name__)

    def turn_on(self) -> None:
        print(DisplayStateLowPower.turn_on.__qualname__)

    def turn_off(self) -> None:
        print(DisplayStateLowPower.turn_off.__qualname__)

    def dim_screen(self, timeout, brightness_level) -> None:
        pass


if __name__ == "__main__":
    display = DisplayStateContext()
    display.set_state(DisplayStateCharging())
    display.get_state().turn_on()
    display.get_state().turn_off()
    display.set_state(DisplayStateNormal())
    display.get_state().turn_on()
    display.set_state(DisplayStateLowPower())
    display.get_state().turn_on()
    display.get_state().turn_off()

