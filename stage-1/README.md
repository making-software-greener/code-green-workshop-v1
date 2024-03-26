# shakespeare-searcher
This software stack was generated with [Compose Generator](https://www.compose-generator.com). <br>
The following sections contain instructions about the selected services and instructions for setting them up.

## Common Website
The common website container is based on nginx, providing the webserver functionality.

## FastAPI
FastAPI is a high-performance, easy to learn, fast to code and ready for production framework for building APIs. It is based on Python 3.6+ and can handle massive amounts of requests in parallel due to its asynchronous programming style.

### Setup
FastAPI is considered as backend service and can therefore be found in backends collection, when generating the compose configuration with Compose Generator.

### Usage
Compose Generator provides a basic Hello World API out of the box which can be found at the url root.

## MySQL Database
MySQL is a relational database.

### Setup
Compose Generator will ask you for the name of a dedicated database and the name of a dedicated user for your application. This database and user will be created on the first startup of the database container. Furthermore, the cli automatically generates a database user password for you, so you don't need to specify it yourself.

## Redis
Redis is a commonly used database, which is known for its high performance. Redis acts as a key-value store and can especially be useful for fast application or database caches.

### Setup
Compose Generator creates a password-protected instance per default. You can find the automatically generated password in the environment.env file.

## PhpMyAdmin
PhpMyAdmin is a database management tool for MySQL or MariaDB.

## Redis Insight
A database administration tool for the Redis database.

### Setup
After generating the stack, you can visit the website on the exposed port.
After accepting the eula, select "I already have a database" followed by "Connect to a Redis Database".

Then fill in the following data:
Host: `database-redis`
Port: `6379`
Name: Name of your choice
Username: leave blank
Password: the password in the environment.env file, which was generated

