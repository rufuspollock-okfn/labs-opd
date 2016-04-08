#--- brand type
INSERT INTO opd2.browser_brand_type
SELECT * FROM opd.brand_type;

#---  gs1 gcp rc (codes 55 and 88 missing)
INSERT INTO opd2.browser_gs1_gcp_rc
SELECT * FROM opd.gs1_gcp_rc;

#--- gs1_gcp
INSERT INTO opd2.browser_gs1_gcp
SELECT * FROM opd.gs1_gcp;

#--- brand owner
INSERT INTO opd2.browser_brand_owner
SELECT * FROM opd.brand_owner;

#--- data corrections
INSERT INTO `opd`.`brand` (`BSIN`, `BRAND_NM`, `BRAND_TYPE_CD`) VALUES ('000001', 'Cheese generic group', '1');
INSERT INTO `opd`.`brand` (`BSIN`, `BRAND_NM`, `BRAND_TYPE_CD`) VALUES ('000002', 'Alcohol generic group', '1');
INSERT INTO `opd`.`brand` (`BSIN`, `BRAND_NM`, `BRAND_TYPE_CD`) VALUES ('000003', 'Music generic group', '1');

#--- brand owner bsin
ALTER TABLE `opd`.`brand` 
ADD COLUMN `OWNER_CD` INT NULL AFTER `BRAND_LINK`;
SET SQL_SAFE_UPDATES = 0;
update  opd.brand_owner_bsin b, opd.brand a  set a.owner_cd = b.owner_cd where a.bsin = b.bsin;

#--- brand
INSERT INTO opd2.browser_brand
SELECT * FROM opd.brand;

#--- gs1 gpc
INSERT INTO opd2.browser_gs1_gpc
SELECT * FROM opd.gs1_gpc where gpc_lang = 'en';

#--- data corrections
SET SQL_SAFE_UPDATES = 0;
update opd.gtin set gpc_c_cd = null where gpc_c_cd in ('68060600','50122900');
update opd.gtin set gpc_f_cd = null where gpc_f_cd in ('68060000');
update opd.gtin set gpc_b_cd = null where gpc_b_cd in ('10000224');

#--- gtin
INSERT INTO opd2.browser_gtin
SELECT * FROM opd.gtin;

#--- nutrition us
INSERT INTO opd2.browser_nutrition
SELECT * FROM opd.nutrition_us;

#--- gs1 gpc hier
INSERT INTO opd2.browser_gs1_gpc_hier
SELECT * FROM opd.gs1_gpc_hier;



