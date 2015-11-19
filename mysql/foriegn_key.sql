ALTER TABLE `Customer_Data`.`Sales` 
ADD INDEX `fk_Sales_1_idx` (`CustomerId` ASC),
ADD INDEX `fk_Sales_2_idx` (`PeriodId` ASC),
ADD INDEX `fk_ProductId_idx` (`ProductId` ASC);
ALTER TABLE `Customer_Data`.`Sales` 
ADD CONSTRAINT `fk_CustomerId`
  FOREIGN KEY (`CustomerId`)
  REFERENCES `Customer_Data`.`Customer` (`CustomerId`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_PeriodId`
  FOREIGN KEY (`PeriodId`)
  REFERENCES `Customer_Data`.`Period` (`PeriodId`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_StoreId`
  FOREIGN KEY (`StoreId`)
  REFERENCES `Customer_Data`.`Store` (`StoreId`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_ProductId`
  FOREIGN KEY (`ProductId`)
  REFERENCES `Customer_Data`.`Product` (`ProductId`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;
