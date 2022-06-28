from asyncore import write
import json

def names_of_registered_students(input_json_path, course_name):
    with open(input_json_path, 'r') as input_file:
        student_dict = json.load(input_file)
        return [ student["student_name"] for student in student_dict.values() if course_name in student["registered_courses"]]


def enrollment_numbers(input_json_path, output_file_path):
    with open(input_json_path, 'r') as json_file:
        main_input_dict = json.load(json_file)
        main_output_list = []
        for student in main_input_dict.values():
            for course in student["registered_courses"]:
                if(course in main_output_list):
                    continue
                else:
                    main_output_list.append(course)
        main_output_list.sort()
    with open(output_file_path, 'w') as file:
        print(main_output_list)
        for course in main_output_list:
            file.write('"' + course + '" ' +  str(len(names_of_registered_students(input_json_path, course))) + "\n")


print("hello") 
# print(names_of_registered_students("students_database.json", "Introduction to Algorithms"))
enrollment_numbers("students_database.json", "out.txt")