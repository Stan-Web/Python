class Sistema_transporte_ruta:
    def __init__(seft):
        seft.base_concimiento= {
            'A':['C','D'],
            'B':['A','E'],
            'C': ['A','B'],
            'D':['E','F'],
            'E':['C','F'],
            'F': ['D','B']
        }
    
    def encontrar_ruta(seft,inicio,destino):
        ruta_actual = [inicio]
        transitados = set()


        while ruta_actual[-1] != destino:
            estacion_actual = ruta_actual[-1]


            if estacion_actual in transitados:
                break

            conexiones = seft.base_concimiento.get(estacion_actual,[])

            if not conexiones:
               ruta_actual.pop()

            else:
                proxima_estacion = [conexion for conexion in conexiones if conexion not in ruta_actual][0]
                ruta_actual.append(proxima_estacion)
                transitados.add(estacion_actual)

        return ruta_actual if ruta_actual[-1] == destino else None
    

programa = Sistema_transporte_ruta()
ruta_optima = programa.encontrar_ruta('A','F')

if ruta_optima:
    print(f'Ruta optima: {ruta_optima}')
else:
    print('No hay ruta optima')

  

