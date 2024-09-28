from pydantic import BaseModel
class CourseSchema(BaseModel):

    Id : int
    Name : str
    Price : int