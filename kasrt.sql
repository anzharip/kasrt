/*
 Navicat Premium Data Transfer

 Source Server         : ublta-hrmipnet
 Source Server Type    : MariaDB
 Source Server Version : 100314
 Source Host           : localhost:32768
 Source Schema         : kasrt

 Target Server Type    : MariaDB
 Target Server Version : 100314
 File Encoding         : 65001

 Date: 16/07/2019 11:21:13
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for rt
-- ----------------------------
DROP TABLE IF EXISTS `rt`;
CREATE TABLE `rt` (
  `kdrt` int(11) NOT NULL AUTO_INCREMENT,
  `kdrw` int(10) NOT NULL DEFAULT 1,
  `nmrt` int(10) NOT NULL,
  `alamat` varchar(255) NOT NULL,
  PRIMARY KEY (`kdrt`) USING BTREE,
  UNIQUE KEY `nmrt` (`nmrt`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of rt
-- ----------------------------
BEGIN;
INSERT INTO `rt` VALUES (4, 1, 1, 'Kemayoran');
INSERT INTO `rt` VALUES (5, 1, 2, 'Kemayoran');
INSERT INTO `rt` VALUES (6, 1, 3, 'Kemayoran');
INSERT INTO `rt` VALUES (7, 1, 4, 'Kemayoran');
INSERT INTO `rt` VALUES (8, 1, 5, 'Kemayoran');
COMMIT;

-- ----------------------------
-- Table structure for saldokas
-- ----------------------------
DROP TABLE IF EXISTS `saldokas`;
CREATE TABLE `saldokas` (
  `kdsaldo` int(11) NOT NULL AUTO_INCREMENT,
  `tahun` year(4) NOT NULL,
  `bulan` enum('jan','feb','mar','apr','mei','jun','jul','agu','sep','okt','nov','des') NOT NULL,
  `masuk` int(10) DEFAULT NULL,
  `keluar` int(10) DEFAULT NULL,
  `saldoakhir` int(10) DEFAULT NULL,
  PRIMARY KEY (`kdsaldo`) USING BTREE,
  UNIQUE KEY `saldokas_index1` (`tahun`,`bulan`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of saldokas
-- ----------------------------
BEGIN;
INSERT INTO `saldokas` VALUES (3, 2019, 'jul', 900000, 400000, 500000);
COMMIT;

-- ----------------------------
-- Table structure for tr_iuran
-- ----------------------------
DROP TABLE IF EXISTS `tr_iuran`;
CREATE TABLE `tr_iuran` (
  `kdiuran` int(11) NOT NULL AUTO_INCREMENT,
  `tahun` year(4) NOT NULL,
  `bulan` enum('jan','feb','mar','apr','mei','jun','jul','agu','sep','okt','nov','des') NOT NULL,
  `norumah` int(10) NOT NULL,
  PRIMARY KEY (`kdiuran`) USING BTREE,
  UNIQUE KEY `tr_iuran_index1` (`tahun`,`bulan`,`norumah`) USING BTREE,
  KEY `norumah` (`norumah`),
  CONSTRAINT `tr_iuran_fk1` FOREIGN KEY (`norumah`) REFERENCES `warga` (`norumah`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tr_iuran
-- ----------------------------
BEGIN;
INSERT INTO `tr_iuran` VALUES (3, 2019, 'jan', 12);
INSERT INTO `tr_iuran` VALUES (4, 2019, 'jun', 11);
INSERT INTO `tr_iuran` VALUES (9, 2019, 'jun', 12);
COMMIT;

-- ----------------------------
-- Table structure for tr_pemasukan
-- ----------------------------
DROP TABLE IF EXISTS `tr_pemasukan`;
CREATE TABLE `tr_pemasukan` (
  `kdpemasukan` int(11) NOT NULL AUTO_INCREMENT,
  `tanggal` datetime DEFAULT current_timestamp(),
  `norumah` int(10) DEFAULT NULL,
  `nokk` varchar(255) DEFAULT NULL,
  `jumlah` int(10) DEFAULT NULL,
  `keterangan` varchar(255) DEFAULT NULL,
  `dokumen_bayar` blob DEFAULT NULL,
  `terverifikasi` tinyint(1) DEFAULT 0,
  PRIMARY KEY (`kdpemasukan`),
  KEY `tr_pemasukan_fk2` (`nokk`),
  KEY `tr_pemasukan_fk1` (`norumah`,`nokk`),
  CONSTRAINT `tr_pemasukan_fk1` FOREIGN KEY (`norumah`, `nokk`) REFERENCES `warga` (`norumah`, `nokk`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tr_pemasukan
-- ----------------------------
BEGIN;
INSERT INTO `tr_pemasukan` VALUES (5, '2019-07-02 11:59:12', 11, '0001', 100000, NULL, NULL, 0);
INSERT INTO `tr_pemasukan` VALUES (6, '2019-07-04 11:59:37', 12, '0002', 200000, NULL, NULL, 0);
INSERT INTO `tr_pemasukan` VALUES (7, '2019-07-01 12:00:02', 13, '0003', 300000, NULL, NULL, 1);
INSERT INTO `tr_pemasukan` VALUES (8, '2019-07-01 12:00:15', 14, '0004', 400000, NULL, NULL, 1);
INSERT INTO `tr_pemasukan` VALUES (12, '2019-07-14 07:01:02', 11, '0001', 200000, 'something', '', 0);
INSERT INTO `tr_pemasukan` VALUES (14, '2019-07-14 07:01:09', 11, '0001', 200000, 'something', '', 1);
COMMIT;

-- ----------------------------
-- Table structure for tr_pengeluaran
-- ----------------------------
DROP TABLE IF EXISTS `tr_pengeluaran`;
CREATE TABLE `tr_pengeluaran` (
  `kdpengeluaran` int(11) NOT NULL AUTO_INCREMENT,
  `tanggal` datetime DEFAULT current_timestamp(),
  `jumlah` int(10) DEFAULT NULL,
  `keterangan` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`kdpengeluaran`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tr_pengeluaran
-- ----------------------------
BEGIN;
INSERT INTO `tr_pengeluaran` VALUES (1, '2019-07-14 05:21:46', 100000, 'pot bunga di depan rumah bu jane smith');
INSERT INTO `tr_pengeluaran` VALUES (2, '2019-07-14 05:22:12', 200000, 'semen di depan rumah pak john doe');
INSERT INTO `tr_pengeluaran` VALUES (5, '2019-07-16 03:11:08', 100000, 'perbaikan pagar rt rusak');
COMMIT;

-- ----------------------------
-- Table structure for warga
-- ----------------------------
DROP TABLE IF EXISTS `warga`;
CREATE TABLE `warga` (
  `kdwarga` int(11) NOT NULL AUTO_INCREMENT,
  `nmrt` int(10) DEFAULT NULL,
  `norumah` int(10) NOT NULL,
  `nokk` varchar(255) NOT NULL,
  `nmkk` varchar(255) DEFAULT NULL,
  `statustinggal` varchar(255) DEFAULT NULL,
  `pengurus` tinyint(1) DEFAULT 0,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`kdwarga`,`norumah`) USING BTREE,
  UNIQUE KEY `norumah` (`norumah`) USING BTREE,
  UNIQUE KEY `nokk` (`nokk`) USING BTREE,
  KEY `norumah_2` (`norumah`,`nokk`),
  KEY `warga_fk1` (`nmrt`),
  CONSTRAINT `warga_fk1` FOREIGN KEY (`nmrt`) REFERENCES `rt` (`nmrt`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of warga
-- ----------------------------
BEGIN;
INSERT INTO `warga` VALUES (3, 2, 11, '0001', 'john doe', 'kontrak', 1, '$2y$12$oNulNtpHg3ntSg1NJiQR0.kmv0hyTmGCtT5wHKdmS1HOYP8yb97Bq');
INSERT INTO `warga` VALUES (4, 2, 12, '0002', 'jane doe', 'milik sendiri', 0, '$2y$12$X8.O9i67XM.6T5sHIQYBQ.VIw/kB/AmsA9EoknJyFLLGt3iCJeNQC');
INSERT INTO `warga` VALUES (5, 3, 13, '0003', 'john smith', 'kontrak', 0, '$2y$12$4YFV.IRYDa2oG30CV7YmD.8/rPoa/fgtz9ABRsLLNU5HUa9xtTszW');
INSERT INTO `warga` VALUES (6, 3, 14, '0004', 'jane smith', 'milik sendiri', 0, '$2y$12$UmKeNK9FHNlvDAFTnNdnMuUY2sKLYiwHATriBi0lWE5nAmys65Q7a');
INSERT INTO `warga` VALUES (12, 1, 101, '0005', 'genghis khan', '', 0, '$2b$12$.gdXHY0/IvOV63qpxhMWXe7ADlg99u9tHsChZ0Cs/jHN4MimAW2y6');
INSERT INTO `warga` VALUES (19, 1, 103, '10102', 'john wick', 'kontrak', 0, '$2b$12$wRJHWxNtW7iUUMXeqh.scOegBPg0729VNkvPm2mHdq1UzHGoCPnv.');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
