-- Adds an average column
DECLARE @value AS FLOAT = SELECT AVG(scores) from hbtn_0c_0.second_table;
ALTER TABLE hbtn_0c_0.second_table ADD average INT
INSERT INTO hbtn_0c_0.second_table (average) VALUES `value`
