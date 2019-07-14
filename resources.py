from flask_restful import Resource, reqparse
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
import models
from base64 import b64encode


class Login(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'username', help='This field cannot be blank', required=True)
        parser.add_argument(
            'password', help='This field cannot be blank', required=True)
        data = parser.parse_args()
        body = {
            "norumah": data["username"],
            "password": data["password"]
        }
        user = models.Warga()
        try:
            if user.get(body) is None:
                return {
                    "message": "Username not found"
                }, 400
            norumah = user.get(body)[2]
            if user.verify_hash(body) is True:
                access_token = create_access_token(identity=norumah)
                return {
                    'message': 'Logged in as {}'.format(data['username']),
                    'access_token': access_token
                }
            else:
                return {
                    "message": "Username & password does not match"
                }, 400
        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500


class RukunTetangga(Resource):
    def post(self):
        # emp_number = get_raw_jwt()['identity']
        parser = reqparse.RequestParser()
        parser.add_argument(
            'kdrw', help='This field cannot be blank', required=True)
        parser.add_argument(
            'nmrt', help='This field cannot be blank', required=True)
        parser.add_argument(
            'alamat', help='This field cannot be blank', required=True)
        data = parser.parse_args()
        body = {
            "kdrw": data["kdrw"], 
            "nmrt": data["nmrt"], 
            "alamat": data["alamat"]
        }
        try:
            rt = models.RukunTetangga()
            rt.post(body)
            return {
                "message": "RT succesfully created"
            }
        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500

    def get(self):
        # norumah = get_raw_jwt()['identity']
        rt = models.RukunTetangga()
        parser = reqparse.RequestParser()
        parser.add_argument(
            'nmrt', help='This field cannot be blank', required=True, location=["form", "args"])
        data = parser.parse_args()
        try:
            if data["nmrt"] == "all":
                result = []
                for rt in rt.get_all():
                    result.append(
                        {
                            "kdrt": str(rt[0]),
                            "kdrw": str(rt[1]),
                            "nmrt": str(rt[2]),
                            "alamat": rt[3]
                        }
                    )
                return {
                    "data": result,
                    "message": "RTs succesfully retrieved"
                }
            else:
                body = {
                    "nmrt": data["nmrt"]
                }
                result = rt.get(body)
                if result is None:
                    return {
                        "message": "RT not found"
                    }, 400
                else:
                    return {
                        "data": {
                            "kdrt": str(result[0]),
                            "kdrw": str(result[1]),
                            "nmrt": str(result[2]),
                            "alamat": result[3]
                        },
                        "message": "RT succesfully retrieved"
                    }
        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500

    def put(self):
        # emp_number = get_raw_jwt()['identity']
        parser = reqparse.RequestParser()
        parser.add_argument(
            'nmrt', help='This field cannot be blank', required=True)
        parser.add_argument(
            'kdrw', help='This field cannot be blank', required=True)
        parser.add_argument(
            'alamat', help='This field cannot be blank', required=True)
        data = parser.parse_args()
        rt = models.RukunTetangga()
        body = {
            "nmrt": data["nmrt"], 
            "kdrw": data["kdrw"], 
            "alamat": data["alamat"]
        }
        try:
            if rt.put(body) == 0:
                return {
                    "message": "RT not updated, no change found on submitted data or no id found"
                }
            else:
                result = {
                    "message": "RT succesfully updated"
                }
                return result
        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500

    def delete(self):
        # emp_number = get_raw_jwt()['identity']
        parser = reqparse.RequestParser()
        parser.add_argument(
            'nmrt', help='This field cannot be blank', required=True)
        data = parser.parse_args()
        rt = models.RukunTetangga()
        try:
            if rt.delete(data) == 0:
                return {
                    "message": "No nmrt found"
                }, 400
            else:
                result = {
                    "message": "RT succesfully deleted"
                }
                return result
        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500


