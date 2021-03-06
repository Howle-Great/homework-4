
from LetterWriter import LetterWriter
from LetterSelector import LetterSelector
from LetterReplier import LetterReplier
from tests.pages.main_page.notifications.NotificationManager import NotificationManager
from tests.pages.main_page.menu.top_menu.TopMenuManager import TopMenuManager
from tests.pages.main_page.confirmationers.RemoveConfirmationer import RemoveConfirmationer
from selenium.webdriver import ActionChains


class LetterManager():

    def __init__(self, driver):
        self.driver = driver
        self.letter_writer = LetterWriter(self.driver)
        self.letter_selector = LetterSelector(self.driver)
        self.letter_replier = LetterReplier(self.driver)
        self.notification_manager = NotificationManager(self.driver)
        self.top_menu_manager = TopMenuManager(self.driver)
        self.remove_confirmationer = RemoveConfirmationer(self.driver)

    def write_letter(self, email, subject, text):
        self.letter_writer.click_write_letter_button()
        self.letter_writer.enter_email_receiver(email)
        self.letter_writer.enter_subject(subject)
        self.letter_writer.enter_textbox(text)
        self.letter_writer.click_send_letter_button()
        self.letter_writer.close_sent_window()

    def write_letter_many_receivers(self, receivers, subject, text):
        self.letter_writer.click_write_letter_button()
        for receiver in receivers:
            self.letter_writer.enter_email_receiver(receiver)
        self.letter_writer.enter_subject(subject)
        self.letter_writer.enter_textbox(text)
        self.letter_writer.click_send_letter_button()
        self.letter_writer.close_sent_window()

    def reply_letter(self, subject, text):
        self.letter_selector.open_letter(subject)
        self.letter_replier.click_reply_button()
        self.letter_writer.enter_textbox(text)
        self.letter_writer.click_send_letter_button()
        self.letter_writer.close_sent_window()

    def remove_letter(self, subject):
        self.letter_selector.select_letter(subject)
        self.top_menu_manager.remove_letter_from_menu()
        self.notification_manager.hide_notification()

    # Call only while in the recycle bin
    def restore_letter(self, subject):
        self.letter_selector.select_letter(subject)
        self.top_menu_manager.click_top_menu_move_letter_button()
        self.top_menu_manager.click_inbox_menu_item()
        self.notification_manager.hide_notification()

    def write_letter_without_sending(self, email, subject, text):
        self.letter_writer.click_write_letter_button()
        self.letter_writer.enter_email_receiver(email)
        self.letter_writer.enter_subject(subject)
        self.letter_writer.enter_textbox(text)

    def send_letter(self):
        self.letter_writer.click_send_letter_button()
        self.letter_writer.close_sent_window()

    