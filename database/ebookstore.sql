-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 23, 2022 at 05:17 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ebookstore`
--

-- --------------------------------------------------------

--
-- Table structure for table `author`
--

CREATE TABLE `author` (
  `id` int(11) NOT NULL,
  `auth_name` varchar(50) NOT NULL,
  `auth_email` varchar(50) NOT NULL,
  `auth_pass` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `author`
--

INSERT INTO `author` (`id`, `auth_name`, `auth_email`, `auth_pass`) VALUES
(1, 'Sathya', 'sathyarajsaliyan@gmail.com', 'pbkdf2:sha256:260000$EpqY4X8KKJkzXqPW$52f2026ac07a7f089519b46a06e3b5a6fd892a5862e62afc36ba4da309b5eb92'),
(2, 'cde', 'cde@gmail.com', 'pbkdf2:sha256:260000$6Kz6CQLEP6tSedMX$402f8d5c30d75e1d1927df1bbe631f1bf77a71e61386153ba2dd56c6ed20f3cf'),
(3, 'pop', 'pop@gmail.com', 'pbkdf2:sha256:260000$RAf0fvm25Wnp1OHe$510000ea26537329ac4c1882cb7827bae28fea782b3160b308068506c667de87'),
(4, 'tgv', 'tgv@gmail.com', 'pbkdf2:sha256:260000$J0NKiTSEksCwbMIp$1daf3041e8408c2ef2c6ca9ba028d18cffc650d0e3d6bad3b48c0e842e019da7');

-- --------------------------------------------------------

--
-- Table structure for table `book`
--

CREATE TABLE `book` (
  `book_id` int(11) NOT NULL,
  `book_title` varchar(50) DEFAULT NULL,
  `book_desc` varchar(1000) DEFAULT NULL,
  `price` varchar(10) NOT NULL,
  `book_img` varchar(1000) DEFAULT NULL,
  `doc_name` varchar(1000) DEFAULT NULL,
  `auth_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `book`
--

INSERT INTO `book` (`book_id`, `book_title`, `book_desc`, `price`, `book_img`, `doc_name`, `auth_id`) VALUES
(7, 'afadad', 'ccccscscc', '340', 'afadadc-no_83.v1.jpg', 'afadad18CS54_ATC_Assignment_Rubrics.pdf', 2),
(8, 'The Daemon', 'dfkdfkn', 'Free', 'The Daemonc-no_83.jpg', 'The Daemon123.pdf', 4),
(9, 'The Daemon', 'dmcc', 'Free', 'The Daemonc-no_83.v1.jpg', 'The Daemon123.pdf', 4),
(10, 'The Daemoncc', 'c cccscs', 'Free', 'The Daemonccc-no_83.jpg', 'The Daemoncc123.pdf', 4),
(16, 'BANKAI', 'ICHIGOOOOO', '1300', 'BANKAIWhatsApp_Image_2021-10-02_at_11.29.01_AM.jpeg', 'BANKAI123.pdf', 4),
(17, 'BANKAI', 'ICHIGOOOOO', '1300', 'BANKAIWhatsApp_Image_2021-10-02_at_11.29.01_AM.jpeg', 'BANKAI123.pdf', 4),
(18, 'The Daemoncc', ',khugyftdrs', 'Free', 'The Daemonccimage.png', 'The Daemoncc4SO19CS138_4th_semresults.pdf', 4),
(19, 'The Daemoncc', ',khugyftdrs', 'Free', 'The Daemonccimage.png', 'The Daemoncc4SO19CS138_4th_semresults.pdf', 4),
(20, 'The Daemoncc', 'figirgeas', 'Free', 'The Daemonccimage.png', 'The Daemoncc18CS54_ATC_Assignment_Rubrics.pdf', 4),
(21, 'FFAAFDA', 'JVNDSIONGVOI', '67890', 'FFAAFDAwallpaperflare.com_wallpaper.jpg', 'FFAAFDACN-Lab_PartA_programs.pdf', 3),
(22, 'RICH DAD', 'OIEDHHHHJJJJJJG G GGGGGGGGG GKGGJGOIHG O HGFOHG  OUFGH OG OFHGOHHGIOSHEFHPSIUHIHPH U GUES VOI GOEO OHS OH GOSOUHG  UGHGHGHGI IH IGH IGJ GIH GII G IG GI RIUHV ERTNVHETVNEURTVNERUTVNERUTNVHEIUT VTUHNIETU EIUTNHEITUHN IENTHIEUTHNIH HUEGNHEHTNTEUNHEUTNH', 'Free', 'RICH DADc-no_83.jpg', 'RICH DAD123.pdf', 4),
(23, 'THE GANGSTER', 'YEEEHAWWWWWWWW', '450', 'THE GANGSTERIMG_20210505_154812.jpg', 'THE GANGSTERCN-Lab_PartA_programs.pdf', 3);

-- --------------------------------------------------------

--
-- Table structure for table `reader`
--

CREATE TABLE `reader` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `reader`
--

INSERT INTO `reader` (`id`, `username`, `email`, `password`) VALUES
(1, 'abc', 'abc@gmail.com', 'pbkdf2:sha256:260000$0yuavwIHkq2h7OSf$1bfa9f8ee31758f5ad5e3f92b861a084ec2ab170b426e798d00a02791f4e9307'),
(2, 'xyz', 'xyz@gmail.com', 'pbkdf2:sha256:260000$OYJF7YWwLLBHPL3a$3ac82ac975fa3110d8d9cdede7681d4e7d6e4eb9011b45c1000f24033f161132'),
(3, 'qwe', 'qwe@gmail.com', 'pbkdf2:sha256:260000$H6PimHxhIKQ929MA$ff8b0364462863b5da611235c92c25b19eba4aa6ee9cf9e70b9a91e8811ea334'),
(4, 'poq', 'poq@gmail.com', 'pbkdf2:sha256:260000$YqIYoTeAcfpAurdj$6d867275318e2205cd5f545f9412b2dfba774045f67f99b989c8194b147e0c90'),
(5, 'zxc', 'zxc@gmail.com', 'pbkdf2:sha256:260000$FXFo5cMbhV6qArLb$4ad60d87cd7f5f22108c8f55f6ab4a19a78c2549b657b5246c213a37e4f79680'),
(6, 'ujn', 'ujn@gmail.com', 'pbkdf2:sha256:260000$VeXR7sipUuCI3XXr$038e5fe0ed4b451779fd28570679714295ac091805bca4c1729d69338b9a2abd');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `author`
--
ALTER TABLE `author`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id` (`id`),
  ADD KEY `id_2` (`id`),
  ADD KEY `auth_pass` (`auth_pass`(768));

--
-- Indexes for table `book`
--
ALTER TABLE `book`
  ADD PRIMARY KEY (`book_id`),
  ADD KEY `fk_auth_id` (`auth_id`);

--
-- Indexes for table `reader`
--
ALTER TABLE `reader`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `remail` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `author`
--
ALTER TABLE `author`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `book`
--
ALTER TABLE `book`
  MODIFY `book_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `reader`
--
ALTER TABLE `reader`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `book`
--
ALTER TABLE `book`
  ADD CONSTRAINT `fk_auth_id` FOREIGN KEY (`auth_id`) REFERENCES `author` (`id`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
