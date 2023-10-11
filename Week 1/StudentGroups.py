students = int(input("How many students?:"))
req_groups = int(input("Required group size?:"))
student_groups = int(students / req_groups)
left_over = students - (req_groups * student_groups)

print(f"There will be {student_groups} full student groups with {left_over} students in the left over group.")
