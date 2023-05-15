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

# MySQL에 더미 데이터 삽입
def create_medicines():
    # 세션 생성
    db = SessionLocal()

    # 더미 데이터 생성
    dummy_data = [
        # Medicine(
        #     product_name="Dummy_Product_1",
        #     manufacturer_name="Dummy_Manufacturer_1",
        #     product_category="Dummy_Category_1",
        #     additive=json.dumps(["Additive_A", "Additive_B"]),
        #     manufacturing_importing="Dummy_Manufacturing/Importing 1",
        #     usage="Dummy_Usage_1",
        #     capacity="Dummy_Capacity_1",
        #     caution="Dummy_Caution_1",
        #     effectiveness="Dummy_Effectiveness_1",
        # ),
        # Medicine(
        #     product_name="Dummy_Product_2",
        #     manufacturer_name="Dummy_Manufacturer_2",
        #     product_category="Dummy_Category_2",
        #     additive=json.dumps(["Additive_C", "Additive_D"]),
        #     manufacturing_importing="Dummy_Manufacturing/Importing 2",
        #     usage="Dummy_Usage_2",
        #     capacity="Dummy_Capacity_2",
        #     caution="Dummy_Caution_2",
        #     effectiveness="Dummy_Effectiveness_2",
        # ),
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
create_medicines()
