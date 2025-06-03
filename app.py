from fastapi import FastAPI, Query
from typing import List, Dict, Union
from swiggy import search_swiggy
from zomato import search_zomato
from pincode_mapping import get_city_from_pincode, validate_pincode

app = FastAPI(title="Food Aggregator API")

@app.get("/search")
def search(pincode: str = Query(...), food_item: str = Query(...)) -> Dict[str, Union[str, List[Dict]]]:
    """
    Aggregates food item results from Swiggy and Zomato based on pincode.
    """
    # Validate pincode format
    if not validate_pincode(pincode):
        return {
            "error": "Invalid pincode format. Please enter a 6-digit pincode.",
            "pincode": pincode,
            "food_item": food_item
        }
    
    # Get city from pincode
    location = get_city_from_pincode(pincode)
    if not location:
        return {
            "error": f"Sorry, we don't serve in pincode {pincode} yet. Please try a different pincode.",
            "pincode": pincode,
            "food_item": food_item
        }
    
    try:
        swiggy_results = search_swiggy(location, food_item)
    except Exception as e:
        swiggy_results = f"Swiggy scraping error: {str(e)}"

    try:
        zomato_results = search_zomato(location, food_item)
    except Exception as e:
        zomato_results = f"Zomato scraping error: {str(e)}"

    return {
        "pincode": pincode,
        "location": location,
        "food_item": food_item,
        "swiggy": swiggy_results,
        "zomato": zomato_results,
        "message": f"Found restaurants nearest to pincode {pincode} in {location}"
    }
