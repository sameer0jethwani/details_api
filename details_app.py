from fastapi import FastAPI,Path,Query,HTTPException,Depends
from schemas import *
from db import SessionLocal,engine
from functions_for_crud import *

app=FastAPI(title="Address Details",
    description="You can perform CRUD operations by using this API",
    version="1.0.0")
model.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()





@app.post("/create_details")
def create_details(detail:Item,db: Session = Depends(get_db)):

    v=get_by_name(db=db,name=detail.name)
    if v is None:
        diction={"name": detail.name, "address": detail.address, "phone_number": detail.phone_number}
        v1=create_details_for(db=db,details=diction)
        return v1
    else:
        raise HTTPException(status_code=404, detail="sorry this name already exist")




@app.get("/get_details_with_name/{name}")
def get_details_with_name(name:str,db: Session = Depends(get_db)):
    """
            This method will return detail based on name
            :return: data row if exist else  error message
            """
    v=get_by_name(db=db,name=name)
    if v!=None:
        return v
    else:
        raise HTTPException(status_code=404, detail="sorry this name does not exist")

@app.get("/get_details_with_phone_number/{phone_number}")
def get_details_with_phone_number(phone_number:str,db: Session = Depends(get_db)):
    """
        This method will return detail based on phone number
        :return: data row if exist else  error message
        """
    v=get_by_phone_number(db=db,phone_number=phone_number)
    if v!=None:
        return v
    else:
        raise HTTPException(status_code=404, detail="sorry this phone number does not exist")

@app.put("/update_details/{name}")
def update_details_name(name:str,detail:UpdateItem,db: Session = Depends(get_db)):
    """
       this method will update the database
       :return: updated detail record
       """
    v=get_by_name(db=db,name=name)
    if v!=None:
        diction = {"name": detail.name, "address": detail.address, "phone_number": detail.phone_number}
        return update_by_name(db=db,name=name,details=diction)
    else:
        raise HTTPException(status_code=404, detail="sorry this name does not exist")


@app.delete("/delete_details/{name}")
def delete_details_name(name:str,db: Session = Depends(get_db)):
    """
           this method will delete the database
           :return: it will delete that details by name
           """
    return delete_by_name(db=db,name=name)


