-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 03, 2020 at 11:17 AM
-- Server version: 10.1.37-MariaDB
-- PHP Version: 7.3.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `amazon_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `brand`
--

CREATE TABLE `brand` (
  `bid` int(10) NOT NULL,
  `cid` varchar(30) NOT NULL,
  `scid` int(15) NOT NULL,
  `bname` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `brand`
--

INSERT INTO `brand` (`bid`, `cid`, `scid`, `bname`) VALUES
(1, '1', 1, 'Samsung'),
(2, '2', 2, 'Redmi'),
(3, '3', 3, 'puma'),
(4, '1', 4, 'Sony');

-- --------------------------------------------------------

--
-- Table structure for table `cart`
--

CREATE TABLE `cart` (
  `cartid` int(11) NOT NULL,
  `cid` int(11) NOT NULL,
  `mid` int(11) NOT NULL,
  `pid` int(11) NOT NULL,
  `amount` int(11) NOT NULL,
  `qty` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `catogory`
--

CREATE TABLE `catogory` (
  `cid` int(30) NOT NULL,
  `cname` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `catogory`
--

INSERT INTO `catogory` (`cid`, `cname`) VALUES
(1, 'Electronics'),
(2, 'Mobiles'),
(3, 'fashion'),
(5, 'dfdfb');

-- --------------------------------------------------------

--
-- Table structure for table `cusreg`
--

CREATE TABLE `cusreg` (
  `cus_id` int(20) NOT NULL,
  `fname` varchar(30) NOT NULL,
  `lname` varchar(30) NOT NULL,
  `address` varchar(50) NOT NULL,
  `email` varchar(20) NOT NULL,
  `pincode` varchar(10) NOT NULL,
  `dob` date NOT NULL,
  `gender` varchar(10) NOT NULL,
  `phono` varchar(30) NOT NULL,
  `username` varchar(30) DEFAULT NULL,
  `password` varchar(30) NOT NULL,
  `cpassword` varchar(30) NOT NULL,
  `district` varchar(30) NOT NULL,
  `state` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cusreg`
--

INSERT INTO `cusreg` (`cus_id`, `fname`, `lname`, `address`, `email`, `pincode`, `dob`, `gender`, `phono`, `username`, `password`, `cpassword`, `district`, `state`) VALUES
(1, 'amal', 'd', 'fgcg@', '123@gmail.com', '668', '0000-00-00', 'male', '9874563210', 'ss', 'ss', 'ss', 'ekm', 'kerala'),
(2, 'a', 's', 'w', 'a@gmail.com', '233', '0000-00-00', 'female', '345', 'ret', 'ert', 'ert', 'f', 'w'),
(3, 'w', 'w', 'w', 'w@gmail.com', 'w', '0000-00-00', 'female', '111', 'w', 'w', 'w', 'w', 'w'),
(7, 'amal', 'raju', 'kudilil', 'amal12@gmail.com', '685667', '0000-00-00', 'male', '6789564563', 'amal', 'amal', 'amal', 'ekm', 'kerala'),
(8, 'Akhil', 'Cyriac', 'asdfghjk', 'akki@gmail.com', '685552', '0000-00-00', 'male', '9632587413', 'akki', '123', '123', 'idukki', 'kerala'),
(9, 'binu ', 'M B', 'fgthyjucvg', 'akki@gmail.com', '8569636', '0000-00-00', 'male', '9632587413', 'binu', '123', '123', 'sdscv', 'andra');

-- --------------------------------------------------------

--
-- Table structure for table `cust_order`
--

