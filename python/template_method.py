from abc import ABC, abstractmethod
from typing import final

"""
Template Method pattern a good way to define algorithm steps, define common methods,
declare abstract methods and define API for calling the algorithm.
So, ultimately Template implements the algorithm and keep it open for extension but at
the same time it does keep close for modification (algorithm steps can't be changed here).
"""


class SDKTestTemplate:

    @final
    def connect(self):
        print("TODO: Connection logic")

    @final
    def disconnect(self):
        print("TODO: Disconnect logic")

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def post(self):
        pass

    @abstractmethod
    def put(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @final
    def api_test(self):
        self.connect()
        self.get()
        self.post()
        self.put()
        self.delete()
        self.disconnect()


class GoogleSDKTest(SDKTestTemplate):
    def get(self):
        print("TODO: " + self.__class__.__name__ + " -> " + self.__class__.get.__name__)

    def post(self):
        print("TODO: " + self.__class__.__name__ + " -> " + self.__class__.post.__name__)

    def put(self):
        print("TODO: " + self.__class__.__name__ + " -> " + self.__class__.put.__name__)

    def delete(self):
        print("TODO: " + self.__class__.__name__ + " -> " + self.__class__.delete.__name__)


class AwsSDKTest(SDKTestTemplate):
    def get(self):
        print("TODO: " + self.__class__.__name__ + " -> " + self.__class__.get.__name__)

    def post(self):
        print("TODO: " + self.__class__.__name__ + " -> " + self.__class__.post.__name__)

    def put(self):
        print("TODO: " + self.__class__.__name__ + " -> " + self.__class__.put.__name__)

    def delete(self):
        print("TODO: " + self.__class__.__name__ + " -> " + self.__class__.delete.__name__)


if __name__ == "__main__":
    googleSdk = GoogleSDKTest()
    awsSdk = AwsSDKTest()

    googleSdk.api_test()
    awsSdk.api_test()
