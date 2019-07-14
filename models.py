import db
import bcrypt
from time import time
from mimetypes import guess_type
from base64 import b64decode
import datetime


class Warga:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get(self):
        field = "`kdwarga`, `nmrt`, `norumah`, `nokk`, `nmkk`, `statustinggal`, `pengurus`"
        table = "`warga`"
        sql_filter = "`norumah` = '%s'" % self.username
        statement = "SELECT %s FROM %s WHERE %s LIMIT 0,1" % (
            field, table, sql_filter)
        connection = db.open_connection()
        cursor = db.sql_cursor(connection, statement)
        result = cursor.fetchone()
        db.close_connection(connection, cursor)
        return result

    def verify_hash(self):
        field = "`norumah`, `password`"
        table = "`warga`"
        sql_filter = "`norumah` = '%s'" % self.username
        statement = "SELECT %s FROM %s WHERE %s LIMIT 0,1" % (
            field, table, sql_filter)
        connection = db.open_connection()
        cursor = db.sql_cursor(connection, statement)
        result = cursor.fetchone()
        db.close_connection(connection, cursor)
        bytes_password = bytes(self.password, "utf-8")
        bytes_hashed = bytes(result[1], "utf-8")
        return bcrypt.checkpw(bytes_password, bytes_hashed)

    def post(self, body):
        password_hashed = bcrypt.hashpw(
            bytes(body["password"], "utf-8"), bcrypt.gensalt())
        field = "(`nmrt`, `norumah`, `nokk`, `nmkk`, `statustinggal`, `pengurus`, `password`)"
        values = "('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
            body["nmrt"], body["norumah"], body["nokk"], body["nmkk"], body["statustinggal"], body["pengurus"], password_hashed.decode("utf-8"))
        table = "`warga`"
        statement = "INSERT INTO %s %s VALUES %s" % (
            table, field, values)
        connection = db.open_connection()
        cursor = db.sql_cursor(connection, statement)
        connection.commit()
        db.close_connection(connection, cursor)
        result = cursor.rowcount
        return result

    def put(self, body):
        field = "`nmrt`='%s', `nokk`='%s', `nmkk`='%s', `statustinggal`='%s', `pengurus`='%s'" % (body['nmrt'], body['nokk'], body['nmkk'], body['statustinggal'], body['pengurus'])
        table = "`warga`"
        sql_filter = "`norumah`='%s'" % (body['norumah'])
        statement = "UPDATE %s SET %s WHERE %s" % (
            table, field, sql_filter)
        connection = db.open_connection()
        cursor = db.sql_cursor(connection, statement)
        connection.commit()
        db.close_connection(connection, cursor)
        return cursor.rowcount

    def put_password(self, body):
        password_hashed = bcrypt.hashpw(
            bytes(body["password"], "utf-8"), bcrypt.gensalt())
        field = "`password`='%s'" % (password_hashed.decode("utf-8"))
        table = "`warga`"
        sql_filter = "`norumah`='%s'" % (body['norumah'])
        statement = "UPDATE %s SET %s WHERE %s" % (
            table, field, sql_filter)
        connection = db.open_connection()
        cursor = db.sql_cursor(connection, statement)
        connection.commit()
        db.close_connection(connection, cursor)
        return cursor.rowcount

    def delete(self, body):
        table = "`warga`"
        sql_filter = "`norumah` = %s" % (body["norumah"])
        statement = "DELETE FROM %s WHERE %s" % (
            table, sql_filter)
        connection = db.open_connection()
        cursor = db.sql_cursor(connection, statement)
        connection.commit()
        db.close_connection(connection, cursor)
        return cursor.rowcount


# class PersonalDetail:
#     def __init__(self, emp_number):
#         self.emp_number = emp_number

