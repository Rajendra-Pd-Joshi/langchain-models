from pydantic import BaseModel,EmailStr,Field
from typing import Optional
class Student(BaseModel):
    name: str="raju joshi"
    age: Optional[int]=None
    email: EmailStr
    cgpa: float= Field(gte=0 ,lte=10 ,description="the decimal value representing the cgpa of an student")



new_student= {
    'age':'22',
    'email':'rajujoshi@gmail.com',
    'cgpa': 9.05
}

student= Student(**new_student)
student_dict=dict(student)
print(student_dict['age'])
student_json=student.model_dump_json()
print(student_json)
