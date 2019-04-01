DROP TABLE IF EXISTS User;
CREATE TABLE User (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(32) NOT NULL,
    password VARCHAR(32) NOT NULL,
    truename VARCHAR(32) NOT NULL,
    state INTEGER NOT NULL,
    address VARCHAR(64) NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO User (username,password,truename,state,address) VALUES ('jiege', '71ddea9bfda25dffd4bbc1c323aa6715', 'huang', 1,'jiangmen');



