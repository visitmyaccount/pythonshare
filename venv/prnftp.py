import ftplib

ftp = ftplib.FTP("ftp.dlptest.com")
ftp.login("dlpuser","rNrKYTX9g7z3RgJRmxWuGHbeu")

def print_hi(name):
    print(f'Hi, {name}')
    for file in ftp.nlst():
        print("files:" + file)

if __name__ == '__main__':
    print_hi('PyCharm')