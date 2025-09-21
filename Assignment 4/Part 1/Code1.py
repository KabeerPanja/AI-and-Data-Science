# Task: Write a menu driven program to create a Student Records Management System (SRMS) using list
# 1. Add Student
# 2. Display Student
# 3. Search Student
# 4. Update Student
# 5. Delete Student
# 6. Sort Student -> by marks
# 7. Exit


records = []

def add_student():
    name = input("Enter Name: ")
    roll_no = input("Enter roll no: ")
    course = input("Enter course: ")
    marks = float(input("Enter Marks: "))

    records.append([name, roll_no, course, marks])
    print("Record successfully added...")

def display_student():
    if records:
        for record in records:
            print("------------------------------")
            print(f"Name: {record[0]}")
            print(f"Roll No: {record[1]}")
            print(f"Course: {record[2]}")
            print(f"Marks: {record[3]}")
    else:
        print("------------------------------")
        print("Empty Records!!!")

def search_student():
    if records:
        roll_no = input("Enter Roll No: ")
        for idx, record in enumerate(records):
            if roll_no == record[1]:
                return record, idx

        return None, None
            
    else:
        return None, None
    
def update_marks():
    found, idx = search_student()
    if found is not None:
        print("Record Found")
        print("------------------------------")
        print(f"Name: {found[0]}")
        print(f"Roll no: {found[1]}")
        print(f"Course: {found[2]}")
        print(f"Marks: {found[3]}")
        print("------------------------------")

        updated_marks = float(input("Enter marks to update: "))

        records[idx][3] = updated_marks
        print("Marks Updated...")
    else:
        print("Student not found in the list!! Unable to update")

def delete_student():
    found, idx = search_student()

    if found is not None:
        records.remove(found)

        print("Record deleted successfully...")

    else:
        print("Unable to delete! Record not found")

def sort_student():
    if records:
        records.sort(key=lambda x:x[3], reverse=True)
        print("Records Sorted...")
    else:
        print("Empty Records! Unable to sort")
    
while True:
    print("------------------------------")
    print("1. Add Student")
    print("2. Display Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Sort Student")
    print("7. Exit")
    print("------------------------------")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
        
    elif choice == "2":
        display_student()

    elif choice == "3":
        found, _ = search_student()
        if found is not None:
            print("------------------------------")
            print(f"Name: {found[0]}")
            print(f"Roll No: {found[1]}")
            print(f"Course: {found[2]}")
            print(f"Marks: {found[3]}")
        else:
            print("Record not found")
    
    elif choice == "4":
        update_marks()
    
    elif choice == "5":
        delete_student()
    
    elif choice == "6":
        sort_student()
    
    elif choice == "7":
        break
    
    else:
        print("Invalid Choice!")

