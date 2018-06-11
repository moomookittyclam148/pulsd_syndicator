from models import *
from datetime import timedelta
from sqlalchemy.exc import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

password = 'Pulsdpulsd1'

def syndicate():
    current_time = datetime.datetime.now()
    prev_time = current_time - timedelta(hours=1)

    events = event.query.filter(event.date_created.between(str(prev_time), str(current_time))).all()

    for event in events:
        add_event_eventbrite(event)
        add_event_yelp(event)
        add_event_eventcrazy(event)
        add_event_youreventfree(event)
        add_event_eventzilla(event)


start_date = datetime.datetime(2018,6,20,10,15)
end_date = datetime.datetime(2018,6,21,12,15)

new_event = event('Free Chicken', '1345 Amsterdam Ave', 'New York', 'NY', '10027',
                  'US', start_date, end_date, '',
                  'test', 'other', 'Free ticket')


def add_event_eventbrite(event):
    driver = webdriver.Chrome()
    driver.get("https://www.eventbrite.com/create")
    if driver.current_url != "https://www.eventbrite.com/create":
        driver.find_element_by_id('signin-email').send_keys('marodriguez148@gmail.com')
        driver.find_element_by_css_selector('.eds-btn.eds-btn--block').click()
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("//*[@id='password']").send_keys(password)
        element = driver.find_element_by_css_selector('.eds-btn.eds-btn--block')
        action = webdriver.ActionChains(driver)
        action.move_to_element(element).click().perform();

    event_address = event.address + ", " + event.city + ", " + event.state + " " + event.zip_code
    event_start_date = event.start_date.strftime("%m/%d/%Y")
    event_start_time = event.start_date.strftime("%H:%M")
    event_end_date = event.end_date.strftime("%m/%d/%Y")
    event_end_time = event.end_date.strftime("%H:%M")

    driver.find_element_by_id('id_group-details-name').send_keys(event.event_name)
    driver.find_element_by_id('location-name-input').send_keys(event_address)
    driver.find_element_by_id('location-name-input').send_keys(Keys.ENTER);
    driver.implicitly_wait(5)
    #driver.find_element_by_class_name('js-dtp-datepicker-input').click()
    driver.find_element_by_class_name('js-dtp-datepicker-input').clear()
    driver.find_element_by_class_name('js-dtp-datepicker-input').send_keys(event_start_date)
    driver.find_element_by_class_name('js-dtp-timepicker-input').clear()
    driver.find_element_by_class_name('js-dtp-timepicker-input').send_keys(event_start_time)
    driver.find_element_by_xpath('//*[@id="create-ticket-free-button"]').click()

    driver.find_element_by_id('create-ticket-free-button').click()
    driver.find_element_by_id('id_group-tickets-1-ticket_type').send_keys('RSVP')
    driver.find_element_by_id('id_group-tickets-1-quantity_total').send_keys('100')
    driver.find_element_by_xpath("//select[@id='id_group-privacy_and_promotion-event_format']/option[@value='100']").click()
    driver.find_element_by_xpath("//select[@id='id_group-privacy_and_promotion-event_category']/option[@value='199']").click()
    driver.find_element_by_xpath("//a[@id='make-event-live-button-almost-done']").click()
    driver.find_element_by_xpath('//*[@id="make-event-live-button-almost-done"]').click()


def add_event_test2(event):
    driver = webdriver.Chrome()
    driver.get("https://www.yelp.com/events/create")
    if driver.current_url != "https://www.yelp.com/events/create":
        driver.implicitly_wait(5)
        driver.find_element_by_xpath('//input[@id="email"]').send_keys('marodriguez148@gmail.com')
        driver.find_element_by_xpath('//input[@id="password"]').send_keys(password)
        driver.find_element_by_xpath('//*[@id="ajax-login"]/button').click()

def add_event_yelp(event):
    print('yelp')

def add_event_eventcrazy(event):
    print('eventcrazy')

def add_event_youreventfree(event):
    print('youreventfree')

def add_event_eventzilla(event):
    driver = webdriver.Chrome()
    driver.get("https://www.eventzilla.net/admin/eventadd")


    if driver.current_url != "https://www.eventzilla.net/admin/eventadd":
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//*[@id="ctl00_cph_newtheme_main_UserName"]').send_keys('marodriguez148@gmail.com')
        driver.find_element_by_xpath('//*[@id="ctl00_cph_newtheme_main_Password"]').send_keys(password)
        element = driver.find_element_by_xpath('//*[@id="ctl00_cph_newtheme_main_Login"]')
        driver.execute_script("arguments[0].click();", element)
        driver.implicitly_wait(10)
        element = driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_UC_CreateEvent_btnSave"]')
        driver.execute_script("arguments[0].click();", element)

    event_address = event.address + ", " + event.city + ", " + event.state + " " + event.zip_code
    event_start_date = event.start_date.strftime("%m/%d/%Y")
    event_start_time = event.start_date.strftime("%H:%M")
    event_end_date = event.end_date.strftime("%m/%d/%Y")
    event_end_time = event.end_date.strftime("%H:%M")

    driver.implicitly_wait(10)
    driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_UC_CreateEvent_txtEventTitle"]').send_keys(event.event_name)
    type_element = driver.find_element_by_xpath('//*[@id="s2id_autogen1"]')
    type_element.send_keys('Other Events')
    type_element.send_keys(Keys.ENTER)
    driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
    driver.find_element_by_xpath('//*[@id="tinymce"]').send_keys(event.event_desc)
    driver.switch_to.default_content()
    driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_UC_CreateEvent_txtStartDate"]').send_keys(event_start_date)
    driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_UC_CreateEvent_sel_StartTime"]').send_keys(event_start_time)
    driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_UC_CreateEvent_txtEndDate"]').send_keys(event_end_date)
    driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_UC_CreateEvent_sel_EndTime"]').send_keys(event_end_time)
    element = driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_UC_CreateEvent_btnSaveEvent"]')
    driver.execute_script("arguments[0].click();", element)
    #action = webdriver.ActionChains(driver)
    #action.click(element).perform();

    driver.find_element_by_id('ctl00_ContentPlaceHolder1_UC_EventTickets_lkAddCategory').click()
    driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_UC_EventTickets_txtCatTicketType"]').send_keys('RSVP')
    driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_UC_EventTickets_txtQuantity"]').send_keys('100')
    driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_UC_EventTickets_btnSave"]').click()
    driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_btnPublishEvent"]').click()
