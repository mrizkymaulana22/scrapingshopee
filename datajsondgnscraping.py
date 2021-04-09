# # gunakan modul json
# import json
#
# # buka file JSON
# file_json = open("note.json")
#
# # parsing data JSON
# data = json.loads(file_json.read())
#
# # cetak isi data JSON
# print(f"Nama: {data['name']}")
# print(f"Website: {data['web']}")
# print("Sosial Media:")
# print(f"- Facebook: {data['social_media']['facebook']}")
# print(f"- Twitter: {data['social_media']['twitter']}")
# print(f"- Instagram: {data['social_media']['instagram']}")

import json
from urllib import request

# tentukan url endpoint
url = "https://api.github.com/users/mrizkymaulana22"

# lakukan http request ke server
response = request.urlopen(url)

# parsing data json
data = json.loads(response.read())

# cetak hasil parsing data
print("== Program Baca profile Github ==")
print(f"Nama: {data['name']}")
print(f"Lokasi: {data['location']}")
print(f"Institusi: {data['company']}")
print(f"Folower: {data['followers']}")
print(f"mendaftar github pada: {data['created_at']}")

