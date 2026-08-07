from carga_datos import cargar_datos


def ejecutar():
    df = cargar_datos()
    if df.empty:
        print("No se pudieron cargar los datos.")
    else:
        print("Primeros cinco registros del DataFrame:")
        print(df.head())

if __name__ == "__main__":
    ejecutar()