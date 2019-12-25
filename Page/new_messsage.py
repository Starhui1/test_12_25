from Base.base import Base
from Page.Page_elements import PageElements


class NewMessage(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def input_mobile(self, phone):
        """输入收件人手机号"""
        self.send_ele(PageElements.new_mess_mobile_id, phone)

    def input_text(self, text):
        """输入短信内容"""
        self.send_ele(PageElements.new_mess_text_id, text)
        self.click_ele(PageElements.new_mess_send_btn_id)

    def get_page_result(self):
        """获取短信内容断言"""
        return [i.text for i in self.find_eles(PageElements.new_page_result_id)]
