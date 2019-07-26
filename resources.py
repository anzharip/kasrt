from flask_restful import Resource, reqparse
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)
import models
from base64 import b64encode


class Login(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'kdrw', help='This field cannot be blank', required=True)
        parser.add_argument(
            'kdrt', help='This field cannot be blank', required=True)
        parser.add_argument(
            'norumah', help='This field cannot be blank', required=True)
        parser.add_argument(
            'passwd', help='This field cannot be blank', required=True)
        data = parser.parse_args()
        # body = {
        #     "username": data["username"],
        #     "passwd": data["passwd"]
        # }
        user = models.Warga()
        try:
            if user.get(data) is None:
                return {
                    "message": "Username not found"
                }, 400
            norumah = user.get(data)[2]
            if user.verify_hash(data) is True:
                user_claims = {
                    "pengurus": user.get(data)[6]
                }
                access_token = create_access_token(
                    identity=norumah, user_claims=user_claims)
                return {
                    'message': 'Logged in as {}'.format(data['kdrw'], data['kdrt'], data['norumah']),
                    'access_token': access_token
                }
            else:
                return {
                    "message": "Username & password does not match"
                }, 400
        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500


# class RukunTetangga(Resource):
#     # @jwt_required
#     def post(self):
#         # Only allow Pengurus
#         # if get_raw_jwt()['user_claims']['pengurus'] == 0:
#         #     return {
#         #         "message": "You are not authorized to access this endpoint"
#         #     }, 401
#         parser = reqparse.RequestParser()
#         parser.add_argument(
#             'kdrw', help='This field cannot be blank', required=True)
#         parser.add_argument(
#             'nmrt', help='This field cannot be blank', required=True)
#         parser.add_argument(
#             'alamat', help='This field cannot be blank', required=True)
#         data = parser.parse_args()
#         body = {
#             "kdrw": data["kdrw"],
#             "nmrt": data["nmrt"],
#             "alamat": data["alamat"]
#         }
#         try:
#             rt = models.RukunTetangga()
#             rt.post(body)
#             return {
#                 "message": "RT succesfully created"
#             }
#         except Exception as e:
#             print(e)
#             return {'message': 'Something went wrong'}, 500

#     # @jwt_required
#     def get(self):
#         # Only allow Pengurus
#         # if get_raw_jwt()['user_claims']['pengurus'] == 0:
#         #     return {
#         #         "message": "You are not authorized to access this endpoint"
#         #     }, 401
#         rt = models.RukunTetangga()
#         parser = reqparse.RequestParser()
#         parser.add_argument(
#             'nmrt', help='This field cannot be blank', required=True, location=["form", "args"])
#         data = parser.parse_args()
#         try:
#             if data["nmrt"] == "all":
#                 result = []
#                 for rt in rt.get_all():
#                     result.append(
#                         {
#                             "kdrt": str(rt[0]),
#                             "kdrw": str(rt[1]),
#                             "nmrt": str(rt[2]),
#                             "alamat": rt[3]
#                         }
#                     )
#                 return {
#                     "data": result,
#                     "message": "RTs succesfully retrieved"
#                 }
#             else:
#                 body = {
#                     "nmrt": data["nmrt"]
#                 }
#                 result = rt.get(body)
#                 if result is None:
#                     return {
#                         "message": "RT not found"
#                     }, 400
#                 else:
#                     return {
#                         "data": {
#                             "kdrt": str(result[0]),
#                             "kdrw": str(result[1]),
#                             "nmrt": str(result[2]),
#                             "alamat": result[3]
#                         },
#                         "message": "RT succesfully retrieved"
#                     }
#         except Exception as e:
#             print(e)
#             return {'message': 'Something went wrong'}, 500

