-- init.sql
CREATE TABLE IF NOT EXISTS test_bd (
    id SERIAL PRIMARY KEY,
    some_text VARCHAR(255) NOT NULL
);
