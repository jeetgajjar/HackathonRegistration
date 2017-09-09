import pyqrcode
import requests
import urllib.parse

client_id = '011ae17fa0204c3d28cd46f3dba0ff654a0a847ba572d37cb6362089502cbed3'
with open('secret') as f:
    secret_id = f.readline()

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
    print(auto_fill_url)
    query = urllib.parse.quote(auto_fill_url)
    qr = pyqrcode.create(query)
    qr.png(name + ".png")

for x in range(2):
    print('{0}. f_name: '.format(x + 1) + resp['data'][x]['first_name'])
    f_name = str(resp['data'][x]['first_name'])
    l_name = str(resp['data'][x]['last_name'])
    email = str(resp['data'][x]['email'])
    major = str(resp['data'][x]['major'])
    if "" in major:
       nm = major.replace(" ", "+")
    shirt_size = str(resp['data'][x]['shirt_size'])
    if " " in shirt_size:
        nss = shirt_size.replace(" ", "+")
    level_of_study = str(resp['data'][x]['level_of_study'])
    if " " in level_of_study:
        nlos = level_of_study.replace(" ", "+").replace("(", "+").replace(")", "+")
    school_name = str(resp['data'][x]['school']['name'])
    if " " in school_name:
        nsn = school_name.replace(" ", "+")
    create_unique_qr(f_name, l_name, email, nm, nss, nsn, nlos, secret="RamHacks2017",
                     error="L", scale="10")
