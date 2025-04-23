from playwright.async_api import async_playwright
import asyncio

async def search_zomato(location: str, food_item: str):
    location = location.lower().replace(" ", "-")
    food_item = food_item.lower().replace(" ", "-")
    url = f"https://www.zomato.com/{location}/delivery/dish-{food_item}"

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=50)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
            locale="en-US"
        )
        page = await context.new_page()

        try:
            await page.goto(url, wait_until="domcontentloaded")
        except Exception as e:
            print("Error during page.goto():", str(e))
            await browser.close()
            return []

        await page.wait_for_timeout(3000)

        # Scroll to load more results
        for _ in range(3):
            await page.mouse.wheel(0, 10000)
            await asyncio.sleep(2)

        content = await page.content()
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(content, "html.parser")

        restaurants = []
        cards = soup.find_all("div", class_="sc-1mo3ldo-0")
        print(f"Found {len(cards)} restaurant cards on Zomato")

        for card in cards:
            try:
                name = card.find("h4", class_="sc-1hp8d8a-0")
                cuisine = card.find("p", class_="sc-gggouf")
                price = card.find("p", class_="KXcjT")
                rating = card.find("div", class_="sc-1q7bklc-1")
                delivery_time = card.find("div", class_="min-basic-info-right")
                offer = card.find("p", class_="sc-eTyWNx")
                img = card.find("img", class_="fyZwWD")
                link = card.find("a", class_="sc-hPeUyl")

                restaurants.append({
                    "Name": name.text.strip() if name else "N/A",
                    "Cuisine": cuisine.text.strip() if cuisine else "N/A",
                    "Price": price.text.strip() if price else "N/A",
                    "Rating": rating.text.strip() if rating else "N/A",
                    "Delivery Time": delivery_time.find("p").text.strip() if delivery_time else "N/A",
                    "Offer": offer.text.strip() if offer else "No offer",
                    "Image URL": img['src'] if img else "N/A",
                    "Restaurant URL": "https://www.zomato.com" + link['href'] if link else "N/A"
                })

            except Exception as e:
                print(f"Error parsing card: {e}")
                continue

        await browser.close()
        return restaurants
