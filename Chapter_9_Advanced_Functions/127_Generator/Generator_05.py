def get_all_users():
    for id in get_teachers_id():
        yield id
    for id in get_students_id():
        yield id

def teacher_id_generator():
    for id in get_teachers_id():
        yield id

def student_id_generator():
    for id in get_students_id():
        yield id