class Warga(Resource):
    def post(self):
        # emp_number = get_raw_jwt()['identity']
        parser = reqparse.RequestParser()
        parser.add_argument(
            'nmrt', help='This field cannot be blank', required=True)
        parser.add_argument(
            'norumah', help='This field cannot be blank', required=True)
        parser.add_argument(
            'nokk', help='This field cannot be blank', required=True)
        parser.add_argument(
            'nmkk', help='This field cannot be blank', required=True)
        parser.add_argument(
            'statustinggal', help='This field cannot be blank', required=True)
        parser.add_argument(
            'pengurus', help='This field cannot be blank', required=True)
        parser.add_argument(
            'password', help='This field cannot be blank', required=True)
        data = parser.parse_args()
        try:
            warga = models.Warga()
            warga.post(data)
            return {
                "message": "Warga succesfully created"
            }
        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500

    def get(self):
        # norumah = get_raw_jwt()['identity']
        warga = models.Warga()
        parser = reqparse.RequestParser()
        parser.add_argument(
            'norumah', help='This field cannot be blank', required=True, location=["form", "args"])
        data = parser.parse_args()
        try:
            if data["norumah"] == "all":
                result = []
                for warga in warga.get_all():
                    result.append(
                        {
                            "kdwarga": str(warga[0]),
                            "nmrt": str(warga[1]),
                            "norumah": str(warga[2]),
                            "nokk": str(warga[3]), 
                            "nmkk": warga[4], 
                            "statustinggal": warga[5], 
                            "pengurus": str(warga[6])
                        }
                    )
                return {
                    "data": result,
                    "message": "Warga succesfully retrieved"
                }
            else:
                result = warga.get(data)
                if result is None:
                    return {
                        "message": "Warga not found"
                    }, 400
                else:
                    return {
                        "data": {
                            "kdwarga": str(result[0]),
                            "nmrt": str(result[1]),
                            "norumah": str(result[2]),
                            "nokk": str(result[3]), 
                            "nmkk": result[4], 
                            "statustinggal": result[5], 
                            "pengurus": str(result[6])
                        },
                        "message": "Warga succesfully retrieved"
                    }
        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500

    def put(self):
        # emp_number = get_raw_jwt()['identity']
        parser = reqparse.RequestParser()
        parser.add_argument(
            'nmrt', help='This field cannot be blank', required=True)
        parser.add_argument(
            'norumah', help='This field cannot be blank', required=True)
        parser.add_argument(
            'nokk', help='This field cannot be blank', required=True)
        parser.add_argument(
            'nmkk', help='This field cannot be blank', required=True)
        parser.add_argument(
            'statustinggal', help='This field cannot be blank', required=True)
        parser.add_argument(
            'pengurus', help='This field cannot be blank', required=True)
        data = parser.parse_args()
        warga = models.Warga()
        try:
            if warga.put(data) == 0:
                return {
                    "message": "Warga not updated, no change found on submitted data or no id found"
                }
            else:
                result = {
                    "message": "Warga succesfully updated"
                }
                return result
        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500

    def delete(self):
        # emp_number = get_raw_jwt()['identity']
        parser = reqparse.RequestParser()
        parser.add_argument(
            'norumah', help='This field cannot be blank', required=True)
        data = parser.parse_args()
        warga = models.Warga()
        try:
            if warga.delete(data) == 0:
                return {
                    "message": "No norumah found"
                }, 400
            else:
                result = {
                    "message": "Warga succesfully deleted"
                }
                return result
        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500


class Pemasukan(Resource):
    def post(self):
        # emp_number = get_raw_jwt()['identity']
        parser = reqparse.RequestParser()
        parser.add_argument(
            'norumah', help='This field cannot be blank', required=True)
        parser.add_argument(
            'nokk', help='This field cannot be blank', required=True)
        parser.add_argument(
            'jumlah', help='This field cannot be blank', required=True)
        parser.add_argument(
            'keterangan', help='This field cannot be blank', required=True)
        parser.add_argument(
            'dokumen_bayar', help='This field cannot be blank', required=True)
        data = parser.parse_args()
        try:
            pemasukan = models.Pemasukan()
            pemasukan.post(data)
            return {
                "message": "Pemasukan succesfully created"
            }
        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500

    def get(self):
        # norumah = get_raw_jwt()['identity']
        pemasukan = models.Pemasukan()
        parser = reqparse.RequestParser()
        parser.add_argument(
            'kdpemasukan', help='This field cannot be blank', required=True, location=["form", "args"])
        data = parser.parse_args()
        try:
            if data["kdpemasukan"] == "all":
                result = []
                for pemasukan in pemasukan.get_all():
                    result.append(
                        {
                            "kdpemasukan": str(pemasukan[0]),
                            "tanggal": str(pemasukan[1]),
                            "norumah": str(pemasukan[2]),
                            "nokk": str(pemasukan[3]),
                            "jumlah": str(pemasukan[4]),
                            "keterangan": pemasukan[5],
                            "dokumen_bayar": str(pemasukan[6]),
                            "terverifikasi": str(pemasukan[7])
                        }
                    )
                return {
                    "data": result,
                    "message": "Pemasukan succesfully retrieved"
                }
            else:
                result = pemasukan.get(data)
                if result is None:
                    return {
                        "message": "Pemasukan not found"
                    }, 400
                else:
                    return {
                        "data": {
                            "kdpemasukan": str(result[0]),
                            "tanggal": str(result[1]),
                            "norumah": str(result[2]),
                            "nokk": str(result[3]),
                            "jumlah": str(result[4]),
                            "keterangan": str(result[5]),
                            "dokumen_bayar": str(result[6]),
                            "terverifikasi": str(result[7])
                        },
                        "message": "Pemasukan succesfully retrieved"
                    }
        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500

    def put(self):
        # emp_number = get_raw_jwt()['identity']
        parser = reqparse.RequestParser()
        parser.add_argument(
            'kdpemasukan', help='This field cannot be blank', required=True)
        parser.add_argument(
            'terverifikasi', help='This field cannot be blank', required=True)
        data = parser.parse_args()
        pemasukan = models.Pemasukan()
        try:
            if pemasukan.put(data) == 0:
                return {
                    "message": "Pemasukan not updated, no change found on submitted data or no id found"
                }
            else:
                result = {
                    "message": "Pemasukan succesfully updated"
                }
                return result
        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500

    def delete(self):
        # emp_number = get_raw_jwt()['identity']
        parser = reqparse.RequestParser()
        parser.add_argument(
            'kdpemasukan', help='This field cannot be blank', required=True)
        data = parser.parse_args()
        pemasukan = models.Pemasukan()
        try:
            if pemasukan.delete(data) == 0:
                return {
                    "message": "No kdpemasukan found"
                }, 400
            else:
                result = {
                    "message": "Pemasukan succesfully deleted"
                }
                return result
        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500


