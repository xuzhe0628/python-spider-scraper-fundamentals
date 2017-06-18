import onedrivesdk

redirect_uri = 'https://localhost:8080'
client_id = '' # fill in your client id
client_secret = '' # fill in your client id
api_base_url = 'https://api.onedrive.com/v1.0/'
scopes = ['wl.signin', 'wl.offline_access', 'onedrive.readwrite']

def auth_onedrive(client_id, scopes, api_base_url, redirect_uri):
    http_provider = onedrivesdk.HttpProvider()
    auth_provider = onedrivesdk.AuthProvider(
        http_provider=http_provider,
        client_id=client_id,
        scopes=scopes)

    client = onedrivesdk.OneDriveClient(api_base_url, auth_provider,
        http_provider)
    auth_url = client.auth_provider.get_auth_url(redirect_uri)
    # Ask for the code
    print('Paste this URL into your browser, approve the app\'s access.')
    print(
        'Copy everything in the address bar after "code=", and'
        ' paste it below.')
    print(auth_url)
    with open('authurl.txt', 'w') as authurl:
        authurl.write(auth_url)
    code = input('Paste code here: ')

    client.auth_provider.authenticate(code, redirect_uri, client_secret)
    
    return client
  
def upload_onedrive(client, upload_path, upload_file):
    returned_item = client.item(drive='me', id='root')
    returned_item = returned_item.children[upload_file]
    upload_item = returned_item.upload(os.path.join(upload_path, upload_file))
    
client = auth_onedrive(client_id, scopes, api_base_url, redirect_uri)
#get the top three elements of root, leaving the next page for more elements
collection = client.item(drive='me', id='root').children.request(top=3).get()

for item in collection:
    print(item.__dict__)

# upload_onedrive(client, base_folder, archive_folder + '.zip')