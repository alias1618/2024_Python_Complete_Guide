def get_all_users():
    yield from get_teachers_id():
    yield from get_students_id():

def teacher_id_generator():
    for id in get_teachers_id():
        yield id

def student_id_generator():
    for id in get_students_id():
        yield id