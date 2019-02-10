/*
Enter your query here.
*/
select CITY, length(CITY) from station order by length(CITY), CITY limit 1; 
select CITY, length(CITY) from station order by length(CITY) desc limit 1;