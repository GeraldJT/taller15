import pandas as pd
import requests

propietarios = pd.read_csv('data/propietarios.csv', delimiter='|')

for index, row in propietarios.iterrows():
    cedula = row['cedula']
    nombre = row['nombre']
    apellido = row['apellido']
    
    data = {
        'cedula': cedula,
        'nombre': nombre,
        'apellido': apellido
    }
    
    r = requests.post('http://127.0.0.1:8000/api/propietarios/', data=data, auth=('gerald', 'geraldjt2002'))
    
    if r.status_code == 201:
        print(f"Propietario '{nombre} {apellido}' creado exitosamente.")
    else:
        print(f"Error al crear el propietario '{nombre} {apellido}'. Error {r.status_code}: {r.text}")


edificios = pd.read_csv('data/edificios.csv', delimiter='|')
print(edificios)

for index, row in edificios.iterrows():
    nombre = row['nombre']
    direccion = row['dirección']
    ciudad = row['ciudad']
    tipo = row['tipo']

    data = {
        'nombre': nombre,
        'direccion': direccion,
        'ciudad': ciudad,
        'tipo': tipo
    }
    
    r = requests.post('http://127.0.0.1:8000/api/edificios/', data=data, auth=('gerald', 'geraldjt2002'))
    
    if r.status_code == 201:
        print(f"Edificio '{nombre}' creado exitosamente.")
    else:
        print(f"Error al crear el propietario '{nombre} {apellido}'. Error {r.status_code}: {r.text}")


departamentos = pd.read_csv('data/departamentos.csv', delimiter='|')
print(departamentos)

def obtener_id_propietario(propietario):
    url = f'http://127.0.0.1:8000/api/propietarios/?cedula={propietario}'
    r = requests.get(url, auth=('gerald', 'geraldjt2002'))
    print(r)
    if r.status_code == 200:
        propietarios = r.json()
        print(propietarios)
        for p in propietarios:
            if p['cedula'] == propietario:
                return p['id']
    return None

def obtener_id_edificio(edificio):
    url = f'http://127.0.0.1:8000/api/edificios/?nombre={edificio}'
    r = requests.get(url, auth=('gerald', 'geraldjt2002'))
    if r.status_code == 200:
        edificios = r.json()
        for e in edificios:
            if e['nombre'] == edificio:
                return e['id']
    return None

for index, row in departamentos.iterrows():
    propietario = row['Propietario']
    costo = row['Costo']
    numero_cuartos = row['Cuartos']
    edificio = row['Edificio']

    propietario_id = obtener_id_propietario(propietario)
    print(propietario_id)
    edificio_id = obtener_id_edificio(edificio)
    print(edificio_id)

    if propietario_id is None:
        print(f"El propietario con cédula '{propietario}' no existe en la base de datos.")
        continue

    if edificio_id is None:
        print(f"El edificio '{edificio}' no existe en la base de datos.")
        continue

    data = {
        'propietario': propietario_id,
        'costo': costo,
        'num_cuartos': numero_cuartos,
        'edificio': edificio_id
    }

    r = requests.post('http://127.0.0.1:8000/api/departamentos/', data=data, auth=('gerald', 'geraldjt2002'))

    if r.status_code == 201:
        print(f"Departamento del propietario con cédula '{propietario}' creado exitosamente.")
    else:
        print(f"Error al crear el departamento del propietario con cédula '{cedula_propietario}'. Error {r.status_code}: {r.text}")
