from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import asyncio
from starlette.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from swiggy_async import search_swiggy  # import your Swiggy scraper (async version)
from zomato_async import search_zomato  # import your Zomato scraper (async version)

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

class SearchRequest(BaseModel):
    location: str
    food_item: str

@app.post("/search")
async def search(request: Request, payload: SearchRequest):
    try:
        # Perform search for Swiggy and Zomato concurrently
        swiggy_results, zomato_results = await asyncio.gather(
            search_swiggy(payload.location, payload.food_item),
            search_zomato(payload.location, payload.food_item)
        )
        
        return JSONResponse(
            content={
                "swiggy_results": swiggy_results,
                "zomato_results": zomato_results
            },
            status_code=200
        )
    except Exception as e:
        return JSONResponse(
            content={"error": str(e)},
            status_code=500
        )
