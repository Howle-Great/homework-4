# -*- coding: utf-8 -*-
from tests.pages.BasicPage import BasicPage
from selenium.webdriver import ActionChains

class LetterSelector(BasicPage):
  first_letter = '.llc:first-of-type > .llc__container'
  first_letter_subject = 'a.llc:first-of-type > .llc__container .llc__subject'
  first_letter_text = 'a.llc:first-of-type > .llc__container .llc__snippet'
  first_letter_read_status = 'a.llc:first-of-type .ll-rs'
  first_letter_avatar = '.llc:first-of-type button.ll-av'
  
  all_letters = 'div.portal-menu-element_select'
  
  dataset_empty = '.dataset__empty'
  
  def get_first_letter_subject(self):
    subject = self.wait_render(self.first_letter_subject)
    return subject.text
  
  def get_first_letter_text(self):
    content = self.wait_render(self.first_letter_text).text
    # We should obtain only the content we written (not sign)
    text = content.split(' -- ')[0]
    return text
    
  def select_first_letter(self):
    elem = self.wait_render(self.first_letter_avatar)
    ActionChains(self.driver).move_to_element(elem).click(elem).perform()
    
  def get_first_letter_read_status(self):
    elem = self.wait_render(self.first_letter_read_status)
    if elem.get_attribute('title') == (u'Пометить прочитанным') or elem.get_attribute('data-title') == (u'Пометить прочитанным'):
      return False
    else:
      return True
    
  def set_first_letter_read_status(self, status):
    elem = self.wait_render(self.first_letter_read_status)
    # Invert status only it's needed
    if self.get_first_letter_read_status() != status:
      elem.click()
    
  def select_all_letters(self):
    elem = self.wait_render(self.all_letters)
    elem.click()
    
  def click_letter(self):
    elem = self.wait_render(self.first_letter)
    elem.click()
    
  def is_there_no_letters(self):
    self.wait_render(self.dataset_empty)