MariaDB默认的存储引擎是Maria，不是MyISAM。Maria可以支持事务，但是默认情况下没有打开事务支持
打开事务 ALTER TABLE tablename ENGINE=MARIA TRANSACTIONAL=1;