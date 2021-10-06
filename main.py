import requests

listado = []

with open('ejemplo.txt') as file:
    while (line := file.readline().rstrip()):
        listado.append(line)

# print(listado)

cookie = {'_ga': 'GA1.3.1490466221.1633470260', '_gid': 'GA1.3.1164441364.1633470260',
          'ASP.NET_SessionId': 'dmmbx41lnu013e4rhvv435p4', '.ASPXAUT': 'B317E772747CDE20E9B9A4C4D7CB9DED119469E4E4A5EFCB6BDD8440E4432957B112FB729DB8813D25E35FECE79DCD1873C7D8006C790298400D1F95A0183184F9DF744BC87A355581DC16A48DD4C2D87E81247CE56DE95B8D5968F66F84DBD5532A6AFE58DD3129867AB00C93E7E33DA35BEDD3D37A1495D27192EFA03BD89326478E0024C746400663C5A93E2CA88E8E2A1094E0888C1D01BBBA0BE0C655904A88FDFD', '.ASPROLES': 'XqUpuStrf1HAp1BUycf8ZOMusplVO31eiU1QRmOX-aOFieI3mj_MgQNNqHvNZo79ObHb3XIS9l7IMtxO3nOjscKJPjrNLeVSfGuT_Heem5BZzVXibkelhRSocfRF0_4kVNWFuzdOvQ4x6aMdlv0g05obOzABq0WqqiNSiudD4JQNqTblJvSGb7JHfNNhOT15jctXLzxBAvJlsByfS1hDwBVfEYXR9AHNTOXEQYw3Kvrx-xdmVLyNeUowFX-wb-5HtOqL0lt1SLGEOhZK4AaFzyDhH-I2b9rWIborP_4QLsajF2mW9PhJHhZAXQ2adtGSdBKTr5o0Bks-xQnva-uZYUTZbnh8iiT7pMplzUNXJcB6Jbk2OhysMnik4QxqTwuTmA53AqO7ykn21s_ohvGDxVP1ec-YIxhQZFGoL4qwkRS8ZVKDyDyzpzSiZVvryLyjsCyuhO5R2fkLxF8KJi98lnuXA_kyGszV2KbzVtU_nyylHfyrB0SDeLjMEFg-EDr6dk17e67mwfSsEksx66Aaqc66giA-rxfpYoha2I4zYPKuLDGcQsqCw8C4zbaAjcaCx_IXpg2'}

count = 0
for l in listado:
    with requests.get(l, stream=True, cookies=cookie) as r:
        # print(r.text)

        file_name = f'reporte-{count}.pdf'
        with open(file_name, 'wb') as fd:
            for chunk in r.iter_content(chunk_size=1024):
                fd.write(chunk)
        count += 1
