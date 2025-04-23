from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
from bs4 import BeautifulSoup

def search_zomato(location: str, food_item: str):
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    # chrome_options.add_argument("--headless")  # Optional for FastAPI
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    try:
        # Prepare the URL
        food_item_url = food_item.replace(" ", "-").lower()
        location_url = location.lower()
        url = f"https://www.zomato.com/{location_url}/delivery/dish-{food_item_url}"

        driver.get(url)
        time.sleep(5)

        for _ in range(3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        restaurant_cards = soup.find_all('div', {'class': 'sc-1mo3ldo-0'})
        print(restaurant_cards)
        restaurants = []
        for card in restaurant_cards:
            try:
                name = card.find('h4', {'class': 'sc-1hp8d8a-0'})
                name = name.text.strip() if name else "N/A"

                cuisine = card.find('p', {'class': 'sc-gggouf'})
                cuisine = cuisine.text.strip() if cuisine else "N/A"

                price = card.find('p', {'class': 'KXcjT'})
                price = price.text.strip() if price else "N/A"

                rating_div = card.find('div', {'class': 'sc-1q7bklc-1'})
                rating = rating_div.text.strip() if rating_div else "N/A"

                delivery_time = card.find('div', {'class': 'min-basic-info-right'})
                delivery_time = delivery_time.find('p').text.strip() if delivery_time else "N/A"

                offer = card.find('p', {'class': 'sc-eTyWNx'})
                offer = offer.text.strip() if offer else "No offer"

                img = card.find('img', {'class': 'fyZwWD'})
                img_url = img['src'] if img else "N/A"

                link = card.find('a', {'class': 'sc-hPeUyl'})
                restaurant_url = "https://www.zomato.com" + link['href'] if link else "N/A"

                restaurants.append({
                    'name': name,
                    'cuisine': cuisine,
                    'price': price,
                    'rating': rating,
                    'delivery_time': delivery_time,
                    'offer': offer,
                    'image_url': img_url,
                    'restaurant_url': restaurant_url
                })
            except Exception:
                continue

        return restaurants
    finally:
        driver.quit()
