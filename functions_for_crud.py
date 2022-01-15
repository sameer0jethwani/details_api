from model import Details
from sqlalchemy.orm import Session
import model

def create_details_for(db:Session,details:dict):



    a=Details()

    a.names=details["name"]
    a.address=details["address"]
    a.phone_numbers=details["phone_number"]
    db.add(a)
    db.commit()
    db.refresh(a)
    return details

def get_by_name(db:Session,name:str):

    rows = db.query(model.Details)
    for i in rows:
        if i.names==str(name):
            return {"name":i.names,"address":i.address,"phone_number":i.phone_numbers}

def get_by_phone_number(db:Session,phone_number:str):

    rows = db.query(model.Details)
    for i in rows:
        if i.phone_numbers==str(phone_number):
            return {"name":i.names,"address":i.address,"phone_number":i.phone_numbers}

def update_by_name(db:Session,name:str,details:dict):
    rows = db.query(model.Details)
    for i in rows:
        if i.names == str(name):
            i.names=details["name"]
            i.address=details["address"]
            i.phone_numbers=details["phone_number"]

            db.commit()
            return {"name":i.names,"address":i.address,"phone_number":i.phone_numbers}

def delete_by_name(db:Session,name:str):
    rows = db.query(model.Details)
    for i in rows:
        if i.names == str(name):
            n=i.names

            db.delete(i)
            db.commit()
            return f"detail deleted of {n}"




