DROP TABLE IF EXISTS User;
CREATE TABLE User (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(32) NOT NULL UNIQUE,
    password VARCHAR(32) NOT NULL,
    truename VARCHAR(32) NOT NULL,
    state INTEGER NOT NULL,
    address VARCHAR(64) NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO User (username,password,truename,state,address) VALUES ('admin', 'c7a2179db92593c9b4c91a1073c5f5f7', 'huang', 1,'jiangmen');


