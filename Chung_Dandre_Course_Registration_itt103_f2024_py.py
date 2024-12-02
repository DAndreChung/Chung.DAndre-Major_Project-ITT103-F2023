
class Courses:
    def __init__(self, course_id, course_name, course_fee):
        self.course_id = course_id
        self.course_name = course_name
        self.course_fee = course_fee



class Students:
    def __init__(self, student_id, student_name, student_email):
        self.student_id = student_id
        self.student_name = student_name
        self.student_email = student_email
        self.student_balance = 0
        self.courses = []


#this section selects the course if the course is /n
#saved in the student courses adds the course fee and prints the statement.
#4
    def enroll(self,course):
          if course not in self.courses:
            self.courses.append(course)
            print("You were enrolled in", course.course_name)
            self.student_balance = self.student_balance + course.course_fee
          else:
            print("Student is in this course")

# this gives the sum of the courses
    def get_total_fee(self):
      total_fee = 0
      for course in self.courses:
         total_fee  = total_fee + course.course_fee
      return total_fee


class RegistrationSystem:
    def __init__(self):
        self.courses = []
        self.students = {}


    #1
    def register_student(self, student_id, student_name, student_email):

      # checks student dictionary for student id
      if student_id in self.students:
        print("Student has previously been added")
      else:
        student = Students(student_id, student_name, student_email)

        #adds student to dictionary with student id as key.
        self.students[student_id] = student
        print("You registered a student")
        print("Name:",student_name)
        print("Id:",student_id)
        print("Email:",student_email)
        print('--------------------------------------------------')

    #2
    def add_course(self, course_id, course_name, course_fee):

         course_exists = False

    # Check if course_id already exists using a loop
         for existing_course in self.courses:
            if existing_course.course_id == course_id:
               course_exists = True
               break

         if course_exists:

            print("Course has already been added")

         else:
                course = Courses(course_id,course_name,course_fee)
                print("You registered a course")
                print("Name:",course_name)
                print("Id:",course_id)
                print("Fee: $",course_fee)
                self.courses.append(course)

    #3
    def show_courses(self):
      #checks in there is an item is in the course list and prints 1st option if there isnt an prints second if it is
      #a for loop is used to print each course in the list
      if not self.courses:
        print("No listed courses")
      else:
        for course in self.courses:
          print("Course_ID:",course.course_id,"Course name:",course.course_name,"Course Fee $",course.course_fee)

    #4
    def enroll_in_course(self, student_id, course_id):

      # This block checks for registered students if they are found then it loops through all through the courses and assigns
      #them to the student if no courses are found they outpu the error statements

          if student_id not in self.students:
            print("No registered students")
            return


          student = self.students[student_id]
          course = None
          for course1 in self.courses:
            if course1.course_id == course_id:
              course = course1
              break

          if course is None:
            print("No courses")
            return

          student.enroll(course)

    #5
    def show_registered_students(self):
      #checks in there is an item is in the student dictionary and prints 1st option if there isnt an prints second if it is
      #a for loop is used to print each student in the dictionary
      if not self.students:
        print("No registered students")
      else:
          for student_id, student in self.students.items():
            print("Student_ID:",student.student_id,"-Student name:",student.student_name,"-Student Email",student.student_email)

    #6
    def show_students_in_course(self, course_id):
      # this section cheks for courses in the course list then checks for students in t the student dictionaary if they are found it adds the students to a list called students in course
      #then the student it displayed as enrolled else it displays an error message

      course = None
      for course1 in self.courses:
        if course1.course_id == course_id:
            course = course1
            break

      if course is None:
       print("No courses")

      students_in_course = []

      for student in self.students.values():
        if course in student.courses:
          students_in_course.append(student)
          break

      if not students_in_course:
        print("No students in this course")

      else:
        for student in students_in_course:
          print("Student_ID:",student.student_id,"Student name:",student.student_name)


    #7
    def calculate_payment(self, student_id):

      #This section is a full calculation of the total fees the students have it then calculates the minimun fee at 40%
      #then askes the user to input the amount they want to pay and shows the difference

      if student_id in self.students:
        pass
      else:
        print("No registered students")
        return

      student = self.students[student_id]
      total_fee = student.get_total_fee()
      print("Total fee is $",total_fee)


      minimum_amount =  total_fee * .4
      print("Minimum Payment is $", minimum_amount)

      pay = float(input("How much do you want to pay: "))
      if payed == "N":
        print("You chose not to pay")
      else:
        student_balance = student.student_balance
        if pay >= minimum_amount:
          student_balance = student_balance - pay
          student.student_balance = student_balance
          print("You have paid", pay)
          print("Your reaming balance is", student_balance)
        else:
          print("You have not paid enough")


    #8
    #this shows the remaining balance for the students
    def check_student_balance(self, student_id):

    # Perform actions if student_id is found.
      if student_id in self.students:
       pass
      else:
        print("No registered students")
        return


      student = self.students[student_id]
      print("Student balance $",student.student_name, student.student_balance)


registration_system = RegistrationSystem()

while True:
    print("Select action you want to run")
    print("1. Register Student")
    print("2. Add Course")
    print("3. Show Courses")
    print("4. Enroll in Course")
    print("5. Show Registered Students")
    print("6. Show Students in a course")
    print("7. Calculate Payment")
    print("8. Check Student Balance")
    print("9. Exit")
    print('--------------------------------------------------')
    user_menu_choice = eval(input("Enter you Corresponding number: "))
    print('--------------------------------------------------')

    # Register Student

    if user_menu_choice == 1:
        student_id= str(input("Enter student id => "))
        student_name= str(input("Enter student name => "))
        student_email= str(input("Enter student email => "))
        print('--------------------------------------------------')
        registration_system.register_student(student_id, student_name, student_email)
        print('--------------------------------------------------')


    elif user_menu_choice == 2:
        course_id= str(input("Enter course id => "))
        course_name= str(input("Enter course name => "))
        course_fee= int(input("Enter course fee => $ "))
        print('--------------------------------------------------')
        registration_system.add_course(course_id, course_name,course_fee)
        print('--------------------------------------------------')

    elif user_menu_choice == 3:
        print('--------------------------------------------------')
        registration_system.show_courses()

    elif user_menu_choice == 4:
        student_id= str(input("Enter student id => "))
        course_id= str(input("Enter course id => "))
        print('--------------------------------------------------')
        registration_system.enroll_in_course(student_id, course_id)
        print('--------------------------------------------------')

    elif user_menu_choice == 5:
        print('--------------------------------------------------')
        registration_system.show_registered_students()
        print('--------------------------------------------------')

    elif user_menu_choice == 6:
        course_id= str(input("Enter course id => "))
        print('--------------------------------------------------')
        registration_system.show_students_in_course(course_id)
        print('--------------------------------------------------')
    elif user_menu_choice == 7:
        student_id= str(input("Enter student id => "))
        payed = str(input("Do you want to pay (Y or N): "))
        print('--------------------------------------------------')
        registration_system.calculate_payment(student_id)
        print('--------------------------------------------------')
    elif user_menu_choice == 8:
        student_id= str(input("Enter student id => "))
        print('--------------------------------------------------')
        registration_system.check_student_balance(student_id)
    else:
      print("leaving")
      break