CREATE TABLE `cust_order` (
  `orderid` int(11) NOT NULL,
  `cid` int(11) NOT NULL,
  `mid` int(11) NOT NULL,
  `pid` int(11) NOT NULL,
  `amount` int(11) NOT NULL,
  `qty` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `mob` varchar(50) NOT NULL,
  `loc` varchar(50) NOT NULL,
  `atype` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cust_order`
--

INSERT INTO `cust_order` (`orderid`, `cid`, `mid`, `pid`, `amount`, `qty`, `name`, `mob`, `loc`, `atype`) VALUES
(19, 3, 2, 14, 17999, 1, '', '', '', ''),
(20, 3, 2, 14, 17999, 1, '', '', '', ''),
(21, 7, 2, 15, 6999, 1, '', '', '', ''),
(22, 7, 2, 15, 6999, 1, '', '', '', ''),
(23, 7, 2, 15, 6999, 1, '', '', '', ''),
(24, 7, 2, 15, 6999, 1, '', '', '', ''),
(25, 7, 2, 15, 6999, 1, '', '', '', ''),
(26, 7, 2, 15, 6999, 1, '', '', '', ''),
(27, 7, 2, 15, 6999, 1, '', '', '', ''),
(28, 7, 2, 15, 6999, 1, '', '', '', ''),
(29, 7, 2, 15, 6999, 1, '', '', '', ''),
(30, 7, 2, 15, 6999, 1, '', '', '', ''),
(31, 7, 2, 15, 6999, 1, '', '', '', ''),
(32, 3, 2, 13, 17999, 1, '', '', '', ''),
(33, 3, 2, 14, 17999, 1, '', '', '', ''),
(34, 8, 2, 14, 17999, 1, '', '', '', ''),
(35, 3, 2, 17, 6799, 1, '', '', '', ''),
(36, 3, 2, 13, 17999, 1, '', '', '', ''),
(37, 3, 2, 12, 2600, 1, '', '', '', ''),
(38, 3, 2, 15, 6999, 1, '', '', '', ''),
(39, 3, 2, 14, 17999, 1, 'Anjaa', '8523697523', 'rajakumari', 'office'),
(40, 3, 2, 13, 17999, 1, 'Anjaa', '8523697523', 'rajakumari', 'office'),
(41, 9, 6, 21, 6000, 1, 'kannan', '7856932563', 'parakkadav', 'home');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `uname` varchar(30) NOT NULL,
  `password` varchar(50) NOT NULL,
  `type` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`uname`, `password`, `type`) VALUES
('w', 'w', 'customer'),
('k', 'k', 'marchant'),
('prashob', '123', 'marchant'),
('', '', 'customer'),
('', '', 'customer'),
('', '', 'marchant'),
('amal', 'amal', 'customer'),
('eldhose', 'eldhose', 'marchant'),
('akki', '123', 'customer'),
('ajas', '123', 'marchant'),
('binu', '123', 'customer');

-- --------------------------------------------------------

--
-- Table structure for table `merchantreg`
--

CREATE TABLE `merchantreg` (
  `mrid` int(15) NOT NULL,
  `name` varchar(30) NOT NULL,
  `owner` varchar(30) NOT NULL,
  `address` varchar(30) NOT NULL,
  `district` varchar(30) NOT NULL,
  `state` varchar(30) NOT NULL,
  `pin` varchar(20) NOT NULL,
  `phone` varchar(30) NOT NULL,
  `email` varchar(30) NOT NULL,
  `username` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  `cpassword` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `merchantreg`
--

INSERT INTO `merchantreg` (`mrid`, `name`, `owner`, `address`, `district`, `state`, `pin`, `phone`, `email`, `username`, `password`, `cpassword`) VALUES
(1, 'eee', 'd', 'd', 'd', 'd', '233', 'sd', 'a@gmail.com', 'd', 'd', 'd'),
(2, 'k', 'k', 'k', 'k', 'k', 'k', 'k', 'a@gmail.com', 'k', 'k', 'k'),
(3, 'Prashob', 'Prashob', 'LCC', 'Ernakulam', 'Kerala', '682033', '8547532288', 'prashob@gmail.com', 'prashob', '123', '123'),
(5, 'eldhose', 'wes', 'chennattu ,onakkoor', 'ekm', 'kerala', '686667', '9400408552', 'eldhoseraj018@gmail.com', 'eldhose', 'eldhose', 'eldhose'),
(6, 'abhinav', 'ajas', 'yhjukill', 'ernakulam', 'kerala', '569252', '9874563214', 'ajas@gmail.com', 'ajas', '123', '123');

-- --------------------------------------------------------

--
-- Table structure for table `model`
--

CREATE TABLE `model` (
  `mid` int(10) NOT NULL,
  `cid` int(30) NOT NULL,
  `scid` int(15) NOT NULL,
  `bid` int(30) NOT NULL,
  `mname` varchar(1000) NOT NULL,
  `spec` varchar(200) NOT NULL,
  `price` varchar(30) NOT NULL,
  `pic` varchar(100) NOT NULL,
  `qty` int(11) NOT NULL,
  `merchid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `model`
--

INSERT INTO `model` (`mid`, `cid`, `scid`, `bid`, `mname`, `spec`, `price`, `pic`, `qty`, `merchid`) VALUES
(12, 3, 3, 3, 'blurv1', 'multicolor', '2600', 'static/media/combo-5-1219-1221-1140-472-1077-10-swiggy-multicolor-original-imaf9zgvgdjujaqq.jpeg', 12, 2),
(13, 1, 1, 1, 's11', 'hd display', '17999', 'static/media/tv22.jpg', -9, 2),
(14, 2, 2, 2, 's11', 'ram hige', '17999', 'static/media/m1.jpg', 2, 2),
(15, 1, 4, 4, 'All New Fire HD   Tablet    HD Display  Wi Fi     GB   Includes Special Offers  Magenta', 'All New Fire HD   Tablet    HD Display  Wi Fi     GB   Includes Special Offers  Magenta', '6999', 'static/media/tablet.jpg', -4, 2),
(16, 1, 4, 4, 'Fire HD 8 Tablet with Alexa, 8 HD Display, 16 GB, Tangerine - with Special Offers,', 'HD 8 Tablet with Alexa, 8 HD Display, 16 GB, Tangerine - with Special Offers', '9888', 'static/media/tb2.jpg', 9, 2),
(17, 1, 4, 4, 'Fire Tablet, 7 Display, Wi-Fi, 8 GB - Includes Special Offers, Magenta', ' 7 Display, Wi-Fi, 8 GB - Includes Special Offers, Magenta', '6799', 'static/media/tb3.jpg', 9, 2),
(20, 3, 3, 3, 'mkji', 'wertyuio', '2000', 'static/media/IMG-20200220-WA0008.jpg', 8, 2),
(21, 2, 2, 2, 'Redmi 5A', 'qazxcvbnmlp', '6000', 'static/media/IMG-20200220-WA0007.jpg', 2, 6);

-- --------------------------------------------------------

--
-- Table structure for table `review`
--

CREATE TABLE `review` (
  `rid` int(11) NOT NULL,
  `cus_id` int(11) NOT NULL,
  `cid` int(11) NOT NULL,
  `scid` int(11) NOT NULL,
  `bid` int(11) NOT NULL,
  `mid` int(11) NOT NULL,
  `comment` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `review`
--

INSERT INTO `review` (`rid`, `cus_id`, `cid`, `scid`, `bid`, `mid`, `comment`) VALUES
(1, 1, 1, 4, 0, 15, 'bad in nature, bad disply,using not easy due to heavy weight '),
(2, 1, 1, 4, 0, 15, 'bad in nature, bad disply,using not easy due to heavy weight '),
(3, 1, 1, 1, 0, 13, 'bad in nature, bad disply,using not easy due to heavy weight '),
(4, 1, 1, 1, 0, 13, 'bad in nature, bad disply,using not easy due to heavy weight '),
(5, 1, 1, 1, 0, 13, 'bad in nature, bad disply,using not easy due to heavy weight '),
(6, 1, 1, 1, 0, 13, 'bad in nature, bad disply,using not easy due to heavy weight '),
(7, 1, 1, 4, 0, 16, 'bad in nature, bad disply,using not easy due to heavy weight '),
(8, 1, 1, 4, 0, 16, 'bad in nature, bad disply,using not easy due to heavy weight '),
(9, 1, 1, 1, 0, 13, 'bad in nature, bad disply,using not easy due to heavy weight '),
(10, 1, 2, 2, 0, 14, 'bad in nature, bad disply,using not easy due to heavy weight '),
(11, 1, 1, 1, 0, 13, 'bad in nature, bad disply,using not easy due to heavy weight '),
(12, 1, 1, 1, 0, 13, 'bad in nature, bad disply,using not easy due to heavy weight '),
(13, 1, 2, 2, 0, 14, 'bad in nature, bad disply,using not easy due to heavy weight '),
(14, 1, 1, 1, 0, 13, 'bad in nature, bad disply,using not easy due to heavy weight '),
(15, 1, 1, 1, 0, 13, 'bad in nature, bad disply,using not easy due to heavy weight '),
(16, 1, 2, 2, 0, 14, 'asaasdfhtyryrtfrty5r5gukyli8'),
(17, 1, 2, 2, 0, 14, 'asaasdfhtyryrtfrty5r5gukyli8'),
(18, 1, 1, 1, 0, 13, 'bad in nature, bad disply,using not easy due to heavy weight '),
(19, 1, 2, 2, 0, 14, 'bad in nature, bad disply,using not easy due to heavy weight '),
(20, 1, 2, 2, 0, 14, 'asaasdfhtyryrtfrty5r5gukyli8'),
(21, 1, 2, 2, 0, 14, 'bad in nature, bad disply,using not easy due to heavy weight '),
(22, 1, 2, 2, 0, 14, 'asaasdfhtyryrtfrty5r5gukyli8'),
(23, 1, 2, 2, 0, 14, 'bad in nature, bad disply,using not easy due to heavy weight '),
(24, 1, 2, 2, 0, 14, 'bad in nature, bad disply,using not easy due to heavy weight '),
(25, 1, 2, 2, 0, 14, 'asaasdfhtyryrtfrty5r5gukyli8'),
(26, 1, 1, 4, 0, 15, 'asaasdfhtyryrtfrty5r5gukyli8'),
(27, 1, 2, 2, 0, 14, 'bad in nature, bad disply,using not easy due to heavy weight '),
(28, 1, 2, 2, 0, 14, 'gud display'),
(29, 1, 2, 2, 0, 14, 'good display'),
(30, 1, 2, 2, 0, 14, 'gud features gud ram'),
(31, 1, 3, 3, 0, 12, 'hello thg'),
(32, 1, 2, 2, 0, 14, 'hello thg'),
(33, 1, 1, 1, 0, 13, 'not sagsbhsd'),
(34, 1, 2, 2, 0, 21, 'battery life is low'),
(35, 1, 3, 3, 0, 20, 'not sagsbhsd'),
(36, 9, 3, 3, 0, 20, 'not sagsbhsd'),
(37, 9, 1, 1, 0, 13, 'not ok');

-- --------------------------------------------------------

--
-- Table structure for table `subcatogory`
--

CREATE TABLE `subcatogory` (
  `scid` int(15) NOT NULL,
  `cid` int(15) NOT NULL,
  `scname` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `subcatogory`
--

INSERT INTO `subcatogory` (`scid`, `cid`, `scname`) VALUES
(1, 1, 'TV'),
(2, 2, 'Smartphone'),
(3, 3, 'shoes'),
(4, 1, 'Tablet'),
(9, 5, 'phone');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `brand`
--
ALTER TABLE `brand`
  ADD PRIMARY KEY (`bid`);

--
-- Indexes for table `cart`
--
ALTER TABLE `cart`
  ADD PRIMARY KEY (`cartid`);

--
-- Indexes for table `catogory`
--
ALTER TABLE `catogory`
  ADD PRIMARY KEY (`cid`);

--
-- Indexes for table `cusreg`
--
ALTER TABLE `cusreg`
  ADD PRIMARY KEY (`cus_id`);

--
-- Indexes for table `cust_order`
--
ALTER TABLE `cust_order`
  ADD PRIMARY KEY (`orderid`);

--
-- Indexes for table `merchantreg`
--
ALTER TABLE `merchantreg`
  ADD PRIMARY KEY (`mrid`);

--
-- Indexes for table `model`
--
ALTER TABLE `model`
  ADD PRIMARY KEY (`mid`);

--
-- Indexes for table `review`
--
ALTER TABLE `review`
  ADD PRIMARY KEY (`rid`);

--
-- Indexes for table `subcatogory`
--
ALTER TABLE `subcatogory`
  ADD PRIMARY KEY (`scid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `brand`
--
ALTER TABLE `brand`
  MODIFY `bid` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `cart`
--
ALTER TABLE `cart`
  MODIFY `cartid` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `catogory`
--
ALTER TABLE `catogory`
  MODIFY `cid` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `cusreg`
--
ALTER TABLE `cusreg`
  MODIFY `cus_id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `cust_order`
--
ALTER TABLE `cust_order`
  MODIFY `orderid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=42;

--
-- AUTO_INCREMENT for table `merchantreg`
--
ALTER TABLE `merchantreg`
  MODIFY `mrid` int(15) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `model`
--
ALTER TABLE `model`
  MODIFY `mid` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `review`
--
ALTER TABLE `review`
  MODIFY `rid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- AUTO_INCREMENT for table `subcatogory`
--
ALTER TABLE `subcatogory`
  MODIFY `scid` int(15) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
