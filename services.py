import random
import string
from sqlalchemy.orm import Session
from models import URLMapping

def generate_short_code(length=6):
    """Generate a random short code for URLs."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def get_or_create_short_url(db: Session, long_url: str):
    """Retrieve existing short URL or create a new one."""
    existing_entry = db.query(URLMapping).filter(URLMapping.long_url == long_url).first()
    if existing_entry:
        return existing_entry.short_code

    short_code = generate_short_code()
    new_entry = URLMapping(short_code=short_code, long_url=long_url)
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry.short_code

def get_long_url(db: Session, short_code: str):
    """Retrieve the original URL from the short code."""
    entry = db.query(URLMapping).filter(URLMapping.short_code == short_code).first()
    return entry.long_url if entry else None
