students = ["Balaji", "Wasim", "Theetchith", "Viswak", "Sanjay", "Pranav", "Shrivardhan"]

attendance = {}

def mark_attendance():
    print("\n--- Mark Attendance ---")
    for student in students:
        while True:
            status = input(f"Is {student} present? (P/A): ").strip().upper()
            if status in ['P', 'A']:
                attendance[student] = "Present" if status == 'P' else "Absent"
                break
            else:
                print("Invalid input! Please enter 'P' for Present or 'A' for Absent.")

def display_attendance():
    print("\n--- Attendance Record ---")
    print(f"{'Name':<10} {'Status':<10}")
    print("-" * 20)
    for student, status in attendance.items():
        print(f"{student:<10} {status:<10}")

def save_to_file():
    with open(" attendance_record.txt", "w") as file:
        file.write("Student Attendance Record\n")
        file.write("-" * 30 + "\n")
        for student, status in attendance.items():
            file.write(f"{student}: {status}\n")
    print("\nAttendance saved to 'attendance_record.txt'")

while True:
    print("\n===== Student Attendance Tracker =====")
    print("1. Mark Attendance")
    print("2. Display Attendance")
    print("3. Save to File")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        mark_attendance()
    elif choice == '2':
        display_attendance()
    elif choice == '3':
        save_to_file()
    elif choice == '4':
        print("Exiting program... Goodbye!")
        break
    else:
        print("Invalid choice! Please select a valid option.")

