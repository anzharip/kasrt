import db
import bcrypt
from time import time
from mimetypes import guess_type
from base64 import b64decode
import datetime


class Warga:

    def get(self, body):
        kdrw = body["username"][0:2]
        kdrt = body["username"][2:4]
        norumah = body["username"][4:]
        field = "`kdrw`, `kdrt`, `norumah`, `nokk`, `nmkk`, `statustinggal`, `pengurus`"
        table = "`tbl_warga`"
        sql_filter = "`kdrw` = '%s' AND `kdrt` = '%s' AND `norumah` = '%s'" % (kdrw, kdrt, norumah)
        statement = "SELECT %s FROM %s WHERE %s LIMIT 0,1" % (
            field, table, sql_filter)
        connection = db.open_connection()
        cursor = db.sql_cursor(connection, statement)
        result = cursor.fetchone()
        db.close_connection(connection, cursor)
        return result

    def get_all(self):
        field = "`kdrw`, `kdrt`, `norumah`, `nokk`, `nmkk`, `statustinggal`, `pengurus`"
        table = "`tbl_warga`"
        statement = "SELECT %s FROM %s LIMIT 0,1000" % (
            field, table)
        connection = db.open_connection()
        cursor = db.sql_cursor(connection, statement)
        result = cursor.fetchall()
        db.close_connection(connection, cursor)
        return result

    def verify_hash(self, body):
        kdrw = body["username"][0:2]
        kdrt = body["username"][2:4]
        norumah = body["username"][4:]
        field = "`kdrw`, `kdrt`, `norumah`, `passwd`"
        table = "`tbl_warga`"
        sql_filter = "`kdrw` = '%s' AND `kdrt` = '%s' AND `norumah` = '%s'" % (kdrw, kdrt, norumah)
        statement = "SELECT %s FROM %s WHERE %s LIMIT 0,1" % (
            field, table, sql_filter)
        connection = db.open_connection()
        cursor = db.sql_cursor(connection, statement)
        result = cursor.fetchone()
        db.close_connection(connection, cursor)
        bytes_password = bytes(body["password"], "utf-8")
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
        field = "`nmrt`='%s', `nokk`='%s', `nmkk`='%s', `statustinggal`='%s', `pengurus`='%s'" % (
            body['nmrt'], body['nokk'], body['nmkk'], body['statustinggal'], body['pengurus'])
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


class RukunTetangga:
    def get(self, body):
        field = "`kdrt`, `nmrt`, `kdrw`, `alamat`"
        table = "`rt`"
        sql_filter = "`nmrt` = '%s'" % body["nmrt"]
        statement = "SELECT %s FROM %s WHERE %s LIMIT 0,1" % (
            field, table, sql_filter)
        connection = db.open_connection()
        cursor = db.sql_cursor(connection, statement)
        result = cursor.fetchone()
        db.close_connection(connection, cursor)
        return result

    def get_all(self):
        field = "`kdrt`, `kdrw`, `nmrt`, `alamat`"
        table = "`rt`"
        statement = "SELECT %s FROM %s LIMIT 0,1000" % (
            field, table)
        connection = db.open_connection()
        cursor = db.sql_cursor(connection, statement)
        result = cursor.fetchall()
        db.close_connection(connection, cursor)
        return result

    def post(self, body):
        field = "(`kdrw`, `nmrt`, `alamat`)"
        values = "('%s', '%s', '%s')" % (
            body["kdrw"], body["nmrt"], body["alamat"])
        table = "`rt`"
        statement = "INSERT INTO %s %s VALUES %s" % (
            table, field, values)
        connection = db.open_connection()
        cursor = db.sql_cursor(connection, statement)
        connection.commit()
        db.close_connection(connection, cursor)
        result = cursor.rowcount
        return result

    def put(self, body):
        field = "`kdrw`='%s', `alamat`='%s'" % (
            body['kdrw'], body['alamat'])
        table = "`rt`"
        sql_filter = "`nmrt`='%s'" % (body['nmrt'])
        statement = "UPDATE %s SET %s WHERE %s" % (
            table, field, sql_filter)
        connection = db.open_connection()
        cursor = db.sql_cursor(connection, statement)
        connection.commit()
        db.close_connection(connection, cursor)
        return cursor.rowcount

    def delete(self, body):
        table = "`rt`"
        sql_filter = "`nmrt` = %s" % (body["nmrt"])
        statement = "DELETE FROM %s WHERE %s" % (
            table, sql_filter)
        connection = db.open_connection()
        cursor = db.sql_cursor(connection, statement)
        connection.commit()
        db.close_connection(connection, cursor)
        return cursor.rowcount


