
SELECT DISTINCT CITY FROM STATION WHERE CITY NOT REGEXP '[aeoiu]$' AND CITY NOT REGEXP '^[aeoiu]';