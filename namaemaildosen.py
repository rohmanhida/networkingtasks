__author__ = 'rhmnhd'

import urllib, urllister, re

usock = urllib.urlopen("http://ptiik.ub.ac.id/page/read/dosen/461acea")
parser = urllister.URLLister()
parser.feed(usock.read())
usock.close()
parser.close()

print "Kelompok : \nAbdurrohman Hidayat\nGhenniy Rachmansyah\nRo'i Fahreza Nur Firmansyah\nM. Fahrur Rozi\n"

for url in parser.urls:
    matchObj = re.match( 'http://ptiik.ub.ac.id/info/staff/.*?', url, re.M|re.I)
    if matchObj:
        # meload halaman dosen
        sock = urllib.urlopen(url)
        htmlSource = sock.read()

        # mencari nama dan email dosen
        nama = re.search('<h2 class="margin-top-sm">.*?\s\s\s\s', htmlSource, re.DOTALL)
        emaildosen = re.findall('<li><span class="fa fa-envelope-o"></span>.*?</li>', htmlSource, re.M|re.I)

        namadosen = nama.group(0)

        for email in emaildosen:
            namadosen = namadosen.replace('<h2 class="margin-top-sm">', '')
            email = email.replace('<li><span class="fa fa-envelope-o"></span>','')
            email = email.replace('</li>','')
            email = email.replace(' [at] ','@')
            email = email.replace(' [dot] ','.')
            print "Nama Dosen : ", namadosen
            print "Email Dosen : ", email, "\n"