class Pengeluaran(Resource):
    def post(self):
        return


class Iuran(Resource):
    def post(self):
        return


class SaldoKas(Resource):
    def post(self):
        return


# class Login(Resource):
#     def post(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument(
#             'username', help='This field cannot be blank', required=True)
#         parser.add_argument(
#             'password', help='This field cannot be blank', required=True)
#         data = parser.parse_args()
#         user = models.User(data["username"], data["password"])
#         try:
#             if user.get() is None:
#                 return {
#                     "message": "Username not found"
#                 }, 400
#             emp_number = user.get()[0]
#             if user.verify_hash() is True:
#                 access_token = create_access_token(identity=emp_number)
#                 return {
#                     'message': 'Logged in as {}'.format(data['username']),
#                     'access_token': access_token
#                 }
#             else:
#                 return {
#                     "message": "Username & password does not match"
#                 }, 400
#         except Exception as e:
#             print(e)
#             return {'message': 'Something went wrong'}, 500


# class PersonalDetail(Resource):
#     @jwt_required
#     def get(self):
#         emp_number = get_raw_jwt()['identity']
#         try:
#             personal_detail = models.PersonalDetail(emp_number)
#             return {
#                 "data": personal_detail.get(),
#                 "message": "Personal detail succesfully retrieved"
#             }
#         except Exception as e:
#             print(e)
#             return {'message': 'Something went wrong'}, 500

#     @jwt_required
#     def put(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument(
#             'first_name', help='This field cannot be blank', required=True)
#         parser.add_argument(
#             'middle_name', help='This field cannot be blank', required=True)
#         parser.add_argument(
#             'last_name', help='This field cannot be blank', required=True)
#         parser.add_argument(
#             'no_ktp', help='This field cannot be blank', required=True)
#         parser.add_argument(
#             'license_expiry_date', help='This field cannot be blank', required=True)
#         parser.add_argument(
#             'no_bpjs_kesehatan', help='This field cannot be blank', required=True)
#         parser.add_argument(
#             'no_npwp', help='This field cannot be blank', required=True)
#         parser.add_argument(
#             'no_bpjs_ketenagakerjaan', help='This field cannot be blank', required=True)
#         parser.add_argument(
#             'work_shift', help='This field cannot be blank', required=True)
#         parser.add_argument(
#             'gender', help='This field cannot be blank', required=True)
#         parser.add_argument(
#             'marital_status', help='This field cannot be blank', required=True)
#         parser.add_argument(
#             'nationality', help='This field cannot be blank', required=True)
#         parser.add_argument(
#             'religion', help='This field cannot be blank', required=True)
#         parser.add_argument(
#             'place_of_birth', help='This field cannot be blank', required=True)
#         data = parser.parse_args()
#         emp_number = get_raw_jwt()['identity']
#         try:
#             personal_detail = models.PersonalDetail(emp_number)
#             if personal_detail.put(data) == 0:
#                 return {
#                     "message": "Personal detail not updated, no change found on submitted data"
#                 }
#             else:
#                 result = {
#                     "message": "Personal detail succesfully updated"
#                 }
#                 return result
#         except Exception as e:
#             print(e)
#             return {'message': 'Something went wrong'}, 500


# class Attachment(Resource):
#     def __init__(self):
#         self.screen = ""

