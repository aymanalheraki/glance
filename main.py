from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
import validators

from database import get_db, Base, engine
from models import URLMapping
from schemas import URLCreate, URLResponse
from services import get_or_create_short_url, get_long_url

# Initialize app and database
app = FastAPI()
Base.metadata.create_all(bind=engine)

BASE_URL = "http://short.ner/"

@app.post("/shorten", response_model=URLResponse)
def shorten_url(url_data: URLCreate, db: Session = Depends(get_db)):
    if not validators.url(str(url_data.long_url)):
        raise HTTPException(status_code=400, detail="Invalid URL")
    
    short_code = get_or_create_short_url(db, str(url_data.long_url))
    return {"short_url": f"{BASE_URL}{short_code}"}

@app.get("/{short_code}")
def redirect_url(short_code: str, db: Session = Depends(get_db)):
    long_url = get_long_url(db, short_code)
    if not long_url:
        raise HTTPException(status_code=404, detail="Short URL not found")
    
    return RedirectResponse(url=long_url, status_code=302)
