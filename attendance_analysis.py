import numpy as np

Attendance=[1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1]
Attendance_list=np.array(Attendance)
print(Attendance_list)

total=len(Attendance)

present=np.sum(Attendance)
print(f"Total Present Days: {present}")

absent=total-present
print(f"Total Absent Days: {absent}")

percentage=(present/total)*100
print(f"Attendance Percentage: {percentage:.2f}%")

if percentage>=75:
  print("Student is Eligible For Exam")
else:
  print("Student is Not Eligible For Exam")

fi=np.where(Attendance_list==0)[0]
print(f"Days Student is Absent: {fi}")
