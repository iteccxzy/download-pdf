import requests

listado = []

with open('ejemplo.txt') as file:
    while (line := file.readline().rstrip()):
        listado.append(line)

# print(listado)

cookie = {
    '.ASPXAUT': '337183F9C6A95068BBD7988348F8B7F4BFA552832EA871ED94E476F82A165296CE9F996F75DC84D9B9217AC2474B947549B7FFC9547DF2F982BA193371AF92163D9E1D4B7DD13FE33BA6B4188967F6B41739EA46DEFA65F5B978B0BA8589A2EF5B84FCF6CDF8006362533B8844653573D1BC2CC5BACD3076D713FDCF93DE19D7D431A6887E1287BB405A1D0202003A0A97FF95DC62483DD5206CE2D4CC8108E4558EA1DB',
}

count = 0
for l in listado:
    
    with requests.get(l, stream=True, cookies=cookie) as r:
        _, fn = r.headers['Content-Disposition'].split('=')     

        file_name = f'acta-{fn}.pdf'
        with open(f'salida\{file_name}', 'wb') as fd:
            for chunk in r.iter_content(chunk_size=1024):
                fd.write(chunk)
        count += 1
