import requests
import pprint
#http://127.0.0.1:8000/api/v0/rooms/
#
# response=requests.get('http://127.0.0.1:8000/api/v0/rooms', auth=('admin','admin'))
#
# if response.status_code!=404:
#     print(response.status_code)
#     pprint.pprint(response.json())
# else:
#     print("404 ошибка")
#

token="e5b05383af4ac3f7a2d61c0a0c26ce80b0f3d83e"
headers = {'Authorization': 'Token ' + token}
response=requests.get('http://127.0.0.1:8000/api/v0/windows', headers=headers)

if response.status_code!=404:
    print(response.status_code)
    pprint.pprint(response.json())
else:
    print("404 ошибка")

