from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from ..db.base import Base

class Income(Base):
    __tablename__ = "incomes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    amount = Column(Float)
    source = Column(String)
    user_id = Column(Integer, index=True)

    user = relationship("User", back_populates="incomes")
