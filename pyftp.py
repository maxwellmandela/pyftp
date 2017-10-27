# A simple python ftp module
# author: maxwellmandela

import ftplib
import os
import config

host = raw_input('Hostname: ')
user = raw_input('Username: ')
password = raw_input('Password: ')


def make_connection():
    try:
        ftp = ftplib.FTP(host or config.host, user or config.user, password or config.password)
        return ftp
    except Exception, err:
        print "Connection error %s:" % (str(err))
        return False


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
    print "Making a connection to server.."
    if make_connection():
        con = make_connection()
        directory = raw_input('Enter upload directory/path: ')
        directory = directory or config.directory
        file_path = raw_input('Enter file path: ')

        print "Connection made!"
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
