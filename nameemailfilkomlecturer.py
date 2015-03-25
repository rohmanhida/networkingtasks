__author__ = 'rhmnhd'

import urllib, urllister, re
# this will open filkom lecturers page
usock = urllib.urlopen("http://ptiik.ub.ac.id/page/read/dosen/461acea")
parser = urllister.URLLister()
parser.feed(usock.read())
usock.close()
parser.close()

print "Kelompok : \nAbdurrohman Hidayat\nGhenniy Rachmansyah\nRo'i Fahreza Nur Firmansyah\nM. Fahrur Rozi\n"

# repeat until all links fetched
for url in parser.urls:
    # searching for lecture in this case 'staff' pattern in raw html
    matchObj = re.match( 'http://ptiik.ub.ac.id/info/staff/.*?', url, re.M|re.I)
    #if match
    if matchObj:
        # load the url
        sock = urllib.urlopen(url)
        htmlSource = sock.read()

        # search for lecturer's name and e-mail
        nama = re.search('<h2 class="margin-top-sm">.*?\s\s\s\s', htmlSource, re.DOTALL)
        emaildosen = re.findall('<li><span class="fa fa-envelope-o"></span>.*?</li>', htmlSource, re.M|re.I)

        # pop
        namadosen = nama.group(0)

        # trying to print it out
        for email in emaildosen:
            # pre-processing from raw pattern
            namadosen = namadosen.replace('<h2 class="margin-top-sm">', '')
            email = email.replace('<li><span class="fa fa-envelope-o"></span>','')
            email = email.replace('</li>','')
            email = email.replace(' [at] ','@')
            email = email.replace(' [dot] ','.')
            # print it
            print "Nama Dosen : ", namadosen
            print "Email Dosen : ", email, "\n"
