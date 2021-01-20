# Strategy/Policy Design pattern
from abc import ABC, abstractmethod

strategyList = []


class InstructionStrategy(ABC):

    @abstractmethod
    def process_instruction(self, buff):
        pass


class GestureInstructionStrategy(InstructionStrategy):
    def process_instruction(self, buff):
        print(self.__class__.__name__ + " " + self.process_instruction.__name__)


class VoiceInstructionStrategy(InstructionStrategy):
    def process_instruction(self, buff):
        print(self.__class__.__name__ + " " + self.process_instruction.__name__)
        pass


class SensorInstructionStrategy(InstructionStrategy):

    def process_instruction(self, buff):
        print(self.__class__.__name__ + " " + self.process_instruction.__name__)
        pass


class Context:

    _strategy = None

    def __init__(self, strategy: InstructionStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy) -> None:
        self._strategy = strategy

    def get_strategy(self):
        return self._strategy

    def interpret_instruction(self, data):
        return self._strategy.process_instruction(data)


if __name__ == "__main__":
    print("Strategy Pattern Demo")
    context = Context(SensorInstructionStrategy())
    context.get_strategy()
    context.interpret_instruction(None)

    context.set_strategy(GestureInstructionStrategy())
    context.get_strategy()
    context.interpret_instruction(None)

    context.set_strategy(VoiceInstructionStrategy())
    context.get_strategy()
    context.interpret_instruction(None)
