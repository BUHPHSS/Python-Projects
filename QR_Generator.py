import pyqrcode
addURL = 'https://github.com/agneya-1402'
url=pyqrcode.create(addURL)
url.svg("uca-url.svg",scale=1)
a=url.terminal(quiet_zone=1)
print(a)