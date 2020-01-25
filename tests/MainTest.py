from pages.MainPage import MainPage
from BasicTest import BasicTest

from user.User import User

import time

import random

class MainTest(BasicTest):

    def setUp(self):
        super(MainTest, self).setUp()
        self.main_page = MainPage(self.driver)
        self.main_page.open()
        self.auth()
        self.main_page.hide_app_loader()

    def add_random_number(self, string):
        string += str(random.randrange(1, 1000000))
        return string

    def test_receive_new_letter(self):
        subject = self.add_random_number('Subject_receive_new_letter ')
        text = 'Text_receive_new_letter'
        letter_manager = self.main_page.letter_manager
        letter_manager.write_letter(self.login, subject, text)
        letter_manager.letter_selector.find_letter_subject_real(subject)

    def test_receive_new_letter_from_another_account(self):
        subject = self.add_random_number('Subj_receive_from_another_account ')
        text = 'Txt_receive_from_another_account'

        receiver = User(self.login2, self.password2)
        letter_manager = self.main_page.letter_manager
        letter_manager.write_letter(receiver.login, subject, text)
        self.main_page.relogin(receiver.login, receiver.password)

        letter_manager.letter_selector.find_letter_subject_real(subject)

    def test_reading_letter(self):
        subject = self.add_random_number('Subject_reading_letter ')
        text = 'Text_reading_letter'
        letter_manager = self.main_page.letter_manager
        letter_manager.write_letter(self.login, subject, text)
        letter_manager.letter_selector.set_letter_read_status(subject, True)
        self.assertTrue(letter_manager.letter_selector.get_letter_read_status(subject))

    def test_remove_letter(self):
        subject = self.add_random_number('Subject_remove_letter ')
        text = 'Text_remove_letter'
        letter_manager = self.main_page.letter_manager
        letter_manager.write_letter(self.login, subject, text)
        letter_manager.remove_letter(subject)

        self.main_page.navigation_manager.go_to_trash()
        letter_manager.letter_selector.find_letter_subject_real(subject)

    def test_restore_letter(self):
        subject = self.add_random_number('Subject_restore_letter ')
        text = 'Text_restore_letter'
        letter_manager = self.main_page.letter_manager
        letter_manager.write_letter(self.login, subject, text)
        letter_manager.remove_letter(subject)

        self.main_page.navigation_manager.go_to_trash()
        letter_manager.restore_letter(subject)
        # Go back (to check for a letter in the inbox folder)
        self.main_page.navigation_manager.go_to_inbox()

        letter_manager.letter_selector.find_letter_subject_real(subject)

    # def test_check_sent_new_letter(self):
    #     subject = 'Subject_check_sent_new_letter'
    #     text = 'Text_check_sent_new_letter'
    #     self.main_page.letter_manager.write_letter(self.login, subject, text)
    #     self.main_page.navigation_manager.go_to_sent_letters_folder()
    #     actual_subject = self.main_page.letter_manager.letter_selector.get_first_letter_subject()
    #     actual_text = self.main_page.letter_manager.letter_selector.get_first_letter_text()
    #     self.check_first_letter(subject, text)

    # def test_open_letter(self):
    #     subject = 'Subject_opened_letter'
    #     text = 'Text_opened_letter'
    #     self.main_page.letter_manager.write_letter(self.login, subject, text)
    #     self.main_page.letter_manager.letter_selector.open_first_letter()
    #     actual_subject = self.main_page.letter_manager.letter_selector.get_opened_letter_subject()
    #     actual_text = self.main_page.letter_manager.letter_selector.get_opened_letter_text()
    #     self.assertEqual(subject, actual_subject)
    #     self.assertEqual(text, actual_text)

    # def test_reply_letter(self):
    #     subject = 'Subject_reply_letter'
    #     text = 'Text_reply_letter'
    #     replied_text = 'Replied text'

    #     first_user = User(self.login, self.password)
    #     receiver = User(self.login2, self.password2)

    #     self.main_page.letter_manager.write_letter(
    #         receiver.login, subject, text)

    #     self.main_page.relogin(receiver.login, receiver.password)
    #     self.main_page.letter_manager.reply_letter(replied_text)

    #     self.main_page.relogin(first_user.login, first_user.password)
    #     self.main_page.letter_manager.letter_selector.open_first_letter()
    #     actual_replied_text = self.main_page.letter_manager.letter_selector.get_replied_letter_text()
    #     self.assertEqual(replied_text, actual_replied_text)

    # def test_write_many_receivers(self):
    #     subject = 'Subject_write_many_receivers'
    #     text = 'Text_write_many_receivers'
    #     receivers = [
    #         User(self.login, self.password),
    #         User(self.login2, self.password2),
    #     ]
    #     receivers_emails = [receiver.login for receiver in receivers]
    #     self.main_page.letter_manager.write_letter_many_receivers(
    #         receivers_emails, subject, text)
    #     for receiver in receivers:
    #         self.main_page.relogin(receiver.login, receiver.password)
    #         self.check_first_letter(subject, text)

    # def test_bold_letter(self):
    #     subject = 'Subject_bold_letter'
    #     text = 'Text_bold_letter'
    #     self.main_page.letter_manager.write_letter_without_sending(
    #         self.login, subject, text)
    #     self.main_page.letter_manager.letter_writer.set_bold_text()
    #     self.main_page.letter_manager.send_letter()
    #     self.main_page.letter_manager.letter_selector.open_first_letter()

    #     bold_element = self.main_page.letter_manager.letter_selector.get_bold()
    #     self.assertEqual(text, bold_element.text)

    # def test_font_title1_letter(self):
    #     subject = 'Subject_font_title1_letter_letter'
    #     text = 'font title1 letter'
    #     self.main_page.letter_manager.write_letter_without_sending(
    #         self.login, subject, text)
    #     self.main_page.letter_manager.letter_writer.set_font_text_title1()

    #     self.main_page.letter_manager.send_letter()
    #     self.main_page.letter_manager.letter_selector.open_first_letter()
    #     element = self.main_page.letter_manager.letter_selector.get_font_text_title1()
    #     self.assertEqual(text, element.text)

    # def test_alignment_text_center(self):
    #     subject = 'Subject_alignment_text_center'
    #     text = 'alignment_text_center'
    #     self.main_page.letter_manager.write_letter_without_sending(
    #         self.login, subject, text)
    #     self.main_page.letter_manager.letter_writer.set_alignment_text_center()

    #     self.main_page.letter_manager.send_letter()
    #     self.main_page.letter_manager.letter_selector.open_first_letter()
    #     element = self.main_page.letter_manager.letter_selector.get_alignment_text_center()
    #     self.assertEqual(text, element.text)

    # def test_indent_text_plus(self):
    #     subject = 'Subject_alignment_text_center'
    #     text = 'alignment_text_indent_text_plus'
    #     self.main_page.letter_manager.write_letter_without_sending(
    #         self.login, subject, text)
    #     self.main_page.letter_manager.letter_writer.set_indent_text_plus()

    #     self.main_page.letter_manager.send_letter()
    #     self.main_page.letter_manager.letter_selector.open_first_letter()
    #     element = self.main_page.letter_manager.letter_selector.get_indent_text()
    #     self.assertEqual(text, element.text)

    # def test_indent_text_minus(self):
    #     subject = 'Subject_alignment_indent_text_minus'
    #     text = 'alignment_text_indent_text_minus'
    #     self.main_page.letter_manager.write_letter_without_sending(
    #         self.login, subject, text)
    #     self.main_page.letter_manager.letter_writer.set_indent_text_minus()

    #     self.main_page.letter_manager.send_letter()
    #     self.main_page.letter_manager.letter_selector.open_first_letter()
    #     element = self.main_page.letter_manager.letter_selector.get_indent_text()
    #     self.assertEqual(text, element.text)

    # def test_italic_letter(self):
    #     subject = 'Subject_italic_letter'
    #     text = 'Text_italic_letter'
    #     self.main_page.letter_manager.write_letter_without_sending(
    #         self.login, subject, text)
    #     self.main_page.letter_manager.letter_writer.set_italic_text()
    #     self.main_page.letter_manager.send_letter()
    #     self.main_page.letter_manager.letter_selector.open_first_letter()

    #     italic_element = self.main_page.letter_manager.letter_selector.get_italic()
    #     self.assertEqual(text, italic_element.text)

    # def test_underline_letter(self):
    #     subject = 'Subject_underline_letter'
    #     text = 'Text_underline_letter'
    #     self.main_page.letter_manager.write_letter_without_sending(
    #         self.login, subject, text)
    #     self.main_page.letter_manager.letter_writer.set_underline_text()
    #     self.main_page.letter_manager.send_letter()
    #     self.main_page.letter_manager.letter_selector.open_first_letter()

    #     underline_element = self.main_page.letter_manager.letter_selector.get_underline()
    #     self.assertEqual(text, underline_element.text)

    # def test_strike_through_letter(self):
    #     subject = 'Subject_strike_through_letter'
    #     text = 'Text_strike_through_letter'
    #     self.main_page.letter_manager.write_letter_without_sending(
    #         self.login, subject, text)
    #     self.main_page.letter_manager.letter_writer.set_strike_through_text()
    #     self.main_page.letter_manager.send_letter()
    #     self.main_page.letter_manager.letter_selector.open_first_letter()

    #     strike_through_element = self.main_page.letter_manager.letter_selector.get_strike_through()
    #     self.assertEqual(text, strike_through_element.text)

    # def test_text_color(self):
    #     subject = 'Subject_text_color'
    #     text = 'Text_color'
    #     self.main_page.letter_manager.write_letter_without_sending(
    #         self.login, subject, text)
    #     self.main_page.letter_manager.letter_writer.set_text_color_purple()
    #     self.main_page.letter_manager.send_letter()
    #     self.main_page.letter_manager.letter_selector.open_first_letter()
    #     element = self.main_page.letter_manager.letter_selector.get_text_color_purple()
    #     self.assertEqual(text, element.text)
    #     style = 'color: rgb(231, 0, 145);'
    #     self.assertEqual(style, element.get_attribute(
    #         'style').encode('utf-8', errors='ignore'))

    # def test_background_color(self):
    #     subject = 'Subject_background_color'
    #     text = 'Background_color'
    #     self.main_page.letter_manager.write_letter_without_sending(
    #         self.login, subject, text)
    #     self.main_page.letter_manager.letter_writer.set_background_color_blue()
    #     self.main_page.letter_manager.send_letter()
    #     self.main_page.letter_manager.letter_selector.open_first_letter()
    #     element = self.main_page.letter_manager.letter_selector.get_background_color_blue()
    #     self.assertEqual(text, element.text)
    #     style = 'background-color: rgb(110, 228, 254);'
    #     self.assertEqual(style, element.get_attribute(
    #         'style').encode('utf-8', errors='ignore'))

    # def test_back_formating(self):
    #     subject = 'Subject preview letter'
    #     text = 'Teeeeext'
    #     self.main_page.letter_manager.write_letter_without_sending(
    #         self.login, subject, text)
    #     self.main_page.letter_manager.letter_writer.set_bold_text()

    #     bold_text = self.main_page.letter_manager.letter_selector.get_bold_text()

    #     self.main_page.letter_manager.letter_writer.click_preview_button()

    #     not_bold_text = self.main_page.letter_manager.letter_selector.get_not_bold_text()
    #     self.assertEqual(text, bold_text)
    #     self.assertEqual(text, not_bold_text)

    # def test_clear_formating(self):
    #     subject = 'Subject letter'
    #     text = 'All_kind_formating'
    #     self.main_page.letter_manager.write_letter_without_sending(
    #         self.login, subject, text)
    #     self.main_page.letter_manager.letter_writer.set_italic_text()
    #     self.main_page.letter_manager.letter_writer.set_underline_text()
    #     self.main_page.letter_manager.letter_writer.set_bold_text()
    #     self.main_page.letter_manager.letter_writer.set_strike_through_text()

    #     self.main_page.letter_manager.letter_writer.click_clear_all_button()
    #     unformating_text = self.main_page.letter_manager.letter_selector.get_unformating_text()
    #     self.assertEqual(text, unformating_text)

    # def test_insert_link(self):
    #     subject = "Hello"
    #     text = 'Welcome to the 4th semester of Tehnopark MailRu\n'
    #     self.main_page.letter_manager.write_letter_without_sending(
    #         self.login, subject, text)
    #     self.main_page.letter_manager.letter_writer.click_link_button()
    #     txt_link = self.main_page.letter_manager.letter_writer.text_link
    #     link = self.main_page.letter_manager.letter_writer.link
    #     self.main_page.letter_manager.letter_writer.enter_link(link)
    #     self.main_page.letter_manager.letter_writer.enter_text_link(txt_link)
    #     self.main_page.letter_manager.letter_writer.click_confirm_link()

    #     actual_text = self.main_page.letter_manager.letter_selector.get_link_text()
    #     self.assertEqual(txt_link, actual_text)
    
    # def test_1(self):
    #     letters = self.main_page.letter_manager.letter_selector.get_all_letters()
    #     texts = [letter.text for letter in letters]
    #     # print(texts[0])
    #     for text in texts:
    #         print(text)
    #         print('-------')
    #     print(len(letters))
