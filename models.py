from sqlalchemy import Column, Integer, String, ARRAY, JSON
from sqlalchemy.ext.declarative import declarative_base
import json

Base = declarative_base()

# class Medicine(Base):
#     __tablename__ = "medicine"

#     id = Column(Integer, primary_key=True, index=True)
#     product_name = Column(String(50), unique=True, index=True, nullable=False)
#     manufacturer_name = Column(String(50), nullable=False)
#     product_category = Column(String(50), nullable=False)
#     additive = Column(JSON, default=json.dumps([]))
#     # additive = Column(ARRAY(String(50)), nullable=True)
#     manufacturing_importing = Column(String(50), nullable=False)
#     usage = Column(String(50), nullable=False)
#     capacity = Column(String(50), nullable=False)
#     caution = Column(String(1000), nullable=False)
#     effectiveness = Column(String(1000), nullable=False)

class Medicine(Base):
    __tablename__ = "medicine"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(50), nullable=False, index=True)
    manufacturer_name = Column(String(50), nullable=False)
    appearance = Column(String(50), nullable=False)
    length = Column(String(50), nullable=False)
    width = Column(String(50), nullable=False)
    thickness = Column(String(50), nullable=False)
    category_name = Column(String(50), nullable=False)
    specialized_general_name = Column(String(50), nullable=False)
    dosage_form_name = Column(String(50), nullable=False)
