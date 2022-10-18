# 0x14-javascript-web_scraping

# Resources
Read or watch:

- [Working with JSON data](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON)
- [The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco](https://medium.com/@vietkieutie/the-workflow-of-accessing-the-attributes-of-a-simply-created-json-object-82a5b33e2319)
- [request module](https://github.com/request/request)
- [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)

# Requirements
## General
* Allowed editors: `vi`, `vim`, `emacs`
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/node`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should be `semistandard` compliant. [Rules of Standard](https://standardjs.com/rules.html) + [semicolons](https://github.com/standard/semistandard) on top. Also as reference: AirBnB style
* All your files must be executable
* The length of your files will be tested using wc
* You are not allowed to use var
## More Info
### Install Node 10

    $ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
    $ sudo apt-get install -y nodejs

### Install semi-standard
#### [Documentation](https://github.com/standard/semistandard)

    $ sudo npm install semistandard --global
### Install request module and use it
#### [Documentation](https://github.com/request/request)

    $ sudo npm install request --global
    $ export NODE_PATH=/usr/lib/node_modules
Notes: Request module has been deprecated since February 2020 - the team is considering alternative to replace this module - however, it’s a really simple and powerful module for practicing web-scraping in JavaScript (and still used a lot in the industry).