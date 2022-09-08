# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import boxsdk

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    auth = OAuth2(
        client_id='4z0cvhr0frhfgaj0rq1ebqkto1v9es0z',
        client_secret='6F78nICiLFTlgTYlID7CGoyDRdYnLDIp',
        access_token='nq2F5trKhpQmntFTXFtY4pJK5xNj8enF',
    )
    client = Client(auth)
    user = client.user().get()
    print('The current user ID is {0}'.format(user.id))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


