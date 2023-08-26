import csv

def main():
  employees = []

  while True:
    print("------------------------------")
    display_menu()
    choice = int(input("Enter choice: "))
    if choice==1:
      add_new_staff(employees)
    elif choice==2:
      save_employees(employees)
    elif choice==3:
      load_employees(employees)
    elif choice==4:
      show_employees(employees)
    elif choice==5:
      break

def show_employees(employees):
  for e in employees:
    print(e)

def add_new_staff(employees):
  name = input("Enter name: ")
  department = input("Enter department: ")
  employees.append({
    "name": name,
    "department": department
  })

  print("New employee added")
  for e in employees:
    print(e)

def save_employees(employees):
  file_ptr = open("employees.csv", "w")
 
  # create a csv writer and sets it headers
  headers = ["name", "department"]
    # csv_writer allows us to write rows in the csv format
  csv_writer = csv.DictWriter(file_ptr, fieldnames=headers)

  # write the first row
  csv_writer.writeheader()

  for e in employees:
    # use the csv_writer to write the row
    # write each employee dictionary to the csv file one row at a time
    csv_writer.writerow(e)

  # closing a file tells Python that you are done
  # processing it
  file_ptr.close()

def load_employees(employees):
  file_ptr = open("employees.csv", "r")
  
  # create a csv_reader
  csv_reader = csv.reader(file_ptr, delimiter=",")
  next(csv_reader, None) # skip the first row
  for row in csv_reader:
    name = row[0]
    department = row[1]

    new_employee = {
      "name": row[0],
      "department": row[1]
    }

    employees.append(new_employee)

  # close the file
  file_ptr.close()
      

def display_menu():
  print("1. Add")
  print("2. Save")
  print("3. Load")
  print("4. List All")
  print("5. Quit")

main()