# pyftp
This is a simple python ftp client for the command line interface(cli).
It helps great when you are facing cpanel with no ssh otherwise you probabaly don't need it

Note: This script has not been tested on windows, tested on Ubuntu 16.04

## How to
```
import ftplib, os
import config # Config variables py file
```
### make connection
```
make_connection()
```
Makes a connection with parameters: host, username, password

### make connection_uri
```
make_connection_uri()
```
Makes a connection from uri string: [host]:[username]@[password]

### get files(connection, dir)
```
get_files(connection, dir)
```
Lists files in a directory

### upload
```
upload(connection, file)
```
Uploads a file to a directory

### run()
```
run()
```
Runs the ftp client

## Issues
Not tested in windows, mac

## Contribution

Feel free to clone, open a pull request or drop an email to [mxmandela@gmail.com](mailto:mxmandela@gmail.com)
