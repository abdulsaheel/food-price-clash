from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import asyncio
from starlette.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from swiggy_async import search_swiggy  # import your Swiggy scraper (async version)
from zomato_async import search_zomato  # import your Zomato scraper (async version)
from pincode_mapping import get_city_from_pincode, validate_pincode, get_nearby_cities

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Setup Jinja2 for HTML templates
templates = Jinja2Templates(directory="templates")

# Serve static files (like Tailwind CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/validate-pincode/{pincode}")
async def validate_pincode_endpoint(pincode: str):
    """
    Validate a pincode and return the corresponding city.
    """
    if not validate_pincode(pincode):
        return JSONResponse(
            content={"valid": False, "error": "Invalid pincode format"},
            status_code=400
        )
    
    city = get_city_from_pincode(pincode)
    if city:
        nearby_cities = get_nearby_cities(pincode, radius=3)
        return JSONResponse(
            content={
                "valid": True, 
                "city": city, 
                "nearby_cities": nearby_cities,
                "message": f"We deliver to {city}"
            },
            status_code=200
        )
    else:
        return JSONResponse(
            content={
                "valid": False, 
                "error": f"Sorry, we don't serve pincode {pincode} yet"
            },
            status_code=404
        )

class SearchRequest(BaseModel):
    pincode: str
    food_item: str

@app.post("/search")
async def search(request: Request, payload: SearchRequest):
    try:
        # Validate pincode format
        if not validate_pincode(payload.pincode):
            return JSONResponse(
                content={"error": "Invalid pincode format. Please enter a 6-digit pincode."},
                status_code=400
            )
        
        # Get city from pincode
        primary_city = get_city_from_pincode(payload.pincode)
        if not primary_city:
            return JSONResponse(
                content={"error": f"Sorry, we don't serve in pincode {payload.pincode} yet. Please try a different pincode."},
                status_code=404
            )
        
        # Get nearby cities as fallback
        nearby_cities = get_nearby_cities(payload.pincode, radius=5)
        
        # Perform search for Swiggy and Zomato concurrently for primary city
        swiggy_results, zomato_results = await asyncio.gather(
            search_swiggy(primary_city, payload.food_item),
            search_zomato(primary_city, payload.food_item)
        )
        
        return JSONResponse(
            content={
                "pincode": payload.pincode,
                "primary_city": primary_city,
                "nearby_cities": nearby_cities,
                "swiggy_results": swiggy_results,
                "zomato_results": zomato_results,
                "message": f"Found restaurants nearest to pincode {payload.pincode} in {primary_city}"
            },
            status_code=200
        )
    except Exception as e:
        return JSONResponse(
            content={"error": str(e)},
            status_code=500
        )
