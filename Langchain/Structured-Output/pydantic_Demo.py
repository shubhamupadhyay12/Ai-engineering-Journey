#pydantic ensures that the data you work with is correct , structured and type-safe


from pydantic import BaseModel,EmailStr , Field
from typing import Optional


class student(BaseModel):
    name : str = 'shubham'
    age : Optional[int]= None
    email : EmailStr
    cgpa : float = Field(gt=0,lt=10, default=5 , description='A decimal value reprenitng the cgpa of the student')  #greater than 0 and less than or equal to 10


new_student = {'age':'35' , 'email':'abc@gmail.com' }   #if not age is given the output is none

student = student(**new_student)

student_dict = dict(student)
print(student_dict['age'])

student_json = student.model_dump_json()