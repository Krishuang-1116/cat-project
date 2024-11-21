'''
Notification class for sending notifications to the owner. 
Currently no use of this class in V0 and V1.
'''

from abc import ABC, abstractmethod


class BaseNotification(ABC):

    def __init__(self) -> None:
        pass

    def set_message(self, message):
        pass

    def get_messages(self):
        pass

    @abstractmethod
    def send_notification(self):
        pass

    @abstractmethod
    def clear_notifications(self):
        pass


class PushNotification(BaseNotification):
    '''
    Notification subclass and takes the form of push. 
    '''

    def __init__(self, owner):
        self.owner = owner
        self.messages = []

    def set_message(self, message):
        '''
        Essentially the bridge between HealthCheck class and Notification class
        '''
        self.messages.append(message)

    def get_messages(self):
        return "\n".join(self.messages)

    def send_notification(self):
        self.send_push_notification()

    def send_push_notification(self):

        print(
            f"Sending notification to {self.owner} with message {self.messages}")

    def clear_notifications(self):
        self.messages = []
