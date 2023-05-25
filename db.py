from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Medicine, Base
import json

# MySQL 연결 정보
DATABASE_URL = "mysql+pymysql://myuser:mypassword@localhost/medicine"

# MySQL 연결 엔진 생성
engine = create_engine(DATABASE_URL)

# MySQL 연결 세션 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 데이터베이스 테이블 생성
Base.metadata.create_all(bind=engine)

from typing import List
import xml.etree.ElementTree as ET
import pandas as pd
from sqlalchemy.exc import SQLAlchemyError
import time

def insert_data_to_mysql(data):
    db = SessionLocal()

    try:
        # Medicine 모델 인스턴스 생성
        medicine = Medicine(
            product_name=data["product_name"],
            manufacturer_name=data["manufacturer_name"],
            appearance=data["appearance"],
            length=data["length"],
            width=data["width"],
            thickness=data["thickness"],
            category_name=data["category_name"],
            specialized_general_name=data["specialized_general_name"],
            dosage_form_name=data["dosage_form_name"]
        )

        # 데이터베이스에 데이터 추가
        db.add(medicine)
        db.commit()
        return True

    except SQLAlchemyError as e:
        db.rollback()
        return str(e)
    
def get_data(file_path: str):
    try:
        # XML 파일 읽기
        df = pd.read_excel(file_path)
        print("행 수:", df.shape[0])

        count = 0
        # 데이터 처리 및 MySQL에 삽입
        for _, row in df.iterrows():
            data = {
                "product_name": row.get("품목명"),
                "manufacturer_name": row.get("업소명"),
                "appearance": row.get("성상"),
                "length": row.get("크기장축"),
                "width": row.get("크기단축"),
                "thickness": row.get("크기두께"),
                "category_name": row.get("분류명"),
                "specialized_general_name": row.get("전문일반구분"),
                "dosage_form_name": row.get("제형코드명"),
            }
            
            result = insert_data_to_mysql(data)
            count += 1
            
        print("count:", count)
        return {"message": "Data inserted into MySQL successfully."}

    except Exception as e:
        return {"message": f"An error occurred: {str(e)}"}

# MySQL에 더미 데이터 삽입
def create_medicines():
    # 세션 생성
    db = SessionLocal()

    # 더미 데이터 생성
    dummy_data = [
		Medicine(
			product_name="Dummy_Product_1",
			manufacturer_name="Dummy_Manufacturer_1",
			appearance="Dummy_Appearance_1",
			length="Dummy_Length_1",
			width="Dummy_Width_1",
			thickness="Dummy_Thickness_1",
			category_name="Dummy_Category_1",
			specialized_general_name="Dummy_Specialized_General_1",
			dosage_form_name="Dummy_Dosage_Form_1",
		),
		Medicine(
			product_name="Dummy_Product_2",
			manufacturer_name="Dummy_Manufacturer_2",
			appearance="Dummy_Appearance_2",
			length="Dummy_Length_2",
			width="Dummy_Width_2",
			thickness="Dummy_Thickness_2",
			category_name="Dummy_Category_2",
			specialized_general_name="Dummy_Specialized_General_2",
			dosage_form_name="Dummy_Dosage_Form_2",
		),
    ]

    # 더미 데이터 삽입
    for dummy in dummy_data:
        db.add(dummy)
    db.commit()
    db.refresh(dummy)
    
    # 세션 종료
    db.close()

# 실행
# create_medicines()
get_data("/Users/jungeun/Downloads/OpenData_PotOpenTabletIdntfc20230319.xls")
