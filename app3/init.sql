-- Create a new schema
CREATE SCHEMA my_schema;

-- Create a new table in the schema
CREATE TABLE my_schema.users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert initial data into the table
INSERT INTO my_schema.users (username, email) VALUES ('kuber', 'kuber@rappi.com');
INSERT INTO my_schema.users (username, email) VALUES ('netes', 'netes@rappi.com');
