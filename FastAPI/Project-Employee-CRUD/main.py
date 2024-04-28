from fastapi import FastAPI, Depends, status, HTTPException
from typing import Annotated
from pydantic import BaseModel
from database import engine, SessionLocal
import models
from models import Employee
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind = engine)

class EmployeeBase(BaseModel):
    first_name : str
    last_name : str = None
    email : str

def get_db():
    db = SessionLocal()

    try :
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/employee", status_code = status.HTTP_201_CREATED)
async def create_employees(employee : EmployeeBase, db : db_dependency):
    db_employee = Employee(first_name = employee.first_name, last_name = employee.last_name, email = employee.email)
    result = db.query(Employee).filter(Employee.email == db_employee.email).first()
    if result : 
        raise HTTPException(status_code=409, detail = "A person with same email already exists")
    if len(db_employee.first_name) <= 2 or db_employee.first_name == " ":
        raise HTTPException(status_code=400, detail="Invalid First Name")
    if not db_employee.email.endswith("@gmail.com") or len(db_employee.email.split('@')[0]) <=1 :
        raise HTTPException(status_code=400, detail="Invalid Email")
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

@app.get("/employee")
async def get_employee(db : db_dependency):
    result = db.query(Employee).all()
    return result

@app.get("/employee/{id}")
async def get_employee_by_id(id : int, db : db_dependency):
    result = db.query(Employee).filter(Employee.id == id).first()
    if not result :
        raise HTTPException(status_code=404, detail=f"No Employee found with Id : {id}")
    return result

@app.put("/employee/{id}")
async def update_employee(employee : EmployeeBase, id : int, db : db_dependency):
    db_employee = db.query(Employee).filter(Employee.id == id).first()
    if not db_employee :
        raise HTTPException(status_code=404, detail= f"No Employee Found with the Id : {id}")
    if employee.first_name :
        if len(db_employee.first_name) <= 2 or db_employee.first_name == " ":
            raise HTTPException(status_code=400, detail="Invalid First Name")
        db_employee.first_name = employee.first_name
    if employee.last_name:
        db_employee.last_name = employee.last_name
    if employee.email :
        result = db.query(Employee).filter(Employee.email == employee.email).first()
        if result : 
            raise HTTPException(status_code=409, detail = "A person with same email already exists")
        if not db_employee.email.endswith("@gmail.com") or len(db_employee.email.split('@')[0]) <=1 :
            raise HTTPException(status_code=400, detail="Invalid Email")
        db_employee.email = employee.email
    db.commit()
    db.refresh(db_employee)
    return db_employee

@app.delete("/employee/{id}")
async def delete_employee(id : int, db:db_dependency):
    db_employee = db.query(Employee).filter(Employee.id == id).first()
    if db_employee is None : 
        raise HTTPException(status_code=404, detail=f"No Item found with ID : {id}")
    db.delete(db_employee)
    db.commit()
    return {"message" : "Employee successfully Deleted"}