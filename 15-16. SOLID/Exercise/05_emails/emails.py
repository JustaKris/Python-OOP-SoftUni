from abc import ABC, abstractmethod


class IEmail(ABC):

    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class IContent(ABC):

    def __init__(self, content):
        self.content = content

    @abstractmethod
    def format(self):
        pass


class MyContent(IContent):

    def format(self):
        return f'<myML>{self.content}</myML>'


class Email(IEmail):

    def __init__(self, protocol: str):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender: str):
        if self.protocol == 'IM':
            self.__sender = f"I'm {sender}"
        else:
            self.__sender = sender

    def set_receiver(self, receiver: str):
        if self.protocol == 'IM':
            self.__receiver = f"I'm {receiver}"
        else:
            self.__receiver = receiver

    def set_content(self, content: IContent):
        self.__content = content.format()

    def __repr__(self):
        return f"Sender: {self.__sender}\nReceiver: {self.__receiver}\nContent:\n{self.__content}"
