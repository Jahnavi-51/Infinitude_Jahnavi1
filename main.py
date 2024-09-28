
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from Database import engine,Sessionlocal
from models import Base, Course
from schema import CourseSchema

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = Sessionlocal()
        yield db
    finally:
        db.close()

@app.post("/addcourse")
def add_course(request: CourseSchema, db: Session = Depends(get_db)):
    course = Course(Id=request.Id,Name=request.Name,Price=request.Price)
    db.add(course)
    db.commit()
    db.refresh(course)
    return course

@app.get("/course/{course_id}")
def get_course(course_id: int, db: Session= Depends(get_db)):
    try:
        course = db.query(Course).filter(Course.Id == course_id)
        return course
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error !!!!!!!")