class Pemasukan:
    def get(self, body):
        field = "`kdpemasukan`, `tanggal`, `norumah`, `nokk`, `jumlah`, `keterangan`, `dokumen_bayar`, `terverifikasi`"
        table = "`tr_pemasukan`"
        sql_filter = "`kdpemasukan` = '%s'" % body["kdpemasukan"]
        statement = "SELECT %s FROM %s WHERE %s LIMIT 0,1" % (
            field, table, sql_filter)
        connection = db.open_connection()
        cursor = db.sql_cursor(connection, statement)
        result = cursor.fetchone()
        db.close_connection(connection, cursor)
        return result

    def get_all(self):
        field = "`kdpemasukan`, `tanggal`, `norumah`, `nokk`, `jumlah`, `keterangan`, `dokumen_bayar`, `terverifikasi`"
        table = "`tr_pemasukan`"
        statement = "SELECT %s FROM %s LIMIT 0,1000" % (
            field, table)
        connection = db.open_connection()
        cursor = db.sql_cursor(connection, statement)
        result = cursor.fetchall()
        db.close_connection(connection, cursor)
        return result

    def post(self, body):
        field = "(`norumah`, `nokk`, `jumlah`, `keterangan`, `dokumen_bayar`)"
        values = "('%s', '%s', '%s', '%s', '%s')" % (
            body["norumah"], body["nokk"], body["jumlah"], body["keterangan"], body["dokumen_bayar"],)
        table = "`tr_pemasukan`"
        statement = "INSERT INTO %s %s VALUES %s" % (
            table, field, values)
        connection = db.open_connection()
        cursor = db.sql_cursor(connection, statement)
        connection.commit()
        db.close_connection(connection, cursor)
        result = cursor.rowcount
        return result

    def put(self, body):
        field = "`terverifikasi`='%s'" % (
            body['terverifikasi'])
        table = "`tr_pemasukan`"
        sql_filter = "`kdpemasukan`='%s'" % (body['kdpemasukan'])
        statement = "UPDATE %s SET %s WHERE %s" % (
            table, field, sql_filter)
        connection = db.open_connection()
        cursor = db.sql_cursor(connection, statement)
        connection.commit()
        db.close_connection(connection, cursor)
        return cursor.rowcount

    def delete(self, body):
        table = "`tr_pemasukan`"
        sql_filter = "`kdpemasukan` = %s" % (body["kdpemasukan"])
        statement = "DELETE FROM %s WHERE %s" % (
            table, sql_filter)
        connection = db.open_connection()
        cursor = db.sql_cursor(connection, statement)
        connection.commit()
        db.close_connection(connection, cursor)
        return cursor.rowcount


class Pengeluaran:
    def get(self, body):
        field = "`kdpengeluaran`, `tanggal`, `jumlah`, `keterangan`"
        table = "`tr_pengeluaran`"
        sql_filter = "`kdpengeluaran` = '%s'" % body["kdpengeluaran"]
        statement = "SELECT %s FROM %s WHERE %s LIMIT 0,1" % (
            field, table, sql_filter)
        connection = db.open_connection()
        cursor = db.sql_cursor(connection, statement)
        result = cursor.fetchone()
        db.close_connection(connection, cursor)
        return result

    def get_all(self):
        field = "`kdpengeluaran`, `tanggal`, `jumlah`, `keterangan`"
        table = "`tr_pengeluaran`"
        statement = "SELECT %s FROM %s LIMIT 0,1000" % (
            field, table)
        connection = db.open_connection()
        cursor = db.sql_cursor(connection, statement)
        result = cursor.fetchall()
        db.close_connection(connection, cursor)
        return result

    def post(self, body):
        field = "(`jumlah`, `keterangan`)"
        values = "('%s', '%s')" % (
            body["jumlah"], body["keterangan"])
        table = "`tr_pengeluaran`"
        statement = "INSERT INTO %s %s VALUES %s" % (
            table, field, values)
        connection = db.open_connection()
        cursor = db.sql_cursor(connection, statement)
        connection.commit()
        db.close_connection(connection, cursor)
        result = cursor.rowcount
        return result

    def delete(self, body):
        table = "`tr_pengeluaran`"
        sql_filter = "`kdpengeluaran` = %s" % (body["kdpengeluaran"])
        statement = "DELETE FROM %s WHERE %s" % (
            table, sql_filter)
        connection = db.open_connection()
        cursor = db.sql_cursor(connection, statement)
        connection.commit()
        db.close_connection(connection, cursor)
        return cursor.rowcount


