# Python Modules
Repository for general purpose Python modules.<br>
These modules are intended for example purposes, but can also be used as-is or as a basis for use within other projects.

Note: Modules written using **Python 3**.
<br>
<br>

## SMTP Modules
The **smtp** directory contains modules related to sending emails via SMTP.
<br>
<br>
Note: In the test modules, you will need to ***change the example values*** for SMTP server login etc.

### Plaintext
Module **freedom35_smtp_plaintext.py** contains a method to demonstrate sending plaintext emails.
<br>
For usage, refer to example code in **test_smtp_plaintext.py**.
<br>
To run **test_smtp_plaintext.py**, use command line:<br>
```sh
$ python3 test_smtp_plaintext.py
```
### MIME (Multipurpose Internet Mail Extensions)
Module **freedom35_smtp_mime.py** contains a class to handle sending MIME emails.
<br>
For usage, refer to example code in **test_smtp_mime.py**.
<br>
To run **test_smtp_mime.py**, use command line:<br>
```sh
$ python3 test_smtp_mime.py
```
<br>
  
## Database Module
The **database** directory contains modules related to SQLite v3 database operations.
<br>
<br>
Module **freedom35_database.py** contains a class to demonstrate simple database operations.
<br>
For usage, refer to example code in **test_database.py**.
<br>
To run **test_database.py**, use command line:<br>
```sh
$ python3 test_database.py
```
Note: The test example uses an in-memory database, but you can change the database name to use a file instead. i.e. **test.db**.
