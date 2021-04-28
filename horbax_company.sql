-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 28 Nis 2021, 20:24:05
-- Sunucu sürümü: 10.4.18-MariaDB
-- PHP Sürümü: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `horbax company`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `article`
--

CREATE TABLE `article` (
  `id` int(11) NOT NULL,
  `title` text NOT NULL,
  `author` text NOT NULL,
  `content` text NOT NULL,
  `created_date` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Tablo döküm verisi `article`
--

INSERT INTO `article` (`id`, `title`, `author`, `content`, `created_date`) VALUES
(8, 'deneme 3', 'eiadooo', '<p><img alt=\"\" src=\"https://www.google.com/search?q=latakia&amp;sxsrf=ALeKk02bw5XC9A9lOVvW_wjCRJjd9ZJqSw:1619546351233&amp;source=lnms&amp;tbm=isch&amp;sa=X&amp;ved=2ahUKEwiG49ingJ_wAhUXhP0HHaatC88Q_AUoAnoECAEQBA#imgrc=qYezC-Af8B4LjM\" />&nbsp;</p>\r\n\r\n<p><strong>Latakia syria</strong></p>\r\n\r\n<p><img alt=\"\" src=\"https://lh3.googleusercontent.com/proxy/WHpYQNO_eIBj90ZWpkU5wSlkV85lzvKgOzs0GLHDW5JjiXMcTMkLcfcRwaXICRuTaeOxusBg7ISc6osmGhTDMbDiCyu9irezrJHjPNcOgkNxDKk4yeKWCJA6gWMjA05PmnEO\" /></p>\r\n', '2021-04-27 18:03:43'),
(9, 'Deneme 3', 'Ayaz.is', '<p>...نهاية مباراة ريال مدريد وتشيلسي بالتعادل الايجابي لهدف لكلا الفريقين بانتظار مباراة العودة في لندن</p>\r\n\r\n<p><img alt=\"\" src=\"https://media06.ligtv.com.tr/img/news/2021/4/27/real-madrid-1-1-chelsea/748_416/UCL-web_ma%C3%A7ozetleri.jpg\" /></p>\r\n', '2021-04-28 09:56:21'),
(10, 'Deneme kod', 'Ayaz.is', '<p>Deneme kodum&nbsp;</p>\r\n\r\n<p>&nbsp;</p>\r\n\r\n<pre class=\"prettyprint\">\r\nclass Voila {\r\npublic:\r\n  // Voila\r\n  static const string VOILA = &quot;Voila&quot;;\r\n\r\n  // will not interfere with embedded <a href=\"#voila2\">tags</a>.\r\n}</pre>\r\n', '2021-04-28 13:08:05');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `userss`
--

CREATE TABLE `userss` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `username` text NOT NULL,
  `password` text NOT NULL,
  `email` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Tablo döküm verisi `userss`
--

INSERT INTO `userss` (`id`, `name`, `username`, `password`, `email`) VALUES
(9, 'Eiad ismail', 'eiadooo', '$5$rounds=535000$lDQCa25wzc7Bipbk$BTe09VMglpAu9JnCyULthPY2TZ2DhoB4j48ooDdIk76', 'eiadismail@gmail.com'),
(10, 'Ayaz ismailoğlu', 'Ayaz.is', '$5$rounds=535000$3kF9TRIWgvp4IIpu$wN/RIHZMKVgaJI8uJzgY/nCFT3X.xWLu8ozv1m8VkD0', 'eiadismail@gmail.com');

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `article`
--
ALTER TABLE `article`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `userss`
--
ALTER TABLE `userss`
  ADD PRIMARY KEY (`id`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `article`
--
ALTER TABLE `article`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Tablo için AUTO_INCREMENT değeri `userss`
--
ALTER TABLE `userss`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
