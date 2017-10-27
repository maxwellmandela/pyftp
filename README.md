# pyftp
This is a simple python ftp client

## How to
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

# Issues
Not tested in windows, mac