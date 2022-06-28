import json
import os



def names_of_registered_students(input_json_path, course_name):
    """
    This function returns a list of the names of the students who registered for
    the course with the name "course_name".
    :param input_json_path: Path of the students database json file.
    :param course_name: The name of the course.
    :return: List of the names of the students.
    """
    with open(input_json_path, 'r') as input_file:
        student_dict = json.load(input_file)
        return [ student["student_name"] for student in student_dict.values() if course_name in student["registered_courses"]]


def enrollment_numbers(input_json_path, output_file_path):
    """
    This function writes all the course names and the number of enrolled
    student in ascending order to the output file in the given path.
    :param input_json_path: Path of the students database json file.
    :param output_file_path: Path of the output text file.
    """
    with open(input_json_path, 'r') as json_file:
        main_input_dict = json.load(json_file)
        main_output_list = []
        for student in main_input_dict.values():
            for course in student["registered_courses"]:
                main_output_list.append(course) if course not in main_output_list else  main_output_list
        main_output_list.sort()
    with open(output_file_path, 'w') as file:
        for course in main_output_list:
            file.write('"' + course + '" ' +  str(len(names_of_registered_students(input_json_path, course))) + "\n")





def courses_for_lecturers(json_directory_path, output_json_path):
    """
    This function writes the courses given by each lecturer in json format.
    :param json_directory_path: Path of the semsters_data files.
    :param output_json_path: Path of the output json file.
    """
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
                        output_dict[lecturer].append(course_name) if course_name not in output_dict[lecturer] else output_dict[lecturer]
    with open(output_json_path, 'w') as file:
        json.dump(output_dict, file, indent=4)