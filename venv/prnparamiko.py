import os.path

import paramiko
import stat

host,port = "test.rebex.net", 22
transport = paramiko.Transport((host, port))

username="demo"
password="password"

transport.connect(None, username, password)

sftp = paramiko.SFTPClient.from_transport(transport)

def changedir():
    newpath = "pub/example";
    sftp.chdir(newpath);
    print(sftp.getcwd())
    sftp.chdir("..")
    print(sftp.getcwd())
    if not sftp.listdir():
        print("No files available")
    for file_attr in sftp.listdir_attr():
        print(file_attr)


def print_hi(name):
    print(f'Hi, {name}')
    for fileattr in sftp.listdir_attr():
        print(fileattr);
        # S_ISDIR for dir, S_ISREG for file
        if stat.S_ISREG(fileattr.st_mode):
            print(fileattr.filename)
            filename = os.path.join("C:\\Users\\SIVA\\PycharmProjects\\Boxfolder\\", fileattr.filename);
            # result = sftp.get(fileattr.filename, open(filename, 'wb').write)
            result = sftp.get(fileattr.filename, os.path.join("C:\\Users\\SIVA\\PycharmProjects\\Boxfolder\\", fileattr.filename))
            print(result)
        elif stat.S_ISDIR(fileattr.st_mode):
            for dfileattr in sftp.listdir_attr(fileattr.filename):
                print(dfileattr)
                if stat.S_ISREG(dfileattr.st_mode):
                    print("file:"+dfileattr.filename)
                else:
                    print("it is dir:"+ dfileattr.filename)


if __name__ == '__main__':
    # print_hi('PyCharm')
    changedir()
