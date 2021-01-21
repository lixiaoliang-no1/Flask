-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- 主机： localhost
-- 生成日期： 2020-11-17 20:16:12
-- 服务器版本： 5.7.26
-- PHP 版本： 5.6.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 数据库： `app`
--

-- --------------------------------------------------------

--
-- 表的结构 `private_text`
--

CREATE TABLE `private_text` (
  `id` int(11) DEFAULT NULL,
  `from_userid` int(11) DEFAULT NULL,
  `to_userid` int(11) DEFAULT NULL,
  `time` int(11) DEFAULT NULL,
  `massage` text COLLATE utf8_unicode_ci
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- 表的结构 `public_text`
--

CREATE TABLE `public_text` (
  `id` int(11) NOT NULL,
  `from_userid` int(11) DEFAULT NULL,
  `from_name` varchar(30) COLLATE utf8_unicode_ci DEFAULT NULL,
  `time` varchar(30) COLLATE utf8_unicode_ci DEFAULT NULL,
  `massage` text COLLATE utf8_unicode_ci
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 转存表中的数据 `public_text`
--

INSERT INTO `public_text` (`id`, `from_userid`, `from_name`, `time`, `massage`) VALUES
(1, 6, '123', '2020-10-26 11:57:15', '456'),
(2, 6, '123', '2020-10-26 12:11:27', '7777'),
(3, 7, '测试人员', '2020-10-26 12:12:41', 'whta?'),
(4, 7, '测试人员', '2020-10-26 12:20:09', 'dd'),
(5, 6, '123', '2020-10-26 12:21:07', '123123');

-- --------------------------------------------------------

--
-- 表的结构 `user`
--

CREATE TABLE `user` (
  `userid` int(11) NOT NULL,
  `username` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `password` varchar(150) COLLATE utf8_unicode_ci DEFAULT NULL,
  `is_admin` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 转存表中的数据 `user`
--

INSERT INTO `user` (`userid`, `username`, `password`, `is_admin`) VALUES
(1, 'admin', 'pbkdf2:sha256:150000$L5VIK6xs$dbcec8f400525d960da56e593bc8fef5ac3fea71ba4c0d461b217b58ee166def', NULL),
(2, 'diego', 'pbkdf2:sha256:150000$jojTnaq2$42c6fa2daf53db42f5a0dfaf6b679ac4e6483b7b249242b30d745e488577c3cb', NULL),
(3, 'double', 'pbkdf2:sha256:150000$2ZYNDoe6$e89cd26d406a627e1dd29f238b3e938e4252f8a8f88e9deb055607cb3dc05db3', NULL),
(4, 'lxl', 'pbkdf2:sha256:150000$CU2x8gZh$c2453006218fe644e9bec1b614e1679b2fb487da015a8588a5c79e447284af4a', NULL),
(5, 'test', 'pbkdf2:sha256:150000$NkCKRpXE$dcd63b5bf6444bcf8d1ce6b881399edf30dcc8e4059ce81a9459c430ff8fed9b', NULL),
(6, '123', 'pbkdf2:sha256:150000$Hovrpb1R$9edf80e395c2c8b9920c95141eb1247304a5c0242b6c96e6753bd827bad6de63', NULL),
(7, '测试人员', 'pbkdf2:sha256:150000$mZwU0Jp8$ff0949f6d248daace76d3582a51752aa56c44f023d42658171e4edb9c1c0b365', NULL),
(8, '陈璐', 'pbkdf2:sha256:150000$Pe0mezNX$2c5d0e2071692047307107ef8e02b3df992b4bb49a16424f8a8a9e2271c528ab', NULL);

-- --------------------------------------------------------

--
-- 表的结构 `user_massage`
--

CREATE TABLE `user_massage` (
  `userid` int(11) DEFAULT NULL,
  `real_name` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `sex` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `location` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `phone` varchar(11) COLLATE utf8_unicode_ci DEFAULT NULL,
  `email` varchar(30) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 转存表中的数据 `user_massage`
--

INSERT INTO `user_massage` (`userid`, `real_name`, `sex`, `location`, `phone`, `email`) VALUES
(1, NULL, NULL, NULL, NULL, NULL),
(2, NULL, NULL, NULL, NULL, NULL),
(3, NULL, NULL, NULL, NULL, NULL),
(4, NULL, NULL, NULL, NULL, NULL),
(5, NULL, NULL, NULL, NULL, NULL),
(6, NULL, NULL, NULL, NULL, NULL),
(7, NULL, NULL, NULL, NULL, NULL),
(8, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- 表的结构 `user_tou`
--

CREATE TABLE `user_tou` (
  `userid` int(11) DEFAULT NULL,
  `address` varchar(70) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 转存表中的数据 `user_tou`
--

INSERT INTO `user_tou` (`userid`, `address`) VALUES
(1, '/up_file_tou/images/mmmmmmmmmmmm.jpg'),
(2, '/up_file_tou/images/f68f35625d820b2f0d73d557ede6a629.png'),
(3, '/up_file_tou/images/d4c4b79ab5e2f76bbca046d08d5e68ff.png'),
(4, '/up_file_tou/images/a270c53b8f8f327437f2d6547ef5ca97.png'),
(5, '/up_file_tou/images/mmmmmmmmmmmm.jpg'),
(6, '/up_file_tou/images/mmmmmmmmmmmm.jpg'),
(7, '/up_file_tou/images/5c92c57605352aba0b22e6ba4bb9245b.png'),
(8, '/up_file_tou/images/mmmmmmmmmmmm.jpg');

-- --------------------------------------------------------

--
-- 表的结构 `user_write_text`
--

CREATE TABLE `user_write_text` (
  `id` int(11) NOT NULL,
  `userid` int(11) DEFAULT NULL,
  `text` text COLLATE utf8_unicode_ci,
  `time` varchar(30) COLLATE utf8_unicode_ci DEFAULT NULL,
  `title` varchar(30) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 转存表中的数据 `user_write_text`
--

INSERT INTO `user_write_text` (`id`, `userid`, `text`, `time`, `title`) VALUES
(1, 7, '456', '2020-10-26 12:24:57', '123');

--
-- 转储表的索引
--

--
-- 表的索引 `public_text`
--
ALTER TABLE `public_text`
  ADD PRIMARY KEY (`id`);

--
-- 表的索引 `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`userid`);

--
-- 表的索引 `user_write_text`
--
ALTER TABLE `user_write_text`
  ADD PRIMARY KEY (`id`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `public_text`
--
ALTER TABLE `public_text`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- 使用表AUTO_INCREMENT `user`
--
ALTER TABLE `user`
  MODIFY `userid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- 使用表AUTO_INCREMENT `user_write_text`
--
ALTER TABLE `user_write_text`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
