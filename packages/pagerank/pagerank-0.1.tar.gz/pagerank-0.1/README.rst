## Pranker
* Pranker is a tool to track the page rank of keywords and domains over time.
* It intends to be a free alternative to position.ly

### Initial Goals
* Support multiple users.
* 1 or 2 requests a day.

## MySQL
-- Create local database.
    CREATE DATABASE prank DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
-- Grant remote access.
    CREATE USER 'prank'@'localhost' IDENTIFIED BY 'prank';
    SET PASSWORD FOR 'prank'@'localhost' = PASSWORD('prank');
    GRANT ALL ON root.* TO 'prank'@'localhost';
    FLUSH PRIVILEGES;

## Backlog
* Write instructions on how to run the project

## Backlog
* Upgrade django to 1.7.x
* Parallelize requests to Google
