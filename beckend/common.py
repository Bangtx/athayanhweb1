from getFPathImage import database
import json


def get_all_question():
    db = database()
    data = db.select_all('question')
    data = json.dumps(data)
    return data


def get_point(id_student):
    db = database()
    point = db.select_one('point', id_student)[0][2]
    return point


def check_ans_and_update_row(id_student, result_student, id_question):
    db = database()
    answer = db.select_one('question', id_question)[0][6][-5: -4]
    point = int(get_point(id_student))
    if result_student == answer:
        point += 1
    print(point)
    db.update_one_row_by_fields('point', 'user', 1, point=point)
    # db.insert_one_row(table_name='point', user=id_student, point=point)


# check_ans_and_insert_row(1, 'C', 26)
#
# def test(table_name, key, value, **kwargs):
#     update = ''
#     i = 1
#     for k, v in kwargs.items():
#         if i < len(kwargs):
#             update += f'`{k}` = {v},  '
#         else:
#             update += f'`{k}` = {v}'
#         i += 1
#
#     sql = f'UPDATE `{table_name}` SET  {update} WHERE  `{key}` = {value} '
#     print(sql)
#
#
# test('test', key='bang', value=65, point=4)