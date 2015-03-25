__author__ = 'rhmnhd'


import urllib, requests, re

halamanutama = urllib.urlopen('https://web.snmptn.ac.id/ptn')
halaman = halamanutama.read()

# mendapatkan nama univ
namaunivdirt = re.findall('href="/ptn/..">.*?</a></strong>', halaman, re.M|re.I)

# mendapatkan halaman univ
halaman = re.findall('(?<=href=")\w+://\w+.\w+.\w+.\w+.\w+', halaman, re.M|re.I)

# nama kelompok
print "Kelompok : \nAbdurrohman Hidayat imoet\nGhenniy Rachmansyah komes\nRo'i Fahreza Ganteng\nMohammad Fahrur Rozi Cakep\n"

for i in range(0,halaman.__len__()):
    # pre-preocessing url univ
    hasil = requests.get(halaman[i+1])

    # pre-preocessing nama univ
    namauniv = namaunivdirt[i]
    namauniv = ''.join([i for i in namauniv if not i.isdigit()])
    namauniv = namauniv.replace('href="/ptn/">','')
    namauniv = namauniv.replace('</a></strong>','')

    print namauniv
    print 'Server (OS) : ',hasil.headers['Server']
    print 'PHP : ',hasil.headers['x-powered-by'], '\n'