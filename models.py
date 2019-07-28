import db
import bcrypt
from time import time
from mimetypes import guess_type
from base64 import b64decode
import datetime


class Warga:

    def get(self, body):
        field = "`kdrw`, `kdrt`, `norumah`, `nokk`, `nmkk`, `statustinggal`, `pengurus`"
        table = "`tbl_warga`"
        sql_filter = "`kdrw` = '%s' AND `kdrt` = '%s' AND `norumah` = '%s'" % (
            body["kdrw"], body["kdrt"], body["norumah"])
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
        # kdrw = body["username"][0:2]
        # kdrt = body["username"][2:4]
        # norumah = body["username"][4:]
        field = "`kdrw`, `kdrt`, `norumah`, `passwd`"
        table = "`tbl_warga`"
        sql_filter = "`kdrw` = '%s' AND `kdrt` = '%s' AND `norumah` = '%s'" % (
            body["kdrw"], body["kdrt"], body["norumah"])
        statement = "SELECT %s FROM %s WHERE %s LIMIT 0,1" % (
            field, table, sql_filter)
        connection = db.open_connection()
        cursor = db.sql_cursor(connection, statement)
        result = cursor.fetchone()
        db.close_connection(connection, cursor)
        bytes_password = bytes(body["passwd"], "utf-8")
        bytes_hashed = bytes(result[3], "utf-8")
        return bcrypt.checkpw(bytes_password, bytes_hashed)

    def post(self, body):
        password_hashed = bcrypt.hashpw(
            bytes(body["passwd"], "utf-8"), bcrypt.gensalt())
        field = "(`kdrw`, `kdrt`, `norumah`, `nokk`, `nmkk`, `statustinggal`, `pengurus`, `passwd`)"
        values = "('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
            body["kdrw"], body["kdrt"], body["norumah"], body["nokk"], body["nmkk"], body["statustinggal"], body["pengurus"], password_hashed.decode("utf-8"))
        table = "`tbl_warga`"
        statement = "INSERT INTO %s %s VALUES %s" % (
            table, field, values)
        connection = db.open_connection()
        cursor = db.sql_cursor(connection, statement)
        connection.commit()
        db.close_connection(connection, cursor)
        result = cursor.rowcount
        return result

    def put(self, body):
        field = "`nokk`='%s', `nmkk`='%s', `statustinggal`='%s', `pengurus`='%s'" % (
            body['nokk'], body['nmkk'], body['statustinggal'], body['pengurus'])
        table = "`tbl_warga`"
        sql_filter = "`kdrw` = '%s' AND `kdrt` = '%s' AND `norumah` = '%s'" % (
            body['kdrw'], body['kdrt'], body['norumah'])
        statement = "UPDATE %s SET %s WHERE %s" % (
            table, field, sql_filter)
        connection = db.open_connection()
        cursor = db.sql_cursor(connection, statement)
        connection.commit()
        db.close_connection(connection, cursor)
        return cursor.rowcount

    def put_password(self, body):
        password_hashed = bcrypt.hashpw(
            bytes(body["passwd"], "utf-8"), bcrypt.gensalt())
        field = "`passwd`='%s'" % (password_hashed.decode("utf-8"))
        table = "`tbl_warga`"
        sql_filter = "`kdrw` = '%s' AND `kdrt` = '%s' AND `norumah` = '%s'" % (
            body['kdrw'], body['kdrt'], body['norumah'])
        statement = "UPDATE %s SET %s WHERE %s" % (
            table, field, sql_filter)
        connection = db.open_connection()
        cursor = db.sql_cursor(connection, statement)
        connection.commit()
        db.close_connection(connection, cursor)
        return cursor.rowcount

    def delete(self, body):
        table = "`tbl_warga`"
        sql_filter = "`kdrw` = '%s' AND `kdrt` = '%s' AND `norumah` = '%s'" % (
            body['kdrw'], body['kdrt'], body['norumah'])
        statement = "DELETE FROM %s WHERE %s" % (
            table, sql_filter)
        connection = db.open_connection()
        cursor = db.sql_cursor(connection, statement)
        connection.commit()
        db.close_connection(connection, cursor)
        return cursor.rowcount


