/*******************************************************************************
   Drop database if it exists
********************************************************************************/
DROP DATABASE IF EXISTS `Customer_Data`;


/*******************************************************************************
   Create database
********************************************************************************/
CREATE DATABASE `Customer_Data`;


USE `Customer_Data`;


/*******************************************************************************
   Create Tables
********************************************************************************/

CREATE TABLE `Customer`
(
    `CustomerId` INT NOT NULL,
    `FirstName` NVARCHAR(20) NOT NULL,
    `LastName` NVARCHAR(20) NOT NULL,	
    `Zipcode` INT NOT NULL,
    `Age` INT,
    `Gender` NVARCHAR(10),
    CONSTRAINT `PK_Customer` PRIMARY KEY  (`CustomerId`)
);
