import pytest,sys,os
sys.path.append(os.getcwd())

from Base.Page import Page
from Base.until import get_android_driver


class TestMessage:
    def setup_class(self):
        self.driver = get_android_driver("com.android.mms", ".ui.ConversationList")
        self.page = Page(self.driver)

    def teardown_class(self):
        self.driver.quit()

    def test_01(self, phone=13012345678):
        self.page.get_message_page().click_new()
        self.page.get_new_message().input_mobile(phone)

    @pytest.mark.parametrize("text", ["python", "appium", "pytest"])
    def test_02(self, text):
        self.page.get_new_message().input_text(text)
        assert text in self.page.get_new_message().get_page_result()
