import json
import os

def courses_for_lecturers(json_directory_path, output_json_path):
    output_dict = {}
    for input_file in os.listdir(json_directory_path):
        name, ext = os.path.splitext(input_file)
        if ext == '.json':
            file_path = os.path.join(json_directory_path, input_file)
            print (file_path)
            with open(file_path, 'r') as json_file:
                main_input_dict = json.load(json_file)
                for course_dict in main_input_dict.values():
                    lecturers = course_dict.get('lecturers')
                    for lecturer in lecturers:
                        output_dict.setdefault(lecturer, [])
                        course_name = course_dict["course_name"]
                        output_dict[lecturer].append(course_name) if course_name\
                             not in output_dict[lecturer] else output_dict[lecturer]
    with open(output_json_path, 'w') as file:
        json.dump(output_dict, file, indent=4)


print ("hello")
courses_for_lecturers("semesters_databases", "out.json")

                

