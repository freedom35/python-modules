# Python Modules
Repository for general purpose Python modules.  
These modules are intended for example purposes, but can also be used as-is or as a basis for use within other projects.

Note: Modules written using [Python 3](https://www.python.org/downloads/).  
  
<br />
  
## SMTP Modules
The **smtp** directory contains modules related to sending emails via SMTP.  
  
Note: In the test modules, you will need to ***change the example values*** for SMTP server login etc.  
  
  
### Plaintext
Module **freedom35/smtp/plaintext.py** contains a method to demonstrate sending plaintext emails.  
  
For usage, refer to example code in **test_smtp_plaintext.py**.  
To run **test_smtp_plaintext.py**, use command line:  
```sh
$ python3 test_smtp_plaintext.py
```
  
  
### MIME (Multipurpose Internet Mail Extensions)
Module **freedom35/smtp/mime.py** contains a class to handle sending MIME emails.  
  
For usage, refer to example code in **test_smtp_mime.py**. 
To run **test_smtp_mime.py**, use command line:  
```sh
$ python3 test_smtp_mime.py
```
  
<br />
  
## Database Module
The **freedom/database** directory contains modules related to SQLite v3 database operations.  
  
Module **freedom35/database/sqlite.py** contains a class to demonstrate simple database operations.  
  
For usage, refer to example code in **test_database.py**.  
To run **test_database.py**, use command line:  
```sh
$ python3 test_database.py
```
  
Note: The test example uses an in-memory SQLite database (**:memory:**), but you can change the database name to use a file instead. I.e. **test.db**.
  
<br />
  
## File Modules
The **freedom/io** directory contains modules related to file handling.  

### File
Module **freedom35/io/file.py** contains methods to demonstrate basic text file read/write operations.  
  
For usage, refer to example code in **test_file.py**.  
To run **test_file.py**, use command line:  
```sh
$ python3 test_file.py
```
  
  
### CSV (Comma Separated Values)
Module **freedom35/io/csv.py** contains methods to demonstrate basic CSV file read/write operations.  
  
For usage, refer to example code in **test_csv.py**. 
To run **test_csv.py**, use command line:  
```sh
$ python3 test_csv.py
```
