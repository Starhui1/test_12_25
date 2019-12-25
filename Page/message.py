from Base.base import Base
from Page.Page_elements import PageElements


class Message(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)
    def click_new(self):
        """点击新建按钮"""
        self.click_ele(PageElements.message_new_btn_id)