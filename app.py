from fastapi import FastAPI, Query
from typing import List, Dict, Union
from swiggy import search_swiggy
from zomato import search_zomato

app = FastAPI(title="Food Aggregator API")

@app.get("/search")
def search(location: str = Query(...), food_item: str = Query(...)) -> Dict[str, Union[str, List[Dict]]]:
    """
    Aggregates food item results from Swiggy and Zomato.
    """
    try:
        swiggy_results = search_swiggy(location, food_item)
    except Exception as e:
        swiggy_results = f"Swiggy scraping error: {str(e)}"

    try:
        zomato_results = search_zomato(location, food_item)
    except Exception as e:
        zomato_results = f"Zomato scraping error: {str(e)}"

    return {
        "location": location,
        "food_item": food_item,
        "swiggy": swiggy_results,
        "zomato": zomato_results
    }
