CREATE TABLE table5u (x DOUBLE, y DOUBLE) ROW FORMAT DELIMITED FIELDS TERMINATED BY ",";
LOAD DATA LOCAL INPATH '/Users/hduser/workspace/CRegressionRDBM/data/file5u.csv' INTO TABLE table5u;