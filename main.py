import requests

count = 0
listado = []
cookie = {
    '.ASPXAUT': '',
}

with open('ejemplo.txt') as file:
    while (line := file.readline().rstrip()):
        listado.append(line)

for l in listado:
    with requests.get(l, stream=True, cookies=cookie) as r:
        _, fn = r.headers['Content-Disposition'].split('=')
        file_name = f'acta-{fn}.pdf'
        with open(f'salida\{file_name}', 'wb') as fd:
            for chunk in r.iter_content(chunk_size=1024):
                fd.write(chunk)
        count += 1
