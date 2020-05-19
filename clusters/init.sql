CREATE DATABASE "avitotest";
CREATE USER "avitotest" WITH LOGIN;
ALTER USER "avitotest" WITH PASSWORD 'verystrongpassword';

CREATE TABLE IF NOT EXISTS edges
    (
        n1 integer,
        n2 integer,
        unique(n1, n2)
    );

CREATE TABLE IF NOT EXISTS clusters
    (
        n integer,
        c integer,
        unique(n, c)
    );

INSERT INTO edges (n1, n2) VALUES (1, 2);
INSERT INTO edges (n1, n2) VALUES (1, 3);
INSERT INTO edges (n1, n2) VALUES (2, 3);
INSERT INTO edges (n1, n2) VALUES (3, 5);
INSERT INTO edges (n1, n2) VALUES (4, 6);
INSERT INTO edges (n1, n2) VALUES (5, 6);
INSERT INTO edges (n1, n2) VALUES (5, 7);
INSERT INTO edges (n1, n2) VALUES (6, 8);
INSERT INTO edges (n1, n2) VALUES (7, 9);
INSERT INTO edges (n1, n2) VALUES (8, 10);
INSERT INTO edges (n1, n2) VALUES (8, 11);
INSERT INTO edges (n1, n2) VALUES (8, 9);
INSERT INTO edges (n1, n2) VALUES (9, 10);
INSERT INTO edges (n1, n2) VALUES (12, 13);
INSERT INTO edges (n1, n2) VALUES (13, 14);
INSERT INTO edges (n1, n2) VALUES (13, 15);
INSERT INTO edges (n1, n2) VALUES (16, 17);