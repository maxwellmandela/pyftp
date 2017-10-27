# A simple python ftp module
# author: maxwellmandela

import ftplib
import os
import config


def make_connection_uri():
    uri = raw_input('Enter connection the URI(server:user@password): ')
    host = uri.split(':')[0]
    username = uri.split(':')[1].split('@')[0]
    password = uri.split(':')[1].split('@')[1]

    print "Connecting.."

    try:
        ftp = ftplib.FTP(host, username, password)
        print "Connection established"
        return ftp
    except Exception, err:
        print "Connection error %s:" % (str(err))
        return False


def make_connection():
    host = raw_input('Hostname: ')
    user = raw_input('Username: ')
    password = raw_input('Password: ')

    try:
        ftp = ftplib.FTP(host or config.host, user or config.user, password or config.password)
        return ftp
    except Exception, err:
        print "Connection error %s:" % (str(err))
        return False


def connection_method():
    connection_option = input('Pick a way to connect(1. URI, 2. Host, Password, User): ')
    if connection_option == 1:
        return make_connection_uri()
    return make_connection()


def get_files(con, directory):
    contents = con.nlst(directory)
    for item in contents:
        print "Found file %s:" % item


def upload(con, file_path):
    file_path = os.path.join(file_path)

    if os.path.isfile(file_path):
        print "File exists, attempting upload.."

        ext = os.path.splitext(file_path)[1]
        if ext in (".txt", ".htm", ".html"):
            new_path = con.storlines("STOR " + file_path, open(file_path))
        else:
            new_path = con.storbinary("STOR " + file_path, open(file_path, "rb"), 1024)
        return new_path
    else:
        return "File not exists, aborting.."


def run():
    con = connection_method()

    if con:
        directory = raw_input('Enter upload directory/path: ')
        directory = directory or config.directory
        file_path = raw_input('Enter file path: ')

        print "Files in %s:" % directory

        get_files(con, directory)

        try:
            con.cwd(directory)
            upload(con, file_path)
            print "File uploaded to", con.pwd()
        except Exception, e:
            print "File not uploaded to server %s" % (str(e))
    else:
        print "Server connection not established, aborting.."


run()
