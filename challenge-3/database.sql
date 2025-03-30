-- given the following table definitions, write a query to find the percentage of users who returned to log in within 7 days of their first login
create table logins (
    user_id INT NOT NULL,
    login_date DATE NOT NULL,
    PRIMARY KEY (user_id, login_date)
);

-- return perc
SELECT COUNT * 100 / (SELECT COUNT FROM logins) AS perc FROM logins WHERE login_date >= CURRENT_DATE - INTERVAL 7 DAY;