import csv
def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv file: 
        writer = csv.writer(csv_file)
        
        if csv file.tell() == 0:
            writer.writerow( ["Name", "Age", "Contact Number", "E-Mail ID"])
            
        writer.writerow(info_list)
if name_ == '_main_':
    condition = True
    student num = 1

    while(condition):
        student_info=input("Enter student information for student #() in the following format (Name Age Contact Number E-mail_ID): ".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        student_info_list = student_info.split(' ')
        print("\nThe entered information is -\nName: \nAge: {\nContact number: \nE-Mail ID: {}" .format(student_info_list [0], student_info_list [1], student_info_list [2], student_info_list [3]))
        choice_check=input("Is the entered information correct? (yes/ no): ")
