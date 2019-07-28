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

 Date: 28/07/2019 20:47:44
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

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
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of saldokas
-- ----------------------------
BEGIN;
INSERT INTO `saldokas` VALUES (10, 2019, 'jul', 100000, 400000, -300000);
INSERT INTO `saldokas` VALUES (12, 2019, 'jun', 0, 0, 0);
INSERT INTO `saldokas` VALUES (13, 2019, 'mei', 0, 0, 0);
COMMIT;

-- ----------------------------
-- Table structure for tbl_warga
-- ----------------------------
DROP TABLE IF EXISTS `tbl_warga`;
CREATE TABLE `tbl_warga` (
  `kdrw` varchar(3) NOT NULL,
  `kdrt` varchar(3) NOT NULL,
  `norumah` varchar(5) NOT NULL,
  `nokk` varchar(16) NOT NULL,
  `nmkk` varchar(50) DEFAULT NULL,
  `statustinggal` varchar(255) DEFAULT NULL,
  `pengurus` tinyint(1) DEFAULT 0,
  `passwd` tinytext NOT NULL,
  PRIMARY KEY (`kdrw`,`norumah`,`kdrt`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tbl_warga
-- ----------------------------
BEGIN;
INSERT INTO `tbl_warga` VALUES ('01', '02', '00005', '10102', 'jane doe', 'kontrak', 0, '$2b$12$mOlWbYJpT6DavagusumtAuigH7UMusS99OeP2ecEpNplcApL3qwku');
INSERT INTO `tbl_warga` VALUES ('01', '02', '00006', '10102', 'john smith', 'kontrak', 0, '$2b$12$t78atiDtjlPy39ObewEGzOMsSregBRwokAmkqtxDLPw5uG5pftsIi');
INSERT INTO `tbl_warga` VALUES ('01', '02', '00007', '10102', 'jane smith', 'kontrak', 1, '$2b$12$W9ucup9UC4kFv66qVsyKMeh7/m6Zj8MhtfOyJmeiPwMkQrP0ezf/O');
COMMIT;

-- ----------------------------
-- Table structure for tr_iuran
-- ----------------------------
DROP TABLE IF EXISTS `tr_iuran`;
CREATE TABLE `tr_iuran` (
  `tahun` year(4) NOT NULL,
  `kdrw` varchar(3) NOT NULL,
  `kdrt` varchar(3) NOT NULL,
  `norumah` varchar(5) NOT NULL,
  `jan` int(11) DEFAULT NULL,
  `feb` int(11) DEFAULT NULL,
  `mar` int(11) DEFAULT NULL,
  `apr` int(11) DEFAULT NULL,
  `may` int(11) DEFAULT NULL,
  `jun` int(11) DEFAULT NULL,
  `jul` int(11) DEFAULT NULL,
  `aug` int(11) DEFAULT NULL,
  `sep` int(11) DEFAULT NULL,
  `oct` int(11) DEFAULT NULL,
  `nop` int(11) DEFAULT NULL,
  `des` int(11) DEFAULT NULL,
  PRIMARY KEY (`tahun`,`kdrw`,`kdrt`,`norumah`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tr_iuran
-- ----------------------------
BEGIN;
INSERT INTO `tr_iuran` VALUES (2019, '01', '01', '1001', 100000, 200000, 100000, 200000, 100000, 200000, 150000, 200000, 100000, 150000, 100000, 200000);
COMMIT;

-- ----------------------------
-- Table structure for tr_pemasukan
-- ----------------------------
DROP TABLE IF EXISTS `tr_pemasukan`;
CREATE TABLE `tr_pemasukan` (
  `kdpemasukan` int(11) NOT NULL AUTO_INCREMENT,
  `tanggal` datetime NOT NULL DEFAULT current_timestamp(),
  `norumah` varchar(5) NOT NULL,
  `kdrw` varchar(3) NOT NULL,
  `kdrt` varchar(3) NOT NULL,
  `nokk` varchar(255) NOT NULL,
  `jumlah` int(10) DEFAULT NULL,
  `keterangan` varchar(255) DEFAULT NULL,
  `dokumen_bayar` blob DEFAULT NULL,
  `terverifikasi` tinyint(1) DEFAULT 0,
  PRIMARY KEY (`kdpemasukan`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tr_pemasukan
-- ----------------------------
BEGIN;
INSERT INTO `tr_pemasukan` VALUES (16, '2019-07-28 13:23:56', '10111', '01', '02', '0001', 100000, 'nothing', 0x61736466, 0);
INSERT INTO `tr_pemasukan` VALUES (17, '2019-07-28 13:24:16', '10101', '01', '02', '0001', 100000, 'nothing', 0x61736466, 1);
INSERT INTO `tr_pemasukan` VALUES (18, '2019-07-28 13:25:40', '10101', '01', '02', '0001', 100000, 'nothing', 0x61736466, 0);
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
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tr_pengeluaran
-- ----------------------------
BEGIN;
INSERT INTO `tr_pengeluaran` VALUES (6, '2019-07-28 13:26:21', 100000, 'perbaikan pagar rt rusak');
INSERT INTO `tr_pengeluaran` VALUES (7, '2019-07-28 13:26:22', 100000, 'perbaikan pagar rt rusak');
INSERT INTO `tr_pengeluaran` VALUES (8, '2019-07-28 13:26:23', 100000, 'perbaikan pagar rt rusak');
INSERT INTO `tr_pengeluaran` VALUES (9, '2019-07-28 13:26:23', 100000, 'perbaikan pagar rt rusak');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
