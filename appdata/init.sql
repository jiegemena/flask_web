DROP TABLE IF EXISTS jguser;
CREATE TABLE jguser (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(32) NOT NULL UNIQUE,
    password VARCHAR(32) NOT NULL,
    truename VARCHAR(32) NOT NULL,
    loginguid VARCHAR(63),
    state INTEGER NOT NULL,
    address VARCHAR(64) NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO jguser (username,password,truename,state,address) VALUES ('admin', '64fc25a5c1a8692d6593e422e9ee80e9', 'huang', 1,'jiangmen');

DROP TABLE IF EXISTS jgservers;
CREATE TABLE jgservers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    jgname VARCHAR(32) NOT NULL UNIQUE,
    jghost VARCHAR(32) NOT NULL,
    jgport INTEGER NOT NULL,
    jgstate INTEGER NOT NULL,
    jgaddtime VARCHAR(32) NOT NULL
);




