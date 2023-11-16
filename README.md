# Python Modules
Repository for general purpose Python modules.  
These modules are intended for example purposes, but can also be used as-is or as a basis for use within other projects.

Note: Modules written using [Python 3](https://www.python.org/downloads/).  
  
<br />
  
## Database Module
The **freedom35/database** directory contains modules related to database operations.  
  
Module **freedom35/database/sqlite.py** contains the class *FreedomTestDatabase* to demonstrate simple [SQLite v3](https://www.sqlite.org/version3.html) database operations. For usage of this class, refer to the example code in **test_database_sqlite.py**.  

To run **test_database_sqlite.py**, use command line:  
```sh
$ python3 test_database_sqlite.py
```
  
Note: The test example uses an in-memory SQLite database (**:memory:**), but you can change the database name to use a file instead. I.e. **test.db**.
  
<br />
  
## I/O Modules
The **freedom35/io** directory contains modules related to file handling.  

### File
Module **freedom35/io/file.py** contains methods to demonstrate basic text file read/write operations. For usage, refer to the example code in **test_io_file.py**.  

To run **test_io_file.py**, use command line:  
```sh
$ python3 test_io_file.py
```
  
  
### CSV (Comma Separated Values)
Module **freedom35/io/csv.py** contains methods to demonstrate basic CSV file read/write operations. For usage, refer to the example code in **test_io_csv.py**.  

To run **test_io_csv.py**, use command line:  
```sh
$ python3 test_io_csv.py
```


## SMTP Modules
The **freedom35/smtp** directory contains modules related to sending emails via SMTP.  
  
**Note: In the SMTP test modules, you will need to change the example email configuration to match your own SMTP server login etc.**  
  
  
### Plaintext
Module **freedom35/smtp/plaintext.py** contains a method to demonstrate sending plaintext emails. For usage, refer to the example code in **test_smtp_plaintext.py**.  

To run **test_smtp_plaintext.py**, use command line:  
```sh
$ python3 test_smtp_plaintext.py
```
  
  
### MIME (Multipurpose Internet Mail Extensions)
Module **freedom35/smtp/mime.py** contains the class *FreedomMimeEmail* to handle sending MIME emails. For usage, refer to the example code in **test_smtp_mime.py**.  

To run **test_smtp_mime.py**, use command line:  
```sh
$ python3 test_smtp_mime.py
```
  
<br />