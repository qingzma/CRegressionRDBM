CREATE TABLE table1u (x DOUBLE, y DOUBLE) ROW FORMAT DELIMITED FIELDS TERMINATED BY ",";
LOAD DATA LOCAL INPATH '/Users/hduser/workspace/CRegressionRDBM/data/file1u.csv' INTO TABLE table1u;