#     @jwt_required
#     def get(self):
#         emp_number = get_raw_jwt()['identity']
#         attachment = models.Attachment(emp_number, self.screen)
#         parser = reqparse.RequestParser()
#         parser.add_argument(
#             'file_id', help='This field cannot be blank', required=True, location=["form", "args"])
#         data = parser.parse_args()
#         try:
#             if data["file_id"] == "all":
#                 result = []
#                 for attachment in attachment.get_meta_all():
#                     result.append(
#                         {
#                             "file_id": str(attachment[1]),
#                             "comment": attachment[2],
#                             "file_name": attachment[3],
#                             "size": str(attachment[4]),
#                             "type": attachment[5],
#                             "date_added": attachment[9]
#                         }
#                     )
#                 return {
#                     "data": result,
#                     "message": "Files succesfully retrieved"
#                 }
#             else:
#                 result = attachment.get(data["file_id"])
#                 if result is None:
#                     return {
#                         "message": "File not found"
#                     }, 400
#                 else:
#                     return {
#                         "data": {
#                             "file_id": result[1],
#                             "file": b64encode(result[5]).decode(),
#                             "comment": result[2],
#                             "file_name": result[3],
#                             "size": result[4],
#                             "type": result[6],
#                             "date_added": result[10]
#                         },
#                         "message": "File succesfully retrieved"
#                     }
#         except Exception as e:
#             print(e)
#             return {'message': 'Something went wrong'}, 500

#     @jwt_required
#     def post(self):
#         emp_number = get_raw_jwt()['identity']
#         parser = reqparse.RequestParser()
#         parser.add_argument(
#             'select_file', help='This field cannot be blank', required=True)
#         parser.add_argument(
#             'file_name', help='This field cannot be blank', required=True)
#         parser.add_argument(
#             'comment', help='This field cannot be blank', required=True)
#         data = parser.parse_args()
#         try:
#             attachment = models.Attachment(emp_number, self.screen)
#             return {
#                 "data": attachment.post(data),
#                 "message": "File succesfully created"
#             }
#         except Exception as e:
#             print(e)
#             return {'message': 'Something went wrong'}, 500

#     @jwt_required
#     def put(self):
#         emp_number = get_raw_jwt()['identity']
#         parser = reqparse.RequestParser()
#         parser.add_argument(
#             'file_id', help='This field cannot be blank', required=True)
#         parser.add_argument(
#             'comment', help='This field cannot be blank', required=True)
#         data = parser.parse_args()
#         attachment = models.Attachment(emp_number, self.screen)
#         try:
#             if attachment.put_comment(data) == 0:
#                 return {
#                     "message": "Comment not updated, no change found on submitted data or no file_id found"
#                 }
#             else:
#                 result = {
#                     "file_id": data['file_id'],
#                     "comment": data['comment'],
#                     "message": "Comment succesfully updated"
#                 }
#                 return result
#         except Exception as e:
#             print(e)
#             return {'message': 'Something went wrong'}, 500

#     @jwt_required
#     def delete(self):
#         emp_number = get_raw_jwt()['identity']
#         parser = reqparse.RequestParser()
#         parser.add_argument(
#             'file_id', help='This field cannot be blank', required=True)
#         data = parser.parse_args()
#         attachment = models.Attachment(emp_number, self.screen)
#         try:
#             if attachment.delete(data['file_id']) == 0:
#                 return {
#                     "message": "No file_id found"
#                 }, 400
#             else:
#                 result = {
#                     "data": {
#                         "file_id": data['file_id']
#                     },
#                     "message": "File succesfully deleted"
#                 }
#                 return result
#         except Exception as e:
#             print(e)
#             return {'message': 'Something went wrong'}, 500


# class PersonalDetailAttachment(Attachment):
#     def __init__(self):
#         self.screen = "personal"


# class Nationality(Resource):
#     def get(self):
#         try:
#             nationality = models.Nationality()
#             result = []
#             for nationality in nationality.get_all():
#                 result.append(
#                     {
#                         "nation_code": str(nationality[0]),
#                         "nation_name": nationality[1]
#                     }
#                 )
#             return {
#                 "data": result,
#                 "message": "Nationality successfully retrieved"
#             }
#         except Exception as e:
#             print(e)
#             return {'message': 'Something went wrong'}, 500


# class WorkShift(Resource):
#     def get(self):
#         try:
#             workshift = models.WorkShift()
#             result = []
#             for workshift in workshift.get_all():
#                 result.append(
#                     {
#                         "workshift_code": str(workshift[0]),
#                         "workshift_name": workshift[1]
#                     }
#                 )
#             return {
#                 "data": result,
#                 "message": "Workshift successfully retrieved"
#             }
#         except Exception as e:
#             print(e)
#             return {'message': 'Something went wrong'}, 500


# class Religion(Resource):
#     def get(self):
#         try:
#             religion = models.Religion()
#             result = []
#             for religion in religion.get_all():
#                 result.append(
#                     {
#                         "religion_code": str(religion[0]),
#                         "religion_name": religion[1]
#                     }
#                 )
#             return {
#                 "data": result,
#                 "message": "Religion successfully retrieved"
#             }
#         except Exception as e:
#             print(e)
#             return {'message': 'Something went wrong'}, 500
