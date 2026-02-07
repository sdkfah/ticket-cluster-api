/*
 Navicat Premium Dump SQL

 Source Server         : localhost_3306
 Source Server Type    : MySQL
 Source Server Version : 80044 (8.0.44)
 Source Host           : localhost:3306
 Source Schema         : tickets

 Target Server Type    : MySQL
 Target Server Version : 80044 (8.0.44)
 File Encoding         : 65001

 Date: 07/02/2026 09:51:16
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;


-- ----------------------------
-- Table structure for device_group_link
-- ----------------------------
DROP TABLE IF EXISTS `device_group_link`;
CREATE TABLE `device_group_link` (
  `id` int NOT NULL AUTO_INCREMENT,
  `device_sn` varchar(64) NOT NULL COMMENT '逻辑关联 devices.sn',
  `group_id` int NOT NULL COMMENT '逻辑关联 device_groups.id',
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_sn_group` (`device_sn`,`group_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='设备与分组的多对多关联表';

-- ----------------------------
-- Table structure for device_groups
-- ----------------------------
DROP TABLE IF EXISTS `device_groups`;
CREATE TABLE `device_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL COMMENT '组名',
  `config_json` json DEFAULT NULL COMMENT '该组特有的配置(延迟、策略等)',
  `description` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='设备分组逻辑表';

-- ----------------------------
-- Table structure for devices
-- ----------------------------
DROP TABLE IF EXISTS `devices`;
CREATE TABLE `devices` (
  `id` int NOT NULL AUTO_INCREMENT,
  `sn` varchar(64) NOT NULL COMMENT '设备SN码/序列号',
  `brand` varchar(32) DEFAULT NULL COMMENT '品牌',
  `model` varchar(64) DEFAULT NULL COMMENT '型号',
  `ip_address` varchar(45) DEFAULT NULL COMMENT '内网IP',
  `status` tinyint DEFAULT '0' COMMENT '0:离线, 1:在线, 2:抢票中',
  `last_seen` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_sn` (`sn`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='设备管理主表';

-- ----------------------------
-- Table structure for order_tasks
-- ----------------------------
DROP TABLE IF EXISTS `order_tasks`;
CREATE TABLE `order_tasks` (
  `id` int NOT NULL AUTO_INCREMENT,
  `city` varchar(64) NOT NULL COMMENT '城市',
  `artist` varchar(128) NOT NULL COMMENT '艺人/演出名称',
  `target_date` varchar(128) DEFAULT NULL COMMENT '目标日期',
  `item_id` varchar(32) DEFAULT NULL COMMENT '项目id',
  `sku_id` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '关联票档',
  `target_price` varchar(32) DEFAULT NULL COMMENT '目标票价',
  `customer_info` varchar(500) DEFAULT NULL COMMENT '实名人信息(姓名+身份证)',
  `priority_order` varchar(255) DEFAULT NULL COMMENT '优先顺序',
  `bounty` decimal(10,2) DEFAULT NULL COMMENT '红包金额',
  `contact_phone` varchar(20) DEFAULT NULL COMMENT '联系电话',
  `status` tinyint DEFAULT '0' COMMENT '状态: 0待处理, 1已抢到, 2已撤单',
  `created_at` datetime DEFAULT NULL COMMENT '创建时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_artist_customer` (`artist`,`customer_info`),
  KEY `idx_status` (`status`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='抢票任务表';

-- ----------------------------
-- Table structure for ticket_items
-- ----------------------------
DROP TABLE IF EXISTS `ticket_items`;
CREATE TABLE `ticket_items` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `item_id` varchar(32) NOT NULL COMMENT '项目ID',
  `project_title` varchar(255) DEFAULT NULL COMMENT '演出名称',
  `venue_name` varchar(128) DEFAULT NULL COMMENT '场馆',
  `perform_id` varchar(32) NOT NULL COMMENT '场次ID',
  `perform_time` datetime DEFAULT NULL COMMENT '演出时间',
  `sku_id` varchar(32) NOT NULL COMMENT '票档SKU ID',
  `price_name` varchar(64) DEFAULT NULL COMMENT '票档描述',
  `price` decimal(10,2) DEFAULT NULL COMMENT '价格',
  `stock_status` tinyint(1) DEFAULT '1' COMMENT '是否有票: 1有, 0无',
  `limit_quantity` int DEFAULT '4' COMMENT '每单限购额',
  `sale_start_time` datetime DEFAULT NULL COMMENT '开抢时间',
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_sku` (`sku_id`),
  KEY `idx_perform_sku` (`perform_id`,`sku_id`),
  KEY `idx_price_time` (`price`,`perform_time`),
  KEY `idx_sale_time` (`sale_start_time`)
) ENGINE=InnoDB AUTO_INCREMENT=113 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='演出信息表';

SET FOREIGN_KEY_CHECKS = 1;
