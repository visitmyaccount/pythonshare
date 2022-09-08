import pysftp
cnopts = pysftp.CnOpts()
cnopts.hostkeys=None

def print_hi(name):
    print(f'Hi, {name}')
    with pysftp.Connection(host="test.rebex.net", username="demo",password="password"
                           , cnopts= cnopts) as sftp:
        for file in sftp.listdir():
            print(file)
            if sftp.isfile(file):
                sftp.get(file, "C:\\Users\\SIVA\\PycharmProjects\\Boxfolder\\"+file);


if __name__ == '__main__':
    print_hi('PyCharm')