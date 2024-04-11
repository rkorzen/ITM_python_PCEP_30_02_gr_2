from abc import ABC, abstractmethod


class Sender(ABC):

    @abstractmethod
    def send(self):
        ...


class MailSender(Sender):

    def send(self):
        print("Wysyłam emaila")


p = MailSender()

def obsluga(xxx: Sender):
    xxx.send()

