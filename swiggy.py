from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json

def search_swiggy(location: str, food_item: str):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--headless")  # Optional for FastAPI deployment
    driver = webdriver.Chrome(options=options)

    try:
        # First load the site to set cookies
        driver.get("https://www.swiggy.com/")
        
        # Create location cookie data
        location_data = {
            "lat": 19.5061743,
            "lng": 27.6480153,
            "area": "",
            "deliveryLocation": "",
            "address": location,
            "city": "",
            "mainText": ""
        }
        
        # Set the location cookie
        location_cookie = {
            'name': 'swgy_dweb_userLocation',
            'value': json.dumps(location_data),
            'domain': '.swiggy.com',
            'path': '/'
        }
        driver.add_cookie(location_cookie)
        
        # Refresh the page to apply cookie
        driver.refresh()
        time.sleep(2)

        # Go to search page
        driver.get("https://www.swiggy.com/search")
        time.sleep(5)

        # Enter search term
        search_box = driver.find_element(By.CSS_SELECTOR, 'input.ssM7E')
        search_box.send_keys(food_item)
        time.sleep(1)
        search_box.send_keys(Keys.ENTER)
        time.sleep(6)

        # Get all results
        dish_cards = driver.find_elements(By.CSS_SELECTOR, 'div[data-testid="search-pl-dish-first-v2-card"]')

        results = []
        for card in dish_cards:
            try:
                restaurant = card.find_element(By.CSS_SELECTOR, 'div._1P-Lf').text.strip()
                rating = card.find_element(By.CSS_SELECTOR, 'span._30uSg').text.strip()
                delivery_time = card.find_element(By.XPATH, './/div[contains(text(),"MINS")]').text.strip()
                dish_name = card.find_element(By.CSS_SELECTOR, 'div.sc-aXZVg.eqSzsP').text.strip()
                description = card.find_element(By.CSS_SELECTOR, 'p._1QbUq').text.strip()
                image_url = card.find_element(By.CSS_SELECTOR, 'img._3XS7H').get_attribute('src')

                prices = card.find_elements(By.CSS_SELECTOR, 'div.sc-aXZVg.htLzaO, div.sc-aXZVg.chixpw')
                if not prices:
                    continue
                if len(prices) == 2:
                    original_price = prices[0].text.strip()
                    discounted_price = prices[1].text.strip()
                else:
                    original_price = discounted_price = prices[0].text.strip()

                results.append({
                    "restaurant": restaurant,
                    "rating": rating,
                    "delivery_time": delivery_time,
                    "dish_name": dish_name,
                    "description": description,
                    "original_price": original_price,
                    "discounted_price": discounted_price,
                    "image_url": image_url
                })
            except Exception:
                continue

        return results
    finally:
        driver.quit()
