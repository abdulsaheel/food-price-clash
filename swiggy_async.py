import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
import json

async def search_swiggy(location: str, food_item: str):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/123.0.0.0 Safari/537.36"
        )
        page = await context.new_page()

        # Set the location cookie before navigating
        location_cookie = {
            "name": "swgy_dweb_userLocation",
            "value": json.dumps({
                "lat": 19.5061743,
                "lng": 27.6480153,
                "area": "",
                "deliveryLocation": "",
                "address": location,
                "city": "",
                "mainText": ""
            }),
            "domain": ".swiggy.com",
            "path": "/"
        }
        await context.add_cookies([location_cookie])

        # Navigate to Swiggy's homepage
        await page.goto("https://www.swiggy.com/", wait_until="domcontentloaded")
        await asyncio.sleep(2)

        # Navigate to the search page
        try:
            await page.goto("https://www.swiggy.com/search", wait_until="domcontentloaded")
            await asyncio.sleep(2)
        except Exception as e:
            print(f"Error navigating to search page: {e}")
            await browser.close()
            return []

        # Enter the search term
        try:
            search_input = await page.wait_for_selector("input[placeholder='Search for restaurants and food']", timeout=5000)
            await search_input.fill(food_item)
            await asyncio.sleep(1)
            await page.keyboard.press("Enter")
            await asyncio.sleep(5)
        except Exception as e:
            print(f"Error performing search: {e}")
            await browser.close()
            return []

        # Scroll to load more results
        for _ in range(3):
            await page.mouse.wheel(0, 10000)
            await asyncio.sleep(2)

        # Parse the page content
        content = await page.content()
        soup = BeautifulSoup(content, "html.parser")

        results = []
        cards = soup.find_all("div", {"data-testid": "search-pl-dish-first-v2-card"})
        print(f"Found {len(cards)} dish cards on Swiggy")

        for card in cards:
            try:
                restaurant = card.find("div", class_="_1P-Lf")
                rating = card.find("span", class_="_30uSg")
                delivery_time = card.find("div", string=lambda text: "MINS" in text if text else False)
                dish_name = card.find("div", class_="sc-aXZVg eqSzsP")
                description = card.find("p", class_="_1QbUq")
                image = card.find("img", class_="_3XS7H")
                # Extract the restaurant link (href attribute)
                restaurant_url = "https://www.swiggy.com" + card.find("a", class_="_3VPpz")['href']
                # Extract prices
                prices = card.find_all("div", class_=["sc-aXZVg htLzaO", "sc-aXZVg chixpw"])
                if not prices:
                    continue
                if len(prices) == 2:
                    original_price = prices[0].get_text(strip=True)
                    discounted_price = prices[1].get_text(strip=True)
                else:
                    original_price = discounted_price = prices[0].get_text(strip=True)

                results.append({
                    "Restaurant": restaurant.get_text(strip=True) if restaurant else "N/A",
                    "Rating": rating.get_text(strip=True) if rating else "N/A",
                    "Delivery Time": delivery_time.get_text(strip=True) if delivery_time else "N/A",
                    "Dish": dish_name.get_text(strip=True) if dish_name else "N/A",
                    "Description": description.get_text(strip=True) if description else "N/A",
                    "Image URL": image['src'] if image else "N/A",
                    "Original Price": original_price,
                    "Discounted Price": discounted_price,
                    "Restaurant URL": restaurant_url
                })
            except Exception as e:
                print(f"Error parsing card: {e}")
                continue

        await browser.close()
        return results
