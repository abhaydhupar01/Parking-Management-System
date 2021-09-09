-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 21, 2021 at 06:07 PM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 8.0.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `parking management`
--

-- --------------------------------------------------------

--
-- Table structure for table `admincred`
--

CREATE TABLE `admincred` (
  `userid` varchar(25) NOT NULL,
  `password` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admincred`
--

INSERT INTO `admincred` (`userid`, `password`) VALUES
('admin', '12345');

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `Name` varchar(30) NOT NULL,
  `Mail` varchar(30) NOT NULL,
  `Yfeedback` varchar(400) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `feedback`
--

INSERT INTO `feedback` (`Name`, `Mail`, `Yfeedback`) VALUES
('Abhay', 'abhaydhupar12@gmail.com', 'Nice Parking system');

-- --------------------------------------------------------

--
-- Table structure for table `information`
--

CREATE TABLE `information` (
  `Name` varchar(20) NOT NULL,
  `Mobile` varchar(11) NOT NULL,
  `Vehicleno` varchar(20) NOT NULL,
  `VehicleType` varchar(20) NOT NULL,
  `Passengers` varchar(11) NOT NULL,
  `InTime` varchar(20) NOT NULL,
  `Slot` varchar(15) NOT NULL,
  `Vstatus` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `information`
--

INSERT INTO `information` (`Name`, `Mobile`, `Vehicleno`, `VehicleType`, `Passengers`, `InTime`, `Slot`, `Vstatus`) VALUES
('Adarsh', '9347832894', 'CA4444', '4', '2', '11:42 AM', '5', 'PKD'),
('Priya', '7943284391', 'CA5555', '4', '1', '11:46 AM', '15', 'PKD'),
('Krishna', '6267288289', 'CA8392', '4', '4', '11:51 AM', '25', 'PKD'),
('Geeta', '8384382429', 'CD6662', '4', '3', '11:43 AM', '7', 'PKD'),
('Ankur', '9324788932', 'CH7733', '4', '2', '11:49 AM', '23', 'PKD'),
('Arpit', '8384738248', 'CL8347', '4', '4', '11:48 AM', '19', 'PKD'),
('Mayank', '9834732482', 'CM9076', '4', '3', '11:52 AM', '27', 'PKD'),
('Chirag', '9174323722', 'CT8828', '4', '3', '11:45 AM', '11', 'PKD'),
('Sohail', '8938883489', 'CV6672', '4', '3', '11:46 AM', '13', 'PKD'),
('Wasim', '6273782989', 'CW7347', '4', '4', '11:44 AM', '9', 'PKD'),
('Kunal', '7453267521', 'CY3323', '4', '4', '11:48 AM', '21', 'PKD'),
('Aparna', '9239473981', 'CY9828', '4', '3', '11:47 AM', '17', 'PKD'),
('Priyank', '7384928322', 'SA1122', '2', '1', '11:52 AM', '26', 'PKD'),
('Abhinav', '9347329847', 'SC9924', '4', '3', '11:42 AM', '1', 'PKD'),
('Lovely', '8871312278', 'SD9956', '2', '1', '11:43 AM', '8', 'PKD'),
('Sakshi', '7346378429', 'SE9943', '2', '2', '11:49 AM', '20', 'PKD'),
('Praveen', '9394939919', 'SK1012', '2', '1', '11:47 AM', '16', 'PKD'),
('Akhil', '9993325766', 'SK3310', '2', '2', '12:10 PM', '28', 'UNPKD'),
('Rohit', '8894732981', 'SK4454', '2', '1', '11:51 AM', '24', 'PKD'),
('Abhay', '9993328655', 'SK7180', '4', '2', '11:41 AM', '29', 'UNPKD'),
('Aditi', '7483479288', 'SK8186', '2', '2', '11:47 AM', '14', 'PKD'),
('Pooja', '9932782642', 'SP9662', '2', '1', '11:50 AM', '22', 'PKD'),
('Ravi', '9395798327', 'SQ9098', '2', '2', '11:44 AM', '10', 'PKD'),
('Raghav', '7493284798', 'SR6463', '2', '2', '11:43 AM', '6', 'PKD'),
('Shreya', '7384234792', 'SR8888', '2', '2', '11:48 AM', '18', 'PKD'),
('Apoorva', '9928328874', 'SR9991', '2', '1', '11:41 AM', '4', 'PKD'),
('Anushka', '9374389284', 'SV5526', '2', '1', '11:45 AM', '12', 'PKD'),
('Aditya', '7847324983', 'SW0012', '4', '4', '11:42 AM', '3', 'PKD');

-- --------------------------------------------------------

--
-- Table structure for table `parkingcharge`
--

CREATE TABLE `parkingcharge` (
  `id` varchar(20) NOT NULL,
  `TwoWheelCharge` varchar(15) NOT NULL,
  `FourWheelCharge` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `parkingcharge`
--

INSERT INTO `parkingcharge` (`id`, `TwoWheelCharge`, `FourWheelCharge`) VALUES
('admin', '20', '40');

-- --------------------------------------------------------

--
-- Table structure for table `slip`
--

CREATE TABLE `slip` (
  `Vehicleno` varchar(10) NOT NULL,
  `InTime` varchar(20) NOT NULL,
  `OutTime` varchar(20) NOT NULL,
  `Date` varchar(20) NOT NULL,
  `Charges` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `slip`
--

INSERT INTO `slip` (`Vehicleno`, `InTime`, `OutTime`, `Date`, `Charges`) VALUES
('SK3310', '12:10 PM', '12:12 PM', '2021-07-10', '15'),
('SK7180', '11:41 AM', '08:17 PM', '2021-07-15', '40');

-- --------------------------------------------------------

--
-- Table structure for table `slots`
--

CREATE TABLE `slots` (
  `Sno` varchar(15) NOT NULL,
  `Stype` varchar(12) NOT NULL,
  `Vehicleno` varchar(12) NOT NULL,
  `Status` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `slots`
--

INSERT INTO `slots` (`Sno`, `Stype`, `Vehicleno`, `Status`) VALUES
('1', '4', 'SC9924', 'UNAVBL'),
('2', '2', '', 'AVBL'),
('3', '4', 'SW0012', 'UNAVBL'),
('4', '2', 'SR9991', 'UNAVBL'),
('5', '4', 'CA4444', 'UNAVBL'),
('6', '2', 'SR6463', 'UNAVBL'),
('7', '4', 'CD6662', 'UNAVBL'),
('8', '2', 'SD9956', 'UNAVBL'),
('9', '4', 'CW7347', 'UNAVBL'),
('10', '2', 'SQ9098', 'UNAVBL'),
('11', '4', 'CT8828', 'UNAVBL'),
('12', '2', 'SV5526', 'UNAVBL'),
('13', '4', 'CV6672', 'UNAVBL'),
('14', '2', 'SK8186', 'UNAVBL'),
('15', '4', 'CA5555', 'UNAVBL'),
('16', '2', 'SK1012', 'UNAVBL'),
('17', '4', 'CY9828', 'UNAVBL'),
('18', '2', 'SR8888', 'UNAVBL'),
('19', '4', 'CL8347', 'UNAVBL'),
('20', '2', 'SE9943', 'UNAVBL'),
('21', '4', 'CY3323', 'UNAVBL'),
('22', '2', 'SP9662', 'UNAVBL'),
('23', '4', 'CH7733', 'UNAVBL'),
('24', '2', 'SK4454', 'UNAVBL'),
('25', '4', 'CA8392', 'UNAVBL'),
('26', '2', 'SA1122', 'UNAVBL'),
('27', '4', 'CM9076', 'UNAVBL'),
('28', '2', '', 'AVBL'),
('29', '4', '', 'AVBL'),
('30', '2', '', 'AVBL'),
('31', '4', '', 'AVBL'),
('32', '2', '', 'AVBL'),
('33', '4', '', 'AVBL'),
('34', '2', '', 'AVBL'),
('35', '4', '', 'AVBL'),
('36', '2', '', 'AVBL'),
('37', '4', '', 'AVBL'),
('38', '2', '', 'AVBL'),
('39', '4', '', 'AVBL'),
('40', '2', '', 'AVBL'),
('41', '4', '', 'AVBL'),
('42', '2', '', 'AVBL'),
('43', '4', '', 'AVBL'),
('44', '2', '', 'AVBL'),
('45', '4', '', 'AVBL'),
('46', '2', '', 'AVBL'),
('47', '4', '', 'AVBL'),
('48', '2', '', 'AVBL'),
('49', '4', '', 'AVBL'),
('50', '2', '', 'AVBL'),
('51', '4', '', 'AVBL'),
('52', '2', '', 'AVBL'),
('53', '4', '', 'AVBL'),
('54', '2', '', 'AVBL'),
('55', '4', '', 'AVBL'),
('56', '2', '', 'AVBL'),
('57', '4', '', 'AVBL'),
('58', '2', '', 'AVBL'),
('59', '4', '', 'AVBL'),
('60', '2', '', 'AVBL'),
('61', '4', '', 'AVBL'),
('62', '2', '', 'AVBL'),
('63', '4', '', 'AVBL'),
('64', '2', '', 'AVBL'),
('65', '4', '', 'AVBL'),
('66', '2', '', 'AVBL'),
('67', '4', '', 'AVBL'),
('68', '2', '', 'AVBL'),
('69', '4', '', 'AVBL'),
('70', '2', '', 'AVBL'),
('71', '4', '', 'AVBL'),
('72', '2', '', 'AVBL'),
('73', '4', '', 'AVBL'),
('74', '2', '', 'AVBL'),
('75', '4', '', 'AVBL'),
('76', '2', '', 'AVBL'),
('77', '4', '', 'AVBL'),
('78', '2', '', 'AVBL'),
('79', '4', '', 'AVBL'),
('80', '2', '', 'AVBL'),
('81', '4', '', 'AVBL'),
('82', '2', '', 'AVBL'),
('83', '4', '', 'AVBL'),
('84', '2', '', 'AVBL'),
('85', '4', '', 'AVBL'),
('86', '2', '', 'AVBL'),
('87', '4', '', 'AVBL'),
('88', '2', '', 'AVBL'),
('89', '4', '', 'AVBL'),
('90', '2', '', 'AVBL'),
('91', '4', '', 'AVBL'),
('92', '2', '', 'AVBL'),
('93', '4', '', 'AVBL'),
('94', '2', '', 'AVBL'),
('95', '4', '', 'AVBL'),
('96', '2', '', 'AVBL'),
('97', '4', '', 'AVBL'),
('98', '2', '', 'AVBL'),
('99', '4', '', 'AVBL'),
('100', '2', '', 'AVBL'),
('101', '4', '', 'AVBL'),
('102', '2', '', 'AVBL'),
('103', '4', '', 'AVBL'),
('104', '2', '', 'AVBL'),
('105', '4', '', 'AVBL'),
('106', '2', '', 'AVBL'),
('107', '4', '', 'AVBL'),
('108', '2', '', 'AVBL'),
('109', '4', '', 'AVBL'),
('110', '2', '', 'AVBL'),
('111', '4', '', 'AVBL'),
('112', '2', '', 'AVBL'),
('113', '4', '', 'AVBL'),
('114', '2', '', 'AVBL'),
('115', '4', '', 'AVBL'),
('116', '2', '', 'AVBL'),
('117', '4', '', 'AVBL'),
('118', '2', '', 'AVBL'),
('119', '4', '', 'AVBL'),
('120', '2', '', 'AVBL'),
('121', '4', '', 'AVBL'),
('122', '2', '', 'AVBL'),
('123', '4', '', 'AVBL'),
('124', '2', '', 'AVBL'),
('125', '4', '', 'AVBL'),
('126', '2', '', 'AVBL'),
('127', '4', '', 'AVBL'),
('128', '2', '', 'AVBL'),
('129', '4', '', 'AVBL'),
('130', '2', '', 'AVBL'),
('131', '4', '', 'AVBL'),
('132', '2', '', 'AVBL'),
('133', '4', '', 'AVBL'),
('134', '2', '', 'AVBL'),
('135', '4', '', 'AVBL'),
('136', '2', '', 'AVBL'),
('137', '4', '', 'AVBL'),
('138', '2', '', 'AVBL'),
('139', '4', '', 'AVBL'),
('140', '2', '', 'AVBL'),
('141', '4', '', 'AVBL'),
('142', '2', '', 'AVBL'),
('143', '4', '', 'AVBL'),
('144', '2', '', 'AVBL'),
('145', '4', '', 'AVBL'),
('146', '2', '', 'AVBL'),
('147', '4', '', 'AVBL'),
('148', '2', '', 'AVBL'),
('149', '4', '', 'AVBL'),
('150', '2', '', 'AVBL'),
('151', '4', '', 'AVBL'),
('152', '2', '', 'AVBL'),
('153', '4', '', 'AVBL'),
('154', '2', '', 'AVBL'),
('155', '4', '', 'AVBL'),
('156', '2', '', 'AVBL'),
('157', '4', '', 'AVBL'),
('158', '2', '', 'AVBL'),
('159', '4', '', 'AVBL'),
('160', '2', '', 'AVBL'),
('161', '4', '', 'AVBL'),
('162', '2', '', 'AVBL'),
('163', '4', '', 'AVBL'),
('164', '2', '', 'AVBL'),
('165', '4', '', 'AVBL'),
('166', '2', '', 'AVBL'),
('167', '4', '', 'AVBL'),
('168', '2', '', 'AVBL'),
('169', '4', '', 'AVBL'),
('170', '2', '', 'AVBL'),
('171', '4', '', 'AVBL'),
('172', '2', '', 'AVBL'),
('173', '4', '', 'AVBL'),
('174', '2', '', 'AVBL'),
('175', '4', '', 'AVBL'),
('176', '2', '', 'AVBL'),
('177', '4', '', 'AVBL'),
('178', '2', '', 'AVBL'),
('179', '4', '', 'AVBL'),
('180', '2', '', 'AVBL'),
('181', '4', '', 'AVBL'),
('182', '2', '', 'AVBL'),
('183', '4', '', 'AVBL'),
('184', '2', '', 'AVBL'),
('185', '4', '', 'AVBL'),
('186', '2', '', 'AVBL'),
('187', '4', '', 'AVBL'),
('188', '2', '', 'AVBL'),
('189', '4', '', 'AVBL'),
('190', '2', '', 'AVBL'),
('191', '4', '', 'AVBL'),
('192', '2', '', 'AVBL'),
('193', '4', '', 'AVBL'),
('194', '2', '', 'AVBL'),
('195', '4', '', 'AVBL'),
('196', '2', '', 'AVBL'),
('197', '4', '', 'AVBL'),
('198', '2', '', 'AVBL'),
('199', '4', '', 'AVBL'),
('200', '2', '', 'AVBL');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `information`
--
ALTER TABLE `information`
  ADD PRIMARY KEY (`Vehicleno`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
