"""
    封装所有元素定位信息
"""
from selenium.webdriver.common.by import By


class PageElements:
    """短信 页面"""
    # 新建短信
    message_new_btn_id = (By.ID, "com.android.mms:id/action_compose_new")
    """新建短信页面"""
    # 接收人手机号
    new_mess_mobile_id = (By.ID, "com.android.mms:id/recipients_editor")
    # 短信内容
    new_mess_text_id = (By.ID, "com.android.mms:id/embedded_text_editor")
    # 发送按钮
    new_mess_send_btn_id = (By.ID, "com.android.mms:id/send_button_sms")
    # 获取当前页面的所有信息
    new_page_result_id = (By.ID, "com.android.mms:id/text_view")
