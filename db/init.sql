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

INSERT INTO User (username,password,truename,state,address) VALUES ('admin', '64fc25a5c1a8692d6593e422e9ee80e9', 'huang', 1,'jiangmen');


