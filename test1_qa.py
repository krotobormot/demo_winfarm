from selenium import webdriver
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# def test_open_page():
#     driver.get('https://openweathermap.org/')
#     driver.maximize_window()
#     assert 'openweathermap' in driver.current_url
#     print('browser.current_url')


def test_search_city_field():
    driver.get('https://openweathermap.org/')
    driver.maximize_window()
    search_city_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search city']")
    search_city_field.send_keys('New York')
    search_button = driver.find_element(By.CSS_SELECTOR,'button[class="button-round dark"]')
    time.sleep(5)
    search_button.click()
    time.sleep(5)
    search_option = driver.find_element(By.CSS_SELECTOR,'.search-dropdown-menu>li:nth-child(1)')
    time.sleep(5)
    search_option.click()
    expected_city = 'New York City, US'
    time.sleep(5)
    displayed_city = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="weather-widget"]/div[2]/div[1]/div[1]/div[1]/h2')))
    displayed_city_text = displayed_city.text
    print(displayed_city_text)
    assert expected_city == displayed_city_text
