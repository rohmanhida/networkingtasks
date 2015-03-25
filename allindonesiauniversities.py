__author__ = 'rhmnhd'


import urllib, requests, re

# open the main page, that contain all url of indonesia universities
halamanutama = urllib.urlopen('https://web.snmptn.ac.id/ptn')
halaman = halamanutama.read()

# parsing university names
namaunivdirt = re.findall('href="/ptn/..">.*?</a></strong>', halaman, re.M|re.I)

# parsing university url
halaman = re.findall('(?<=href=")\w+://\w+.\w+.\w+.\w+.\w+', halaman, re.M|re.I)

# nama kelompok
print "Kelompok : \nAbdurrohman Hidayat imoet\nGhenniy Rachmansyah komes\nRo'i Fahreza Ganteng\nMohammad Fahrur Rozi Cakep\n"

# repeat until all url processed
for i in range(0,halaman.__len__()):
    # get the header of html page
    hasil = requests.get(halaman[i+1])

    # pre-processing university names
    namauniv = namaunivdirt[i]
    namauniv = ''.join([i for i in namauniv if not i.isdigit()])
    namauniv = namauniv.replace('href="/ptn/">','')
    namauniv = namauniv.replace('</a></strong>','')

    # it seems a bit ugly because if x-powered-by isn't found it will error and stop
    # i'm new in python, hehe
    print namauniv
    print 'Server (OS) : ',hasil.headers['Server']
    print 'PHP : ',hasil.headers['x-powered-by'], '\n'
