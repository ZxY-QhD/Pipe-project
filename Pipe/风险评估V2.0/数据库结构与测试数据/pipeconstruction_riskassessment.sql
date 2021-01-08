/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50717
Source Host           : 127.0.0.1:3306
Source Database       : pipeconstruction_riskassessment

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2020-11-21 21:23:09
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for newprojectinfo
-- ----------------------------
DROP TABLE IF EXISTS `newprojectinfo`;
CREATE TABLE `newprojectinfo` (
  `U01` varchar(100) NOT NULL,
  `date` date DEFAULT NULL,
  `U02` varchar(100) NOT NULL,
  `U03` varchar(100) NOT NULL,
  `U04` varchar(100) NOT NULL,
  `U31` varchar(100) NOT NULL,
  `U05` varchar(100) NOT NULL,
  `U32` varchar(100) NOT NULL,
  `U06` varchar(100) NOT NULL,
  `U33` varchar(100) NOT NULL,
  `U07` varchar(100) NOT NULL,
  `U34` varchar(100) NOT NULL,
  `U08` varchar(100) NOT NULL,
  `U11` varchar(100) NOT NULL,
  `U09` int(11) NOT NULL,
  `U12` varchar(100) NOT NULL,
  `U13` varchar(100) NOT NULL,
  `U4` varchar(100) DEFAULT NULL,
  `U5` varchar(100) DEFAULT NULL,
  `U6` varchar(100) DEFAULT NULL,
  `U7` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`U01`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of newprojectinfo
-- ----------------------------
INSERT INTO `newprojectinfo` VALUES ('A101', '2020-11-21', '石家庄运河桥顶管隧道施工工程', '石家庄', '铁道建设', '甲级', '铁道建设', '特级总承包', '铁道建设', '甲级', '铁道建设', '甲级', '2300', '5.6', '0', '{r=1.8}', '软黏土', '{}', '{U511:0,U512:2.9,U52:6,U53:1,U54:2.0}', '{U61:1,U62:3.7,U63:6}', '');

-- ----------------------------
-- Table structure for risk_advice
-- ----------------------------
DROP TABLE IF EXISTS `risk_advice`;
CREATE TABLE `risk_advice` (
  `RiskNo` varchar(100) NOT NULL,
  `RiskName` varchar(100) NOT NULL,
  `Advice` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`RiskNo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of risk_advice
-- ----------------------------
INSERT INTO `risk_advice` VALUES ('U11', '新建顶管埋深', null);
INSERT INTO `risk_advice` VALUES ('U12', '新建顶管尺寸', null);
INSERT INTO `risk_advice` VALUES ('U13', '新建工程土层性质', null);
INSERT INTO `risk_advice` VALUES ('U21', '土舱压力', '土舱压力一方面决定掌子面的稳定性，另一方面影响着掘进过程中地层损失的大小，因此施工中应严格控制土舱压力。施工中土舱压力应以靠近土舱中轴位置的监测元件监测结果为准，以静止水土压力为基准进行±20kPa调整。当接近既有建筑（构筑）物时，应适当调高，但在遇有水平平行既有管线时应适当调低。');
INSERT INTO `risk_advice` VALUES ('U22', '注浆压力', '泥浆套主要作用为掘进过程减阻和减小地层损失。泥浆套主要成分为膨润土和水，膨润土在注入前需膨化48h，膨润泥浆的注入压力应静止土压力的1.1倍，过大易造成土体劈裂跑浆，过小则难以保证充填效果、地层损失过大。顶管顶进过程中一般需进行同步注浆和补充注浆，以确保管周泥浆套的施做质量。');
INSERT INTO `risk_advice` VALUES ('U23', '顶进速度', '顶进速度:在顶进速度的控制中，应注意以下几点：①开始顶进和结束顶进之前速度不宜过快；②每节顶进开始时，应逐步提高顶进速度，防止启动速度过大；③一节顶进过程中，应尽量保持恒定，减少波动，以保证切口水压稳定和送、排泥浆管的畅通；④顶进速度的快慢必须满足每节润滑泥浆注浆量的要求，保证润滑泥浆处于良好的工作状态。');
INSERT INTO `risk_advice` VALUES ('U31', '施工技术状况', null);
INSERT INTO `risk_advice` VALUES ('U32', '施工质量', null);
INSERT INTO `risk_advice` VALUES ('U33', '检测情况', null);
INSERT INTO `risk_advice` VALUES ('U34', '监理情况', null);
INSERT INTO `risk_advice` VALUES ('U41', '新建顶管与邻近柔性管线净距', null);
INSERT INTO `risk_advice` VALUES ('U42', '新建顶管与邻近柔性管线空间位置关系', null);
INSERT INTO `risk_advice` VALUES ('U43', '邻近柔性管线管径', null);
INSERT INTO `risk_advice` VALUES ('U51', '开挖顶管邻近刚性管线与净距', '对顶管穿越邻近隧道区域，根据工程需要，可采取压密注浆的方式进行地层与加固处理，减小顶管施工对邻近隧道结构的影响。');
INSERT INTO `risk_advice` VALUES ('U52', '新建顶管与邻近刚性管线空间位置关系', null);
INSERT INTO `risk_advice` VALUES ('U53', '邻近刚性管线材质', null);
INSERT INTO `risk_advice` VALUES ('U54', '邻近刚性管线尺寸', null);
INSERT INTO `risk_advice` VALUES ('U61', '建筑物基础形式', '建筑物的基础形式：若建筑物基础为桩基，桩基未侵入隧道开挖边线，但是桩端已不能承载上部荷载时，可通过预注浆提高桩基的承载力，保证建筑物的安全；若桩基已经侵入隧道开挖边线，可对桩基进行梁式托换或者板基基础托换，必要时切断原桩。若建筑物基础为筏板基础或箱型基础，该基础形式整体刚度较好，建筑物自身抗变形能力较强，则可从隧道自身防治措施着手，在施工过程中提前改良地层，减小地层损失，同时地面上跟踪注浆和监测。若建筑物基础为其他浅基础，自身抗变形能力较弱，则从洞内和洞外均须处理，严格遵守“管超前、严注浆、短进尺、弱爆破、快支护、勤量测”十八字方针。');
INSERT INTO `risk_advice` VALUES ('U62', '新建顶管与临近基础水平净距', null);
INSERT INTO `risk_advice` VALUES ('U63', '临近基础高度', null);

-- ----------------------------
-- Table structure for risk_level2
-- ----------------------------
DROP TABLE IF EXISTS `risk_level2`;
CREATE TABLE `risk_level2` (
  `U01` varchar(100) NOT NULL,
  `RiskName` varchar(100) NOT NULL,
  `RiskWeight` double NOT NULL,
  `RiskValue` double NOT NULL,
  `RiskLevel` varchar(100) NOT NULL,
  PRIMARY KEY (`U01`,`RiskName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of risk_level2
-- ----------------------------
INSERT INTO `risk_level2` VALUES ('A101', 'U11', '0.066', '0.6', '较高风险');
INSERT INTO `risk_level2` VALUES ('A101', 'U12', '0.066', '0.7', '较高风险');
INSERT INTO `risk_level2` VALUES ('A101', 'U13', '0.066', '0.6', '较高风险');
INSERT INTO `risk_level2` VALUES ('A101', 'U21', '0.066', '0.7', '较高风险');
INSERT INTO `risk_level2` VALUES ('A101', 'U22', '0.066', '0.32', '较低风险');
INSERT INTO `risk_level2` VALUES ('A101', 'U23', '0.066', '0.32', '较低风险');
INSERT INTO `risk_level2` VALUES ('A101', 'U31', '0.05', '0.24', '较低风险');
INSERT INTO `risk_level2` VALUES ('A101', 'U32', '0.05', '0.24', '较低风险');
INSERT INTO `risk_level2` VALUES ('A101', 'U33', '0.05', '0.24', '较低风险');
INSERT INTO `risk_level2` VALUES ('A101', 'U34', '0.05', '0.24', '较低风险');
INSERT INTO `risk_level2` VALUES ('A101', 'U51', '0.05', '0.7', '较高风险');
INSERT INTO `risk_level2` VALUES ('A101', 'U52', '0.05', '0.6', '较高风险');
INSERT INTO `risk_level2` VALUES ('A101', 'U53', '0.05', '0.54', '中等风险');
INSERT INTO `risk_level2` VALUES ('A101', 'U54', '0.05', '0.48', '中等风险');
INSERT INTO `risk_level2` VALUES ('A101', 'U61', '0.066', '0.6', '较高风险');
INSERT INTO `risk_level2` VALUES ('A101', 'U62', '0.066', '0.32', '较低风险');
INSERT INTO `risk_level2` VALUES ('A101', 'U63', '0.066', '0.3', '较低风险');

-- ----------------------------
-- Table structure for risk_result
-- ----------------------------
DROP TABLE IF EXISTS `risk_result`;
CREATE TABLE `risk_result` (
  `U01` varchar(100) NOT NULL,
  `Sum_Risk1` double NOT NULL,
  `Sum_Risk2` double NOT NULL,
  `Sum_Risk3` double NOT NULL,
  `Sum_Risk4` double NOT NULL,
  `Sum_Risk5` double NOT NULL,
  `Result` varchar(100) NOT NULL,
  PRIMARY KEY (`U01`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of risk_result
-- ----------------------------
INSERT INTO `risk_result` VALUES ('A101', '0', '0.464', '0.43', '0.1', '0', '较低风险');

-- ----------------------------
-- Table structure for userinfo
-- ----------------------------
DROP TABLE IF EXISTS `userinfo`;
CREATE TABLE `userinfo` (
  `UserId` int(11) NOT NULL,
  `Username` varchar(100) NOT NULL,
  `Password` varchar(100) NOT NULL,
  PRIMARY KEY (`UserId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of userinfo
-- ----------------------------
INSERT INTO `userinfo` VALUES ('1', 'admin', '123456');
