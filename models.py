from sqlalchemy import Column, String, Integer
from database import Base

class URLMapping(Base):
    __tablename__ = "url_mapping"
    
    id = Column(Integer, primary_key=True, index=True)
    short_code = Column(String(10), unique=True, index=True, nullable=False)
    long_url = Column(String, unique=True, nullable=False)
