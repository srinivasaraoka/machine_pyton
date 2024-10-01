


tupple1=()
tupple=(1,2,3,4,4)
'''
In Python, a tuple  that is used to store an ordered 
collection of items. Tuples are similar to lists, but they have some important 
differences:

LIST

1. Lists are mutable
2. List is a container to contain different types of
  objects and is used to iterate objects.
3. Syntax Of Listlist = ['a', 'b', 'c', 1,2,3]
4. List iteration is slower
5. Lists consume more memory
6. Operations like insertion and deletion are better

Tuple
1. Tuples are immutable
2. Tuple is also similar to list but contains immutable
objects.
3. Syntax Of Tuple
tuples = ('a', 'b', 'c', 1, 2)
4. Tuple processing is faster than List.
5. Tuple consume less memory
6. Elements can be accessed better.

performed.
Immutability: Tuples are immutable, meaning once they are created, their elements cannot be changed or modified. This makes tuples a good choice for data that should not be altered.
Syntax: Tuples are defined by enclosing elements in parentheses ( ), separated by commas. For example: my_tuple = (1, 2, 3).
Indexing and Slicing: Like lists, tuples support indexing and slicing. You can access elements by their index and get sub-parts of the tuple using slicing.
Performance: Due to their immutability, tuples can be slightly more performant than lists for certain operations, and they can be used as keys in dictionaries, while lists cannot.
Heterogeneous: Tuples can contain elements of different data types, such as integers, strings, and even other tuples.

'''
# Define a global list to store student records
student_records = []

# Function to add a new student record
def add_student(id, name, age, grades):
    student = (id, name, age, grades)
    student_records.append(student)
    print(f"Student {name} added successfully.")

# Function to update a student's information
def update_student(id, name, age, grades):
    for i, student in enumerate(student_records):
        if student[0] == id:  # Check if id matches
            # Update student record
            student_records[i] = (id, name, age, grades)
            print(f"Student {name}'s information updated.")
            return
    print(f"Student with ID {id} not found.")

# Function to calculate and display average grade for a student
def average_grade(id):
    for student in student_records:
        if student[0] == id:
            grades = student[3]
            average = sum(grades) / len(grades)
            print(f"Average grade for {student[1]}: {average:.2f}")
            return
    #print(f"Student with ID {id} not found.")

# Function to list all students sorted by average grade
def list_students_sorted_by_average_grade():
    sorted_students = sorted(student_records, key=lambda student: sum(student[3]) / len(student[3]), reverse=True)
    print(sorted_students)
    #print("List of students sorted by average grade:")
    for student in sorted_students:
        average = sum(student[3]) / len(student[3])
        #print(f"ID: {student[0]}, Name: {student[1]}, Average Grade: {average:.2f}")

# Example usage:
if __name__ == "__main__":
    # Adding students
    add_student(1, "Alice", 20, (85, 90, 92))
    add_student(2, "Bob", 21, (78, 80, 85))
    add_student(3, "Charlie", 19, (90, 95, 88))

    # Updating a student's information
    update_student(2, "Bob Smith", 21, (78, 80, 85, 88))

    # Calculating and displaying average grade for a student
    average_grade(1)

    # Listing all students sorted by average grade
    list_students_sorted_by_average_grade()

#sorted_students = sorted(student_records, key=lambda student: sum(student[3]) / len(student[3]), reverse=True)