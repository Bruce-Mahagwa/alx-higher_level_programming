-- Lists number of records with the same score
SELECT score COUNT (score) "number" FROM hbtn_0c_0.second_table GROUP BY score
