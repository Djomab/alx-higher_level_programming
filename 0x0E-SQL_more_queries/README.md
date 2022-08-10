# 0x0E. SQL - More queries :ledger:

# Introduction
Deep into SQL queries.

# Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General
* How to create a new MySQL user
* How to manage privileges for a user to a database or table
* What’s a PRIMARY KEY
* What’s a FOREIGN KEY
* How to use NOT NULL and UNIQUE constraints
* How to retrieve datas from multiple tables in one request
* What are subqueries
* What are JOIN and UNION

# More Info

## Install MySQL 8.0 on Ubuntu

    $ sudo apt update
    $ sudo apt install mysql-server
    ...
    $ mysql --version
    mysql  Ver 8.0.30-0ubuntu0.22.04.1 for Linux on x86_64 ((Ubuntu))
    $

## Connect to MySQL server

    $ mysql -u root -p
    Enter password: 
    Welcome to the MySQL monitor.  Commands end with ; or \g.
    Your MySQL connection id is 28
    Server version: 8.0.30-0ubuntu0.22.04.1 (Ubuntu)

    Copyright (c) 2000, 2022, Oracle and/or its affiliates.

    Oracle is a registered trademark of Oracle Corporation and/or its
    affiliates. Other names may be trademarks of their respective
    owners.

    Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

    mysql> 

## How to import a SQL dump

    $ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
    Enter password: 
    $ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
    Enter password: 
    $ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
    Enter password: 
    id  name
    1   Drama
    2   Mystery
    3   Adventure
    4   Fantasy
    5   Comedy
    6   Crime
    7   Suspense
    8   Thriller
    $

## Cheatsheet

<img src="cheatsheetpng" style="margin-top: 10px; margin-bottom: 10px;">

# Tasks

0- Write a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).

1- Write a script that creates the MySQL server user user_0d_1.
* user_0d_1 should have all privileges on your MySQL server
* The user_0d_1 password should be set to user_0d_1_pwd
* If the user user_0d_1 already exists, your script should not fail