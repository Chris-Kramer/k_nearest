from typing import Optional, List, ForwardRef

class Student:
  """
  A student in the course
  """
  
  # internal class attributed to store the last id issued
  __id_counter = 0

  @staticmethod
  def _get_new_id() -> int:
    """
    Returns a newly issued id
    """
    Student.__id_counter += 1
    return Student.__id_counter

  def __init__(self,name:str,email:str):
    """
    Creates a new student with a unique id.

    Parameters:
    -----------
     * `name` is the full name of the student
     * `email` is a valid email for this student
    """
    self._name = name
    self._email = email
    self._id = Student._get_new_id()
    self._grade = None

  def id(self) -> int:
    """
    The unique identifier of this student
    """
    return self._id

  def name(self) -> str:
    """
    The full name of this student.
    """
    return self._name

  def set_name(self, name:str):
    """
    Set the full name of this student to `name`.
    """
    self._name = name

  def email(self) -> str:
    """
    The email of this student.
    """
    return self._email

  def set_email(self, email:str):
    """
    Set the email of this student to `email`.
    """
    self._email = email
  
  def grade(self) -> Optional[int]:
    """
    The grade of this student.
    """
    return self._grade
    
  def set_grade(self, grade:int):
    """
    Set the grade for this student.
    Assumes: self.grade() is None and grade in {-3,0,2,4,7,10,12}
    """    
    self._grade = grade

  @staticmethod
  def is_grade(value:int) -> bool:
    """
    Check if `value` represents a valid grade
    """
    return value in [-3,0,2,4,7,10,12]
  
  def __repr__(self) -> str:
    return f"Student(id={self.id()}, name={repr(self.name())}, grade={self.grade()})"
  
  def __str__(self) -> str:
    return f"{self.name()} (ID {self.id()})"

class Course:
  """
  A course
  """

  def __init__(self,title:str,code:str):
    """
    Creates a course with the given title and code.
    """
    self._title = title
    self._code = code
    self._students = []

  def title(self) -> str:
    """
    The title of this course
    """
    return self._title

  def code(self) -> str:
    """
    The code of this course
    """
    return self._code

  def find_student_by_id(self, id:int) -> Optional[Student]:
    """
    Finds a student with the given `id`, returns None if no student is found.
    """
    i = len(self._students)-1
    while i >= 0 and self._students[i].id() != id:
        i -= 1
    if i == -1: return None
    else: return self._students[i]

  def find_students_by_name(self, name:str) -> List[Student]:
    """
    A list with all students with the given `name`.
    """
    return [ student for student in self._students
                     if student.name() == name ]

  def add_student(self, student:Student):
    """
    Add a student to the course.
    Assumes the student is not in the course
    """
    self._students.append(student)

  def del_student(self, student:Student):
    """
    Remove a student to the course.
    Assumes the student is in the course
    """    
    self._students.remove(student)
  
  def students(self) -> List[Student]:
    """
    Returns a list with all the students in the course.
    """
    return self._students.copy()

  def grade_avg(self) -> Optional[float]:
    """
    Computes the average grade (ignores students without a grade)
    """
    grades = [ student.grade() for student in self._students
                               if student.grade() ]
    if len(grades) == 0:
      return None
    else:
      return sum(grades) / len(grades)

  
