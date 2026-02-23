from sqlalchemy import Column, Integer, String, Float
from database import Base

class InterviewResult(Base):
    __tablename__ = "results"

    id = Column(Integer, primary_key=True, index=True)
    role = Column(String)
    technical_score = Column(Float)
    communication_score = Column(Float)
    confidence_score = Column(Float)
    overall_score = Column(Float)
