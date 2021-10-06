import requests

listado = []

with open('ejemplo.txt') as file:
    while (line := file.readline().rstrip()):
        listado.append(line)

# print(listado)

cookie = {'_ga': '',
          '_gid': '',
          'ASP.NET_SessionId': '',
          '.ASPXAUT': '',
          '.ASPROLES': ''}

count = 0
for l in listado:
    with requests.get(l, stream=True, cookies=cookie) as r:
        # print(r.text)

        file_name = f'reporte-{count}.pdf'
        with open(file_name, 'wb') as fd:
            for chunk in r.iter_content(chunk_size=1024):
                fd.write(chunk)
        count += 1
