from Page.message import Message
from Page.new_messsage import NewMessage


class Page:
    def __init__(self,driver):
        self.driver = driver
    def get_message_page(self):
        return Message(self.driver)
    def get_new_message(self):
        return NewMessage(self.driver)
