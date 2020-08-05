CREATE DATABASE IF NOT EXISTS cse4701f19_project2;
USE cse4701f19_project2;
CREATE TABLE account (
 account_no INT(11) NOT NULL AUTO_INCREMENT,
 name_on_account VARCHAR(100) NOT NULL,
 balance FLOAT NOT NULL DEFAULT '0',
 account_open_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
 PRIMARY KEY (account_no)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


INSERT INTO account (account_no, name_on_account, balance, account_open_date) VALUES ()