class Pemasukan:
    def get(self, body):
        field = "`kdpemasukan`, `tanggal`, `norumah`, `kdrw`, `kdrt`, `nokk`, `jumlah`, `keterangan`, `dokumen_bayar`, `terverifikasi`"
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
        field = "`kdpemasukan`, `tanggal`, `norumah`, `kdrw`, `kdrt`, `nokk`, `jumlah`, `keterangan`, `dokumen_bayar`, `terverifikasi`"
        table = "`tr_pemasukan`"
        statement = "SELECT %s FROM %s LIMIT 0,1000" % (
            field, table)
        connection = db.open_connection()
        cursor = db.sql_cursor(connection, statement)
        result = cursor.fetchall()
        db.close_connection(connection, cursor)
        return result

    def post(self, body):
        field = "(`norumah`, `kdrw`, `kdrt`, `nokk`, `jumlah`, `keterangan`, `dokumen_bayar`)"
        values = "('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
            body["norumah"], body["kdrw"], body["kdrt"], body["nokk"], body["jumlah"], body["keterangan"], body["dokumen_bayar"],)
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
        field = "`tahun`, `kdrw`, `kdrt`, `norumah`, `jan`, `feb`, `mar`, `apr`, `may`, `jun`, `jul`, `aug`, `sep`, `oct`, `nop`, `des`"
        table = "`tr_iuran`"
        sql_filter = "`tahun` = '%s' AND `kdrw` = '%s' AND `kdrt` = '%s' AND `norumah` = '%s'" % (
            body["tahun"], body["kdrw"], body["kdrt"], body["norumah"])
        statement = "SELECT %s FROM %s WHERE %s LIMIT 0,1" % (
            field, table, sql_filter)
        connection = db.open_connection()
        cursor = db.sql_cursor(connection, statement)
        result = cursor.fetchone()
        db.close_connection(connection, cursor)
        return result

    def get_all(self):
        field = "`tahun`, `kdrw`, `kdrt`, `norumah`, `jan`, `feb`, `mar`, `apr`, `may`, `jun`, `jul`, `aug`, `sep`, `oct`, `nop`, `des`"
        table = "`tr_iuran`"
        statement = "SELECT %s FROM %s LIMIT 0,1000" % (
            field, table)
        connection = db.open_connection()
        cursor = db.sql_cursor(connection, statement)
        result = cursor.fetchall()
        db.close_connection(connection, cursor)
        return result

    def post(self, body):
        field = "(`tahun`, `kdrw`, `kdrt`, `norumah`, `jan`, `feb`, `mar`, `apr`, `may`, `jun`, `jul`, `aug`, `sep`, `oct`, `nop`, `des`)"
        values = "('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
            body["tahun"], body["kdrw"], body["kdrt"], body["norumah"], body["jan"], body["feb"], body["mar"], body["apr"], body["may"], body["jun"], body["jul"], body["aug"], body["sep"], body["oct"], body["nop"], body["des"])
        table = "`tr_iuran`"
        statement = "INSERT INTO %s %s VALUES %s" % (
            table, field, values)
        connection = db.open_connection()
        cursor = db.sql_cursor(connection, statement)
        connection.commit()
        db.close_connection(connection, cursor)
        result = cursor.rowcount
        return result

    def put(self, body):
        field = "`jan` = %s, `feb` = %s, `mar` = %s, `apr` = %s, `may` = %s, `jun` = %s, `jul` = %s, `aug` = %s, `sep` = %s, `oct` = %s, `nop` = %s, `des` = %s" % (
            body['jan'], body['feb'], body['mar'], body['apr'], body['may'], body['jun'], body['jul'], body['aug'], body['sep'], body['oct'], body['nop'], body['des'])
        table = "`tr_iuran`"
        sql_filter = "`tahun` = '%s' AND `kdrw` = '%s' AND `kdrt` = '%s' AND `norumah` = '%s'" % (
            body["tahun"], body["kdrw"], body["kdrt"], body["norumah"])
        statement = "UPDATE %s SET %s WHERE %s" % (
            table, field, sql_filter)
        connection = db.open_connection()
        cursor = db.sql_cursor(connection, statement)
        connection.commit()
        db.close_connection(connection, cursor)
        return cursor.rowcount

    def delete(self, body):
        table = "`tr_iuran`"
        sql_filter = "`tahun` = '%s' AND `kdrw` = '%s' AND `kdrt` = '%s' AND `norumah` = '%s'" % (
            body["tahun"], body["kdrw"], body["kdrt"], body["norumah"])
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
