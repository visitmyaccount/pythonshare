from boxsdk import OAuth2, Client

def printItems(entry):
    if entry.type == "folder":
        print("reading folder items:" + entry.name + "========================" + entry.id)
        subfolder = client.folder(folder_id=entry.id).get()
        print('Sub Folder Name "{0}" has {1} items in it'.format(subfolder.name, subfolder.item_collection['entries']))
        for subentry in subfolder.item_collection['entries']:
            printItems(subentry)

auth = OAuth2(
    client_id='4z0cvhr0frhfgaj0rq1ebqkto1v9es0z',
    client_secret='6F78nICiLFTlgTYlID7CGoyDRdYnLDIp',
    access_token='Vaend76ML4Y5YB9iXonWNlxw9Tyj9822',
)
client = Client(auth)
user = client.user().get()
print('The current user ID is {0}'.format(user.id))


pending_collaborations = client.get_pending_collaborations()
print ("pending collabs:" + pending_collaborations)
for pending_collaboration in pending_collaborations:
    print('Collaboration {0} is pending'.format(pending_collaboration.id))

