-- User table.
CREATE TABLE IF NOT EXISTS user (
    id SERIAL,
    username VARCHAR(100) NOT NULL UNIQUE,
    email_address VARCHAR(255) NOT NULL UNIQUE,
    created_on DATETIME NOT NULL DEFAULT (DATETIME(CURRENT_TIMESTAMP, 'LOCALTIME')),
    created_by_id INT NOT NULL REFERENCES user(id) DEFAULT 0,
    updated_on DATETIME NOT NULL DEFAULT (DATETIME(CURRENT_TIMESTAMP, 'LOCALTIME')),
    updated_by_id INT NOT NULL REFERENCES user(id) DEFAULT 0
);

-- CREATE Admin user if one does not yet exist.
WITH exst AS (
    SELECT id
    FROM user 
    WHERE username = 'admin'
)
INSERT INTO user
(id, username, email_address)
SELECT 0 AS id, 'admin' AS username, 'nv@iiitd.ac.in' AS email_address
WHERE NOT EXISTS (SELECT id FROM exst);


-- Basic data table.
CREATE TABLE IF NOT EXISTS data ( 
    id SERIAL,
    reqdata VARCHAR(150) NOT NULL UNIQUE,
    created_on DATETIME NOT NULL DEFAULT (DATETIME(CURRENT_TIMESTAMP, 'LOCALTIME')),
    created_by_id INT NOT NULL REFERENCES user(id) DEFAULT 0,
    updated_on DATETIME NOT NULL DEFAULT (DATETIME(CURRENT_TIMESTAMP, 'LOCALTIME')),
    updated_by_id INT NOT NULL REFERENCES user(id) DEFAULT 0
);

-- req table.
CREATE TABLE IF NOT EXISTS req (
    id SERIAL,
    name VARCHAR(100) NOT NULL UNIQUE,
    created_on DATETIME NOT NULL DEFAULT (DATETIME(CURRENT_TIMESTAMP, 'LOCALTIME')),
    created_by_id INT NOT NULL REFERENCES user(id) DEFAULT 0,
    updated_on DATETIME NOT NULL DEFAULT (DATETIME(CURRENT_TIMESTAMP, 'LOCALTIME')),
    updated_by_id INT NOT NULL REFERENCES user(id) DEFAULT 0
);
