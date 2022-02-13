"""
Data model for the course manager. Defines Student and Course.

*** This version defines only the public contract of Student and Course: its methods are not implemented ***
"""

from typing import Optional, List, ForwardRef

class Student:
  """
  A student in the course
  """
  
  def __init__(self,name:str,email:str):
    """
    Creates a new student with a unique id.

    Parameters:
    -----------
     * `name` is the full name of the student
     * `email` is a valid email for this student
    """
    pass

  def id(self) -> int:
    """
    The unique identifier of this student
    """
    pass

  def name(self) -> str:
    """
    The full name of this student.
    """
    pass

  def set_name(self, name:str):
    """
    Set the full name of this student to `name`.
    """
    pass

  def email(self) -> str:
    """
    The email of this student.
    """
    pass

  def set_email(self, email:str):
    """
    Set the email of this student to `email`.
    """
    pass
  
  def grade(self) -> Optional[int]:
    """
    The grade of this student.
    """
    pass
    
  def set_grade(self, grade:int):
    """
    Set the grade for this student.
    Assumes: self.grade() is None and grade in {-3,0,2,4,7,10,12}
    """    
    pass

  @staticmethod
  def is_grade(value:int) -> bool:
    """
    Check if `value` represents a valid grade
    """
    pass

class Course:
  """
  A course
  """

  def __init__(self,title:str,code:str):
    """
    Creates a course with the given title and code.
    """
    pass

  def title(self) -> str:
    """
    The title of this course
    """
    pass

  def code(self) -> str:
    """
    The code of this course
    """
    pass

  def find_student_by_id(self, id:int) -> Optional[Student]:
    """
    Finds a student with the given `id`, returns None if no student is found.
    """
    pass

  def find_students_by_name(self, name:str) -> List[Student]:
    """
    A list with all students with the given `name`.
    """
    pass

  def add_student(self, student:Student):
    """
    Add a student to the course.
    Assumes the student is not in the course
    """
    pass

  def del_student(self, student:Student):
    """
    Remove a student to the course.
    Assumes the student is in the course
    """    
    pass
  
  def students(self) -> List[Student]:
    """
    Returns a list with all the students in the course.
    """
    pass

  def grade_avg(self) -> Optional[float]:
    """
    Computes the average grade (ignores students without a grade)
    """
    pass

  