#     # @jwt_required
#     def put(self):
#         # Only allow Pengurus
#         # if get_raw_jwt()['user_claims']['pengurus'] == 0:
#         #     return {
#         #         "message": "You are not authorized to access this endpoint"
#         #     }, 401
#         parser = reqparse.RequestParser()
#         parser.add_argument(
#             'nmrt', help='This field cannot be blank', required=True)
#         parser.add_argument(
#             'kdrw', help='This field cannot be blank', required=True)
#         parser.add_argument(
#             'alamat', help='This field cannot be blank', required=True)
#         data = parser.parse_args()
#         rt = models.RukunTetangga()
#         body = {
#             "nmrt": data["nmrt"],
#             "kdrw": data["kdrw"],
#             "alamat": data["alamat"]
#         }
#         try:
#             if rt.put(body) == 0:
#                 return {
#                     "message": "RT not updated, no change found on submitted data or no id found"
#                 }
#             else:
#                 result = {
#                     "message": "RT succesfully updated"
#                 }
#                 return result
#         except Exception as e:
#             print(e)
#             return {'message': 'Something went wrong'}, 500

#     # @jwt_required
#     def delete(self):
#         # Only allow Pengurus
#         # if get_raw_jwt()['user_claims']['pengurus'] == 0:
#         #     return {
#         #         "message": "You are not authorized to access this endpoint"
#         #     }, 401
#         parser = reqparse.RequestParser()
#         parser.add_argument(
#             'nmrt', help='This field cannot be blank', required=True)
#         data = parser.parse_args()
#         rt = models.RukunTetangga()
#         try:
#             if rt.delete(data) == 0:
#                 return {
#                     "message": "No nmrt found"
#                 }, 400
#             else:
#                 result = {
#                     "message": "RT succesfully deleted"
#                 }
#                 return result
#         except Exception as e:
#             print(e)
#             return {'message': 'Something went wrong'}, 500


