import pyqrcode
import requests

client_id = '011ae17fa0204c3d28cd46f3dba0ff654a0a847ba572d37cb6362089502cbed3'
secret_id = ''
per_page = 1000
url = ('https://my.mlh.io/api/v2/users?client_id={0}&secret={1}&per_page={2}'.format(client_id, secret_id, per_page))
u = requests.get(url)
resp = u.json()

current_participants = resp['pagination']['results_on_page']
print(current_participants)
print(resp['data'][0]['school']['name'])

def create_unique_qr(f_name, l_name, email, major, shirt_size, school_name, level_of_study, secret, error, scale):
    auto_fill_url = ('https://docs.google.com/forms/d/e/1FAIpQLScDAjNoosnfIE_gJ4DeNumMW1edxIeVLcW-zEJufyq2-roSSA/'
                     'viewform?usp=pp_url&entry.1937819802={0}&entry.347848875={1}&entry.35909750={2}&entry.68492964={3}'
                     '&entry.1577975628={4}&entry.1728344773={5}&entry.86949640{6}'
                     '&entry.1024666618={7}'.format(
        f_name, l_name, email, major, shirt_size, school_name, level_of_study, secret))
    name = l_name + "-" + f_name
    qr = pyqrcode.create(auto_fill_url.encode('utf-8'))
    qr.png(name + ".png")

for x in range(2):
    print('{0}. f_name: '.format(x + 1) + resp['data'][x]['first_name'])
    f_name = str(resp['data'][x]['first_name'])
    l_name = str(resp['data'][x]['last_name'])
    email = str(resp['data'][x]['email'])
    major = str(resp['data'][x]['major'])
    shirt_size = str(resp['data'][x]['shirt_size'])
    level_of_study = str(resp['data'][x]['level_of_study'])
    school_name = str(resp['data'][x]['school']['name'])
    create_unique_qr(f_name, l_name, email, major, shirt_size, school_name, level_of_study, secret="RamHacks2017!",
                     error="L", scale="10")


# create_unique_qr("test", "ma", "email@email.com", "minor", "Large", "school", "undergrad", "from Python", "L", "15")

# "id": 61325,
#             "email": "@vcu.edu",
#             "first_name": "",
#             "last_name": "",
#             "major": "Computer Science",
#             "shirt_size": "Unisex - L",
#             "dietary_restrictions": "None",
#             "special_needs": "n/a",
#             "date_of_birth": "1996-02-23",
#             "gender": "Male",
#             "phone_number": "+",
#             "level_of_study": "University (Undergraduate)",
#             "school": {
#                 "id": 2282,
#                 "name": "Virginia Commonwealth University"

