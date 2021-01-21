from abc import ABC, abstractmethod

# 1. Send IoT data over BT/WiFi/Zigbee
# 2. There are two services which needs there own config while both utilizes BT/WiFi/Zigbee. And the reason for choosing
# this design pattern. Sensor services sends data to AWS, Gesture service sends data to Firebase.


class ConnectivityVisitor:
    pass


class Connectivity(ABC):
    @abstractmethod
    def connect(self) -> None:
        pass

    @abstractmethod
    def disconnect(self) -> None:
        pass

    @abstractmethod
    def transmit(self, data: []) -> None:
        pass

    # add visitor
    @abstractmethod
    def accept(self, connectivity_visitor: ConnectivityVisitor) -> None:
        pass


class BT(Connectivity):
    def accept(self, connectivity_visitor: ConnectivityVisitor) -> None:
        print(self.__class__.__name__ + "->" + self.accept.__name__ + connectivity_visitor.__class__.__name__)

    def connect(self) -> None:
        pass

    def disconnect(self) -> None:
        pass

    def transmit(self, data: []) -> None:
        pass


class WiFi(Connectivity):
    def accept(self, connectivity_visitor: ConnectivityVisitor) -> None:
        print(self.__class__.__name__ + "->" + self.accept.__name__ + connectivity_visitor.__class__.__name__)
        connectivity_visitor.visit(self)

    def connect(self) -> None:
        pass

    def disconnect(self) -> None:
        pass

    def transmit(self, data: []) -> None:
        pass


class Zigbee(Connectivity):
    def accept(self, connectivity_visitor: ConnectivityVisitor) -> None:
        print(self.__class__.__name__ + "->" + self.accept.__name__ + connectivity_visitor.__class__.__name__)

    def connect(self) -> None:
        pass

    def disconnect(self) -> None:
        pass

    def transmit(self, data: []) -> None:
        pass


class ConnectivityVisitor(ABC):

    @abstractmethod
    def visit(self, bt: BT) -> None:
        pass

    @abstractmethod
    def visit(self, wifi: WiFi) -> None:
        pass

    @abstractmethod
    def visit(self, zigbee: Zigbee) -> None:
        pass


# sensor service sends data to AWS
class SensorConfig(ConnectivityVisitor):

    def visit(self, bt: BT) -> None:
        print(self.__class__.__name__ + "->" + self.visit.__name__ + ".bt")

    def visit(self, wifi: WiFi) -> None:
        print(self.__class__.__name__ + "->" + self.visit.__name__ + ".wifi")

    def visit(self, zigbee: Zigbee) -> None:
        print(self.__class__.__name__ + "->" + self.visit.__name__ + ".zigbee")


# gesture service sends data to Firebase
class GestureConfig(ConnectivityVisitor):

    def visit(self, bt: BT) -> None:
        print(self.__class__.__name__ + "->" + self.visit.__name__ + ".bt")

    def visit(self, wifi: WiFi) -> None:
        print(self.__class__.__name__ + "->" + self.visit.__name__ + ".wifi")

    def visit(self, zigbee: Zigbee) -> None:
        print(self.__class__.__name__ + "->" + self.visit.__name__ + ".zigbee")


# TODO: logic is properly implemented but need some correction in inheritance as
#  always last visit() of the config is taken. Just execute and check.
if __name__ == "__main__":
    SensorConfig().visit(WiFi())
    SensorConfig().visit(BT())
    SensorConfig().visit(Zigbee())

    GestureConfig().visit(WiFi())
    GestureConfig().visit(BT())
    GestureConfig().visit(Zigbee())
