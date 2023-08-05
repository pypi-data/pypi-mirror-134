import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float
from pagexdata.database import Base
from pydantic import BaseModel


class RedditHits(Base):
    __tablename__ = 'reddit_hits'

    date = Column(DateTime, primary_key=True)
    ticker_symbol = Column(String, primary_key=True)
    subreddit = Column(String, primary_key=True)
    hits = Column(Integer)
    positive_hits = Column(Boolean)
    rank = Column(Integer, nullable=True)
    previous_rank = Column(Integer, nullable=True)
    change_rank = Column(Integer, nullable=True)
    change_hits_one_day = Column(Integer, nullable=True)
    change_hits_two_days = Column(Integer, nullable=True)
    change_hits_three_days = Column(Integer, nullable=True)
    change_hits_one_week = Column(Integer, nullable=True)
    change_hits_two_weeks = Column(Integer, nullable=True)
    change_hits_four_weeks = Column(Integer, nullable=True)
    hits_volatility_one_week = Column(Float, nullable=True)
    hits_volatility_two_weeks = Column(Float, nullable=True)


class StockData(Base):
    __tablename__ = 'stockdata'

    date = Column(DateTime, primary_key=True)
    ticker_symbol = Column(String, primary_key=True)
    price = Column(Float)
    volume = Column(Integer)


class ImportLog(Base):
    __tablename__ = 'importlog'

    date = Column(DateTime, primary_key=True)
    type = Column(String, primary_key=True)
    state = Column(String)
    message = Column(String, nullable=True)
    extra = Column(String, nullable=True)


# pagination entities for rest api
class RedditHitsPage(BaseModel):
    date: datetime.datetime
    ticker_symbol: str
    subreddit: str
    hits: int
    rank: int
    previous_rank: int
    change_rank: int
    change_hits_one_day: int
    change_hits_two_days: int
    change_hits_three_days: int
    change_hits_one_week: int
    change_hits_two_weeks: int
    change_hits_four_weeks: int
    hits_volatility_one_week: float
    hits_volatility_two_weeks: float

    class Config:
        orm_mode = True


class StockDataPage(BaseModel):
    date: datetime.datetime
    ticker_symbol: str
    price: float
    volume: int

    class Config:
        orm_mode = True


class ImportLogPage(BaseModel):
    date: datetime.datetime
    type: str
    state: str
    message: str
    extra: str

    class Config:
        orm_mode = True
