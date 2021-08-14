print('This program separates a URL into its different parts')
url = input('Paste the URL here: ')

scheme = []
subdomain = []
sdom = []
tdom = []
subdirec = []
frog = []

index = 0
ind = 0

urlchar = list(url)
qreez = list(url)

for i in range(0, urlchar.index('/') + 2):
    scheme.append(urlchar[i])
print('Scheme:', ''.join(scheme))

for i in scheme:
    urlchar.remove(i)

while urlchar.count('.') != 1:
    ind = ind + 1
    for i in range(0, urlchar.index('.')+1):
        subdomain.append(urlchar[0])
        urlchar.remove(urlchar[0])
    print('Subdomain' + str(ind) + ':', ''.join(subdomain))
    subdomain.clear()

for i in range(0, urlchar.index('.')):
    sdom.append(urlchar[0])
    urlchar.remove(urlchar[0])
print('Second-level domain:', ''.join(sdom))

for i in range(0, urlchar.index('/')):
    tdom.append(urlchar[0])
    urlchar.remove(urlchar[0])
print('Top-level domain:', ''.join(tdom))

if qreez[len(qreez) - 1] == '/':
    qreez.reverse()
    qreez.remove(qreez[0])
    qreez.reverse()

qreez.reverse()
while qreez.count('/') != 2:
    index = index + 1
    for i in range(0, qreez.index('/')+1):
        subdirec.append(qreez[0])
        qreez.remove(qreez[0])
    subdirec.reverse()
    print('Subdirectory' + str(index) + ':', ''.join(subdirec))
    subdirec.clear()