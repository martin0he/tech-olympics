-- given the following table definitions, write a query to find the percentage of users who returned to log in within 7 days of their first login
create table logins (
    user_id INT NOT NULL,
    login_date DATE NOT NULL,
    PRIMARY KEY (user_id, login_date)
);

SELECT count(*) * 100.0 / (select count(*) from logins)
FROM logins
WHERE DATEDIFF(day, CURRENT_DATE, login_date) < 7;