class Iuran:
    def get(self, body):
        field = "`kdiuran`, `tahun`, `bulan`, `norumah`"
        table = "`tr_iuran`"
        sql_filter = "`kdiuran` = '%s'" % body["kdiuran"]
        statement = "SELECT %s FROM %s WHERE %s LIMIT 0,1" % (
            field, table, sql_filter)
        connection = db.open_connection()
        cursor = db.sql_cursor(connection, statement)
        result = cursor.fetchone()
        db.close_connection(connection, cursor)
        return result

    def get_all(self):
        field = "`kdiuran`, `tahun`, `bulan`, `norumah`"
        table = "`tr_iuran`"
        statement = "SELECT %s FROM %s LIMIT 0,1000" % (
            field, table)
        connection = db.open_connection()
        cursor = db.sql_cursor(connection, statement)
        result = cursor.fetchall()
        db.close_connection(connection, cursor)
        return result

    def post(self, body):
        field = "(`tahun`, `bulan`, `norumah`)"
        values = "('%s', '%s', '%s')" % (
            body["tahun"], body["bulan"], body["norumah"])
        table = "`tr_iuran`"
        statement = "INSERT INTO %s %s VALUES %s" % (
            table, field, values)
        connection = db.open_connection()
        cursor = db.sql_cursor(connection, statement)
        connection.commit()
        db.close_connection(connection, cursor)
        result = cursor.rowcount
        return result

    def delete(self, body):
        table = "`tr_iuran`"
        sql_filter = "`kdiuran` = %s" % (body["kdiuran"])
        statement = "DELETE FROM %s WHERE %s" % (
            table, sql_filter)
        connection = db.open_connection()
        cursor = db.sql_cursor(connection, statement)
        connection.commit()
        db.close_connection(connection, cursor)
        return cursor.rowcount


class SaldoKas:
    def get(self, body):
        field = "`kdsaldo`, `tahun`, `bulan`, `masuk`, `keluar`, `saldoakhir`"
        table = "`saldokas`"
        sql_filter = "`kdsaldo` = '%s'" % body["kdsaldo"]
        statement = "SELECT %s FROM %s WHERE %s LIMIT 0,1" % (
            field, table, sql_filter)
        connection = db.open_connection()
        cursor = db.sql_cursor(connection, statement)
        result = cursor.fetchone()
        db.close_connection(connection, cursor)
        return result

    def get_all(self):
        field = "`kdsaldo`, `tahun`,`bulan`, `masuk`, `keluar`, `saldoakhir`"
        table = "`saldokas`"
        statement = "SELECT %s FROM %s LIMIT 0,1000" % (
            field, table)
        connection = db.open_connection()
        cursor = db.sql_cursor(connection, statement)
        result = cursor.fetchall()
        db.close_connection(connection, cursor)
        return result

    def get_total_pemasukan(self, body):
        # SELECT FORMAT(SUM(`jumlah`),1) AS total_pemasukan FROM `kasrt`.`tr_pemasukan` WHERE `terverifikasi`=1 AND `tanggal`>='2019-07-01' AND `tanggal`<='2019-07-31' LIMIT 0,1000
        field = "SUM(`jumlah`) AS total_pemasukan"
        table = "`tr_pemasukan`"
        sql_filter = "`terverifikasi`=1 AND `tanggal`>='%s-01' AND `tanggal`<='%s-31'" % (
            body["tahunbulan"], body["tahunbulan"])
        statement = "SELECT %s FROM %s WHERE %s LIMIT 0,1" % (
            field, table, sql_filter)
        connection = db.open_connection()
        cursor = db.sql_cursor(connection, statement)
        result = cursor.fetchone()
        db.close_connection(connection, cursor)
        return result

    def get_total_pengeluaran(self, body):
        # SELECT FORMAT(SUM(`jumlah`),1) AS total_pengeluaran FROM `kasrt`.`tr_pengeluaran` WHERE `tanggal`>='2019-07-01' AND `tanggal`<='2019-07-31' LIMIT 0,1000
        field = "SUM(`jumlah`) AS total_pengeluaran"
        table = "`tr_pengeluaran`"
        sql_filter = "`tanggal`>='%s-01' AND `tanggal`<='%s-31'" % (
            body["tahunbulan"], body["tahunbulan"])
        statement = "SELECT %s FROM %s WHERE %s LIMIT 0,1" % (
            field, table, sql_filter)
        connection = db.open_connection()
        cursor = db.sql_cursor(connection, statement)
        result = cursor.fetchone()
        db.close_connection(connection, cursor)
        return result

    def post(self, body):
        field = "(`tahun`,`bulan`, `masuk`, `keluar`, `saldoakhir`)"
        values = "('%s', '%s', '%s', '%s', '%s')" % (
            body["tahun"], body["bulan"], body["masuk"], body["keluar"], body["saldoakhir"])
        table = "`saldokas`"
        statement = "INSERT INTO %s %s VALUES %s" % (
            table, field, values)
        connection = db.open_connection()
        cursor = db.sql_cursor(connection, statement)
        connection.commit()
        db.close_connection(connection, cursor)
        result = cursor.rowcount
        return result

    def delete(self, body):
        table = "`saldokas`"
        sql_filter = "`kdsaldo` = %s" % (body["kdsaldo"])
        statement = "DELETE FROM %s WHERE %s" % (
            table, sql_filter)
        connection = db.open_connection()
        cursor = db.sql_cursor(connection, statement)
        connection.commit()
        db.close_connection(connection, cursor)
        return cursor.rowcount
