--
-- Table structure for table `authtoken_token`
--

CREATE TABLE IF NOT EXISTS `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


--
-- Indexes for table `authtoken_token`
--
ALTER TABLE `authtoken_token`
 ADD PRIMARY KEY (`key`), ADD UNIQUE KEY `user_id` (`user_id`);


--
-- Constraints for table `authtoken_token`
--
ALTER TABLE `authtoken_token`
ADD CONSTRAINT `authtoken_token_user_id_535fb363_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