class Warga(Resource):
    # @jwt_required
    def post(self):
        # Only allow Pengurus
        # if get_raw_jwt()['user_claims']['pengurus'] == 0:
        #     return {
        #         "message": "You are not authorized to access this endpoint"
        #     }, 401
        parser = reqparse.RequestParser()
        parser.add_argument(
            'kdrw', help='This field cannot be blank', required=True)
        parser.add_argument(
            'kdrt', help='This field cannot be blank', required=True)
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
            'passwd', help='This field cannot be blank', required=True)
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

    # @jwt_required
    def get(self):
        # Only allow Pengurus
        # if get_raw_jwt()['user_claims']['pengurus'] == 0:
        #     return {
        #         "message": "You are not authorized to access this endpoint"
        #     }, 401
        warga = models.Warga()
        parser = reqparse.RequestParser()
        parser.add_argument(
            'kdrw', help='This field cannot be blank', required=True, location=["form", "args"])
        parser.add_argument(
            'kdrt', help='This field cannot be blank', required=True, location=["form", "args"])
        parser.add_argument(
            'norumah', help='This field cannot be blank', required=True, location=["form", "args"])
        data = parser.parse_args()
        try:
            if data["kdrw"] == "all" and data["kdrt"] == "all" and data["norumah"] == "all":
                result = []
                for warga in warga.get_all():
                    result.append(
                        {
                            "kdrw": str(warga[0]),
                            "kdrt": str(warga[1]),
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
                            "kdrw": str(result[0]),
                            "kdrt": str(result[1]),
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

    # @jwt_required
    def put(self):
        # Only allow Pengurus
        # if get_raw_jwt()['user_claims']['pengurus'] == 0:
        #     return {
        #         "message": "You are not authorized to access this endpoint"
        #     }, 401
        parser = reqparse.RequestParser()
        parser.add_argument(
            'kdrw', help='This field cannot be blank', required=True)
        parser.add_argument(
            'kdrt', help='This field cannot be blank', required=True)
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

    # @jwt_required
    def delete(self):
        # Only allow Pengurus
        # if get_raw_jwt()['user_claims']['pengurus'] == 0:
        #     return {
        #         "message": "You are not authorized to access this endpoint"
        #     }, 401
        parser = reqparse.RequestParser()
        parser.add_argument(
            'kdrw', help='This field cannot be blank', required=True)
        parser.add_argument(
            'kdrt', help='This field cannot be blank', required=True)
        parser.add_argument(
            'norumah', help='This field cannot be blank', required=True)
        data = parser.parse_args()
        warga = models.Warga()
        try:
            if warga.delete(data) == 0:
                return {
                    "message": "No kdrw, kdrt, and norumah found"
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
    # @jwt_required
    def post(self):
        # emp_number = get_raw_jwt()['identity']
        parser = reqparse.RequestParser()
        parser.add_argument(
            'norumah', help='This field cannot be blank', required=True)
        parser.add_argument(
            'kdrw', help='This field cannot be blank', required=True)
        parser.add_argument(
            'kdrt', help='This field cannot be blank', required=True)
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

    # @jwt_required
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
                            "kdrw": str(pemasukan[3]),
                            "kdrt": str(pemasukan[4]),
                            "nokk": str(pemasukan[5]),
                            "jumlah": str(pemasukan[6]),
                            "keterangan": pemasukan[7],
                            "dokumen_bayar": str(pemasukan[8]),
                            "terverifikasi": str(pemasukan[9])
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
                            "kdrw": str(result[3]),
                            "kdrt": str(result[4]),
                            "nokk": str(result[5]),
                            "jumlah": str(result[6]),
                            "keterangan": str(result[7]),
                            "dokumen_bayar": str(result[8]),
                            "terverifikasi": str(result[9])
                        },
                        "message": "Pemasukan succesfully retrieved"
                    }
        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500

    # @jwt_required
    def put(self):
        # Only allow Pengurus
        # if get_raw_jwt()['user_claims']['pengurus'] == 0:
        #     return {
        #         "message": "You are not authorized to access this endpoint"
        #     }, 401
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

    # @jwt_required
    def delete(self):
        # Only allow Pengurus
        # if get_raw_jwt()['user_claims']['pengurus'] == 0:
        #     return {
        #         "message": "You are not authorized to access this endpoint"
        #     }, 401
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
    # @jwt_required
    def post(self):
        # Only allow Pengurus
        # if get_raw_jwt()['user_claims']['pengurus'] == 0:
        #     return {
        #         "message": "You are not authorized to access this endpoint"
        #     }, 401
        parser = reqparse.RequestParser()
        parser.add_argument(
            'jumlah', help='This field cannot be blank', required=True)
        parser.add_argument(
            'keterangan', help='This field cannot be blank', required=True)
        data = parser.parse_args()
        try:
            pengeluaran = models.Pengeluaran()
            pengeluaran.post(data)
            return {
                "message": "Pengeluaran succesfully created"
            }
        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500

    # @jwt_required
    def get(self):
        # Only allow Pengurus
        # if get_raw_jwt()['user_claims']['pengurus'] == 0:
        #     return {
        #         "message": "You are not authorized to access this endpoint"
        #     }, 401
        pengeluaran = models.Pengeluaran()
        parser = reqparse.RequestParser()
        parser.add_argument(
            'kdpengeluaran', help='This field cannot be blank', required=True, location=["form", "args"])
        data = parser.parse_args()
        try:
            if data["kdpengeluaran"] == "all":
                result = []
                for pengeluaran in pengeluaran.get_all():
                    result.append(
                        {
                            "kdpengeluaran": str(pengeluaran[0]),
                            "tanggal": str(pengeluaran[1]),
                            "jumlah": str(pengeluaran[2]),
                            "keterangan": pengeluaran[3]
                        }
                    )
                return {
                    "data": result,
                    "message": "Pengeluaran succesfully retrieved"
                }
            else:
                result = pengeluaran.get(data)
                if result is None:
                    return {
                        "message": "Pengeluaran not found"
                    }, 400
                else:
                    return {
                        "data": {
                            "kdpengeluaran": str(result[0]),
                            "tanggal": str(result[1]),
                            "jumlah": str(result[2]),
                            "keterangan": result[3]
                        },
                        "message": "Pengeluaran succesfully retrieved"
                    }
        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500

    # @jwt_required
    def delete(self):
        # Only allow Pengurus
        # if get_raw_jwt()['user_claims']['pengurus'] == 0:
        #     return {
        #         "message": "You are not authorized to access this endpoint"
        #     }, 401
        parser = reqparse.RequestParser()
        parser.add_argument(
            'kdpengeluaran', help='This field cannot be blank', required=True)
        data = parser.parse_args()
        pengeluaran = models.Pengeluaran()
        try:
            if pengeluaran.delete(data) == 0:
                return {
                    "message": "No kdpengeluaran found"
                }, 400
            else:
                result = {
                    "message": "Pengeluaran succesfully deleted"
                }
                return result
        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500


class Iuran(Resource):
    # @jwt_required
    def post(self):
        # Only allow Pengurus
        # if get_raw_jwt()['user_claims']['pengurus'] == 0:
        #     return {
        #         "message": "You are not authorized to access this endpoint"
        #     }, 401
        parser = reqparse.RequestParser()
        parser.add_argument(
            'tahun', help='This field cannot be blank', required=True)
        parser.add_argument(
            'kdrw', help='This field cannot be blank', required=True)
        parser.add_argument(
            'kdrt', help='This field cannot be blank', required=True)
        parser.add_argument(
            'norumah', help='This field cannot be blank', required=True)
        parser.add_argument(
            'jan', help='This field cannot be blank', required=True)
        parser.add_argument(
            'feb', help='This field cannot be blank', required=True)
        parser.add_argument(
            'mar', help='This field cannot be blank', required=True)
        parser.add_argument(
            'apr', help='This field cannot be blank', required=True)
        parser.add_argument(
            'may', help='This field cannot be blank', required=True)
        parser.add_argument(
            'jun', help='This field cannot be blank', required=True)
        parser.add_argument(
            'jul', help='This field cannot be blank', required=True)
        parser.add_argument(
            'aug', help='This field cannot be blank', required=True)
        parser.add_argument(
            'sep', help='This field cannot be blank', required=True)
        parser.add_argument(
            'oct', help='This field cannot be blank', required=True)
        parser.add_argument(
            'nop', help='This field cannot be blank', required=True)
        parser.add_argument(
            'des', help='This field cannot be blank', required=True)
        data = parser.parse_args()
        try:
            iuran = models.Iuran()
            iuran.post(data)
            return {
                "message": "Iuran succesfully created"
            }
        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500

    # @jwt_required
    def get(self):
        # Only allow Pengurus
        # if get_raw_jwt()['user_claims']['pengurus'] == 0:
        #     return {
        #         "message": "You are not authorized to access this endpoint"
        #     }, 401
        iuran = models.Iuran()
        parser = reqparse.RequestParser()
        parser.add_argument(
            'kdiuran', help='This field cannot be blank', required=True, location=["form", "args"])
        data = parser.parse_args()
        try:
            if data["kdiuran"] == "all":
                result = []
                for iuran in iuran.get_all():
                    result.append(
                        {
                            "tahun": str(iuran[0]),
                            "kdrw": str(iuran[1]),
                            "kdrt": str(iuran[2]),
                            "norumah": str(iuran[3]),
                            "jan": str(iuran[4]),
                            "feb": str(iuran[5]),
                            "mar": str(iuran[6]),
                            "apr": str(iuran[7]),
                            "may": str(iuran[8]),
                            "jun": str(iuran[9]),
                            "jul": str(iuran[10]),
                            "aug": str(iuran[11]),
                            "sep": str(iuran[12]),
                            "oct": str(iuran[13]),
                            "nop": str(iuran[14]),
                            "dec": str(iuran[15]),
                        }
                    )
                return {
                    "data": result,
                    "message": "Iuran succesfully retrieved"
                }
            else:
                result = iuran.get(data)
                if result is None:
                    return {
                        "message": "Iuran not found"
                    }, 400
                else:
                    return {
                        "data": {
                            "tahun": str(result[0]),
                            "kdrw": str(result[1]),
                            "kdrt": str(result[2]),
                            "norumah": str(result[3]),
                            "jan": str(result[4]),
                            "feb": str(result[5]),
                            "mar": str(result[6]),
                            "apr": str(result[7]),
                            "may": str(result[8]),
                            "jun": str(result[9]),
                            "jul": str(result[10]),
                            "aug": str(result[11]),
                            "sep": str(result[12]),
                            "oct": str(result[13]),
                            "nop": str(result[14]),
                            "dec": str(result[15]),
                        },
                        "message": "Iuran succesfully retrieved"
                    }
        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500

    # @jwt_required
    def delete(self):
        # Only allow Pengurus
        # if get_raw_jwt()['user_claims']['pengurus'] == 0:
        #     return {
        #         "message": "You are not authorized to access this endpoint"
        #     }, 401
        parser = reqparse.RequestParser()
        parser.add_argument(
            'tahun', help='This field cannot be blank', required=True)
        parser.add_argument(
            'kdrw', help='This field cannot be blank', required=True)
        parser.add_argument(
            'kdrt', help='This field cannot be blank', required=True)
        parser.add_argument(
            'norumah', help='This field cannot be blank', required=True)
        data = parser.parse_args()
        iuran = models.Iuran()
        try:
            if iuran.delete(data) == 0:
                return {
                    "message": "No kdiuran found"
                }, 400
            else:
                result = {
                    "message": "Iuran succesfully deleted"
                }
                return result
        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500


class SaldoKas(Resource):
    # @jwt_required
    def post(self):
        # Only allow Pengurus
        # if get_raw_jwt()['user_claims']['pengurus'] == 0:
        #     return {
        #         "message": "You are not authorized to access this endpoint"
        #     }, 401
        parser = reqparse.RequestParser()
        parser.add_argument(
            'tahunbulan', help='This field cannot be blank', required=True)
        data = parser.parse_args()
        try:
            saldokas = models.SaldoKas()
            bulandict = {
                "01": "jan",
                "02": "feb",
                "03": "mar",
                "04": "apr",
                "05": "mei",
                "06": "jun",
                "07": "jul",
                "08": "agu",
                "09": "sep",
                "10": "okt",
                "11": "nov",
                "12": "des",
            }
            tahun = data["tahunbulan"].split("-")[0]
            bulan = bulandict[data["tahunbulan"].split("-")[1]]
            if saldokas.get_total_pemasukan(data)[0] is None:
                total_pemasukan = 0
            else:
                total_pemasukan = int(saldokas.get_total_pemasukan(data)[0])
            if saldokas.get_total_pengeluaran(data)[0] is None:
                total_pengeluaran = 0
            else:
                total_pengeluaran = int(
                    saldokas.get_total_pengeluaran(data)[0])
            body = {
                "tahun": tahun,
                "bulan": bulan,
                "masuk": total_pemasukan,
                "keluar": total_pengeluaran,
                "saldoakhir": (total_pemasukan - total_pengeluaran)
            }
            saldokas.post(body)
            return {
                "message": "SaldoKas succesfully created"
            }
        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500

    # @jwt_required
    def get(self):
        # Only allow Pengurus
        # if get_raw_jwt()['user_claims']['pengurus'] == 0:
        #     return {
        #         "message": "You are not authorized to access this endpoint"
        #     }, 401
        saldokas = models.SaldoKas()
        parser = reqparse.RequestParser()
        parser.add_argument(
            'kdsaldo', help='This field cannot be blank', required=True, location=["form", "args"])
        data = parser.parse_args()
        try:
            if data["kdsaldo"] == "all":
                result = []
                for saldokas in saldokas.get_all():
                    result.append(
                        {
                            "kdsaldo": str(saldokas[0]),
                            "tahun": str(saldokas[1]),
                            "bulan": saldokas[2],
                            "masuk": str(saldokas[3]),
                            "keluar": str(saldokas[4]),
                            "saldoakhir": str(saldokas[5])
                        }
                    )
                return {
                    "data": result,
                    "message": "Saldo Kas succesfully retrieved"
                }
            else:
                result = saldokas.get(data)
                if result is None:
                    return {
                        "message": "Saldo Kas not found"
                    }, 400
                else:
                    return {
                        "data": {
                            "kdsaldo": str(result[0]),
                            "tahun": str(result[1]),
                            "bulan": result[2],
                            "masuk": str(result[3]),
                            "keluar": str(result[4]),
                            "saldoakhir": str(result[5])
                        },
                        "message": "Saldo Kas succesfully retrieved"
                    }
        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500

    # @jwt_required
    def delete(self):
        # Only allow Pengurus
        # if get_raw_jwt()['user_claims']['pengurus'] == 0:
        #     return {
        #         "message": "You are not authorized to access this endpoint"
        #     }, 401
        parser = reqparse.RequestParser()
        parser.add_argument(
            'kdsaldo', help='This field cannot be blank', required=True)
        data = parser.parse_args()
        saldokas = models.SaldoKas()
        try:
            if saldokas.delete(data) == 0:
                return {
                    "message": "No kdsaldo found"
                }, 400
            else:
                result = {
                    "message": "Saldo Kas succesfully deleted"
                }
                return result
        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500
