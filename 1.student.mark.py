student_adder = []
def add_student(student_id: str, name: str):
      if any(student['id'] == student_id for student in student_adder):
           print(f"your stdid is exsited")
           return
      new_student = {
           'id': student_id,
           'name': name,
}
      student_adder.append(new_student)
      print(f"Student {name} (ID: {student_id}) added!")
def  display_student():
      if not student_adder:
           print(f"\n The list is empty rn!")
           return
      for student in student_adder:
          student_id = student['id']
          name = student['name']
      print(f"ID: {student_id} | Name: {name}")
add_student(2213139, "phung minh hieu")