#     def get(self):
#         field = "A.`emp_firstname`, A.`emp_middle_name`, A.`emp_lastname`, A.`employee_id`, A.`emp_other_id`, A.`emp_dri_lice_num`, A.`emp_dri_lice_exp_date`, A.`emp_bpjs_no`, A.`emp_npwp_no`, A.`emp_bpjs_ket_no`, D.`id` AS `work_shift_id`, A.`emp_gender`, A.`emp_marital_status`, E.`id` AS `nation_code`, A.`emp_birthday`, B.`id` AS `emp_religion`, A.`emp_birth_place`"
#         table = "(((`hs_hr_employee` AS A JOIN `ohrm_religion` AS B ON A.`emp_religion`=B.`id`) JOIN `ohrm_employee_work_shift` AS C ON A.`emp_number`=C.`emp_number`) JOIN `ohrm_work_shift` AS D ON C.`work_shift_id`=D.`id`) JOIN `ohrm_nationality` AS E ON A.`nation_code`=E.`id`"
#         sql_filter = "A.`emp_number` LIKE %s" % self.emp_number
#         statement = "SELECT %s FROM %s WHERE %s LIMIT 0,1" % (
#             field, table, sql_filter)
#         connection = db.open_connection()
#         cursor = db.sql_cursor(connection, statement)
#         result = cursor.fetchone()
#         db.close_connection(connection, cursor)
#         print(result)
#         if isinstance(result[6], datetime.date):
#             license_expiry_date = result[6].isoformat()
#         else:
#             license_expiry_date = ""
#         result = {
#             "first_name": result[0],
#             "middle_name": result[1],
#             "last_name": result[2],
#             "employee_id": result[3],
#             "no_ktp": result[4],
#             "drivers_license_number": result[5],
#             # "license_expiry_date": result[6].isoformat(),
#             "license_expiry_date": license_expiry_date,
#             "no_bpjs_kesehatan": result[7],
#             "no_npwp": result[8],
#             "no_bpjs_ketenagakerjaan": result[9],
#             "work_shift": str(result[10]),
#             "gender": str(result[11]),
#             "marital_status": result[12],
#             "nationality": str(result[13]),
#             "date_of_birth": result[14].isoformat(),
#             "religion": str(result[15]),
#             "place_of_birth": result[16]
#         }
#         return result

#     def put(self, body):
#         table = "`hs_hr_employee` AS A JOIN `ohrm_employee_work_shift` AS B ON A.`emp_number` = B.`emp_number`"
#         field = "A.`emp_firstname`='%s', A.`emp_middle_name`='%s', A.`emp_lastname`='%s', A.`emp_other_id`='%s', A.`emp_dri_lice_exp_date`='%s', A.`emp_bpjs_no`='%s', A.`emp_npwp_no`='%s', A.`emp_bpjs_ket_no`='%s', B.`work_shift_id`='%s', A.`emp_gender`='%s', A.`emp_marital_status`='%s', A.`nation_code`='%s', A.`emp_religion`='%s', A.`emp_birth_place`='%s'" % (
#             body["first_name"], body["middle_name"], body["last_name"], body["no_ktp"], body["license_expiry_date"], body["no_bpjs_kesehatan"], body["no_npwp"], body["no_bpjs_ketenagakerjaan"], body["work_shift"], body["gender"], body["marital_status"], body["nationality"], body["religion"], body["place_of_birth"])
#         sql_filter = "A.`emp_number` = '%s'" % (self.emp_number)
#         statement = "UPDATE %s SET %s WHERE %s " % (
#             table, field, sql_filter)
#         connection = db.open_connection()
#         cursor = db.sql_cursor(connection, statement)
#         connection.commit()
#         db.close_connection(cursor, connection)
#         result = cursor.rowcount
#         return result


# class Attachment:
#     def __init__(self, emp_number, screen):
#         self.emp_number = emp_number
#         self.screen = screen

#     def get_meta_all(self):
#         field = "`emp_number`,`eattach_id`,`eattach_desc`,`eattach_filename`, `eattach_size`,`eattach_type`,`screen`,`attached_by`,`attached_by_name`, DATE_FORMAT(`attached_time`, '%Y-%m-%dT%T') AS `attached_time`"
#         table = "`hs_hr_emp_attachment`"
#         sql_filter = "`emp_number`='%s' AND `screen`='%s'" % (
#             self.emp_number, self.screen)
#         statement = "SELECT %s FROM %s WHERE %s LIMIT 0,1000" % (
#             field, table, sql_filter)
#         connection = db.open_connection()
#         cursor = db.sql_cursor(connection, statement)
#         result = cursor.fetchall()
#         db.close_connection(connection, cursor)
#         return result

#     def get_meta(self, file_id):
#         field = "`emp_number`,`eattach_id`,`eattach_desc`, `eattach_filename`, `eattach_size`, `eattach_type`,`screen`,`attached_by`,`attached_by_name`, DATE_FORMAT(`attached_time`, '%Y-%m-%dT%T') AS `attached_time`"
#         table = "`hs_hr_emp_attachment`"
#         sql_filter = "`emp_number`='%s' AND `screen`='%s' AND `eattach_id` = '%s'" % (
#             self.emp_number, self.screen, file_id)
#         statement = "SELECT %s FROM %s WHERE %s LIMIT 0,1" % (
#             field, table, sql_filter)
#         connection = db.open_connection()
#         cursor = db.sql_cursor(connection, statement)
#         result = cursor.fetchone()
#         db.close_connection(connection, cursor)
#         return result

