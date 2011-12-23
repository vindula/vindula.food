SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL';

CREATE SCHEMA IF NOT EXISTS `myvindulaDB` DEFAULT CHARACTER SET latin1 ;
USE `myvindulaDB` ;

-- -----------------------------------------------------
-- Table `myvindulaDB`.`vin_food_specialty`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`vin_food_specialty` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`vin_food_specialty` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `name` VARCHAR(45) NULL DEFAULT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
AUTO_INCREMENT = 7
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `myvindulaDB`.`vin_food_restaurant`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`vin_food_restaurant` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`vin_food_restaurant` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `name` VARCHAR(45) NULL DEFAULT NULL ,
  `address` VARCHAR(100) NULL DEFAULT NULL ,
  `phone_number` VARCHAR(45) NULL DEFAULT NULL ,
  `delivery` TINYINT(1) NULL DEFAULT NULL ,
  `opening_hours` VARCHAR(45) NULL DEFAULT NULL ,
  `has_agreement` INT(1) NULL DEFAULT NULL ,
  `agreement` VARCHAR(45) NULL DEFAULT NULL ,
  `vin_food_specialty_id` INT(11) NOT NULL ,
  PRIMARY KEY (`id`) ,
  INDEX `fk_vin_food_restaurant_vin_food_specialty1` (`vin_food_specialty_id` ASC) ,
  CONSTRAINT `fk_vin_food_restaurant_vin_food_specialty1`
    FOREIGN KEY (`vin_food_specialty_id` )
    REFERENCES `myvindulaDB`.`vin_food_specialty` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 7
DEFAULT CHARACTER SET = latin1;



SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
