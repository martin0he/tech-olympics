-- given the following table definitions, write a query to find the percentage of users who returned to log in within 7 days of their first login
create table logins (
    user_id INT NOT NULL,
    login_date DATE NOT NULL,
    PRIMARY KEY (user_id, login_date)
);

-- answer
SELECT ROUND(100 * COUNT(DISTINCT t2.user_id) / COUNT(DISTINCT t1.user_id), 2) AS perc
FROM logins t1
LEFT JOIN logins t2
ON t1.user_id = t2.user_id
AND t2.login_date > t1.login_date
AND t2.login_date <= t1.login_date + INTERVAL 7 DAY
WHERE t1.login_date = (SELECT MIN(t3.login_date) FROM logins t3 WHERE t3.user_id = t1.user_id);