#     def get(self, file_id):
#         field = "`emp_number`,`eattach_id`,`eattach_desc`, `eattach_filename`, `eattach_size`, `eattach_attachment`, `eattach_type`,`screen`,`attached_by`,`attached_by_name`, DATE_FORMAT(`attached_time`, '%Y-%m-%dT%T') AS `attached_time`"
#         table = "`hs_hr_emp_attachment`"
#         sql_filter = "`emp_number`='%s' AND `screen`='%s' AND `eattach_id` = '%s'" % (
#             self.emp_number, self.screen, file_id)
#         statement = "SELECT %s FROM %s WHERE %s LIMIT 0,1" % (
#             field, table, sql_filter)
#         connection = db.open_connection()
#         cursor = db.sql_cursor(connection, statement)
#         result = cursor.fetchone()
#         db.close_connection(connection, cursor)
#         return result

#     def put_comment(self, body):
#         field = "`eattach_desc` = '%s'" % body['comment']
#         table = "`hs_hr_emp_attachment`"
#         sql_filter = "`emp_number`='%s' AND `screen`='%s' AND `eattach_id` = '%s'" % (
#             self.emp_number, self.screen, body['file_id'])
#         statement = "UPDATE %s SET %s WHERE %s" % (
#             table, field, sql_filter)
#         connection = db.open_connection()
#         cursor = db.sql_cursor(connection, statement)
#         connection.commit()
#         db.close_connection(connection, cursor)
#         return cursor.rowcount

#     def post(self, body):
#         emp_number = self.emp_number
#         eattach_id = str(int(time()))
#         eattach_desc = body['comment']
#         eattach_filename = body['file_name']
#         eattach_attachment = b64decode(body["select_file"]).hex()
#         eattach_size = int((len(body["select_file"]) * 3/4) -
#                            body["select_file"].count("=", -2))
#         eattach_size = str(eattach_size)
#         eattach_type = guess_type(eattach_filename)[0]
#         screen = self.screen
#         attached_by = self.emp_number
#         field = "(`emp_number`,`eattach_id`,`eattach_desc`, `eattach_filename`, `eattach_size`, `eattach_attachment`, `eattach_type`,`screen`,`attached_by`)"
#         values = "('%s', '%s', '%s', '%s', '%s', x'%s', '%s', '%s', '%s')" % (emp_number, eattach_id, eattach_desc,
#                                                                               eattach_filename, eattach_size, eattach_attachment, eattach_type, screen, attached_by)
#         table = "`hs_hr_emp_attachment`"
#         statement = "INSERT INTO %s %s VALUES %s" % (
#             table, field, values)
#         connection = db.open_connection()
#         cursor = db.sql_cursor(connection, statement)
#         connection.commit()
#         db.close_connection(connection, cursor)
#         result = {
#             "file_id": eattach_id,
#             "comment": eattach_desc,
#             "file_name": eattach_filename,
#             "size": eattach_size,
#             "type": eattach_type,
#             "date_added": self.get_meta(eattach_id)[9]
#         }
#         return result

#     def delete(self, file_id):
#         table = "`hs_hr_emp_attachment`"
#         sql_filter = "`emp_number` = %s AND `eattach_id` = %s" % (
#             self.emp_number, file_id)
#         statement = "DELETE FROM %s WHERE %s" % (
#             table, sql_filter)
#         connection = db.open_connection()
#         cursor = db.sql_cursor(connection, statement)
#         connection.commit()
#         db.close_connection(connection, cursor)
#         return cursor.rowcount

# class Nationality():
#     def get_all(self):
#         field = "`id`, `name`"
#         table = "`ohrm_nationality`"
#         statement = "SELECT %s FROM %s LIMIT 0,1000" % (
#             field, table)
#         connection = db.open_connection()
#         cursor = db.sql_cursor(connection, statement)
#         result = cursor.fetchall()
#         db.close_connection(connection, cursor)
#         return result


# class WorkShift():
#     def get_all(self):
#         field = "`id`, `name`"
#         table = "`ohrm_work_shift`"
#         statement = "SELECT %s FROM %s LIMIT 0,1000" % (
#             field, table)
#         connection = db.open_connection()
#         cursor = db.sql_cursor(connection, statement)
#         result = cursor.fetchall()
#         db.close_connection(connection, cursor)
#         return result


# class Religion():
#     def get_all(self):
#         field = "`id`, `name`"
#         table = "`ohrm_religion`"
#         statement = "SELECT %s FROM %s LIMIT 0,1000" % (
#             field, table)
#         connection = db.open_connection()
#         cursor = db.sql_cursor(connection, statement)
#         result = cursor.fetchall()
#         db.close_connection(connection, cursor)
#         return result
