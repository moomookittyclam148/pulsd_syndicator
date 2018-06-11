from models import *
from datetime import timedelta, datetime
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


start_date = datetime(2018,6,20,10,15)
end_date = datetime(2018,6,20,12,15)

new_event = event('Free Chicken', '1345 Amsterdam Ave', 'New York', 'NY', '10027',
                  'US', start_date, end_date, '',
                  'test', 'other', 'Free ticket')


def add_event_test(event):
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
    driver.find_element_by_xpath('').clear()
    driver.find_element_by_xpath('//div[@class="js-dtp-enddatetimepicker"]//input[@class="js-dtp-datepicker-input"]').send_keys(event_end_date)
    driver.find_element_by_class_name('js-dtp-timepicker-input').clear()
    driver.find_element_by_class_name('js-dtp-timepicker-input').send_keys(event_end_date)
    driver.find_element_by_id('id_group-details-description').clear()
    driver.find_element_by_id('id_group-details-description').send_keys(event.event_desc)
    driver.find_element_by_id('id_group-organizer-organizers-0-organization_name').send_keys('Pulsd')

    driver.find_element_by_id('create-ticket-free-button').click()
    driver.find_element_by_id('id_group-tickets-1-ticket_type').send_keys('RSVP')
    driver.find_element_by_id('id_group-tickets-1-quantity_total').send_keys('100')
    driver.find_element_by_xpath("//select[@id='id_group-privacy_and_promotion-event_format']/option[@value='100']").click()
    driver.find_element_by_xpath("//select[@id='id_group-privacy_and_promotion-event_category']/option[@value='199']").click()
    driver.find_element_by_xpath("//a[@id='make-event-live-button-almost-done']").click()


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

def add_event_eventbrite(event):
    print('eventbrite')

def add_event_eventcrazy(event):
    print('eventcrazy')

def add_event_youreventfree(event):
    print('youreventfree')

def add_event_eventzilla(event):
    print('eventzilla')
