import psycopg2
from datetime import datetime

# Configuración de base de datos
DB_CONFIG = {
    'host': 'localhost',
    'database': 'fovipol',
    'user': 'postgres',
    'password': 'pebe'  # Cambia esto por tu contraseña
}

# Campos a mostrar
CAMPOS_MOSTRAR = ['linea_titular', 'numero_d_2', 'fecha2', 'hora2', 'duracion', 'tipo', 'ent_sal']

def conectar_db():
    """Establece conexión con la base de datos PostgreSQL"""
    try:
        return psycopg2.connect(**DB_CONFIG)
    except Exception as e:
        print(f"❌ Error al conectar a PostgreSQL: {e}")
        return None

def formatear_valor(valor):
    """Formatea valores para mostrar en tabla"""
    if isinstance(valor, datetime):
        return valor.strftime('%Y-%m-%d %H:%M:%S')
    elif valor is None:
        return 'N/A'
    return str(valor)

def mostrar_resultados(resultados, columnas, linea_titular, numero_d_2):
    """Muestra los resultados de la consuSlta de forma optimizada"""
    print("\n" + "="*120)
    print("REPORTE DE VINCULACIONES TELEFÓNICAS - - DIVIAC - DEPSOTEC")
    print("="*120)
    print(f"Línea Titular: {linea_titular}")
    print(f"Número D_2: {numero_d_2}")
    print(f"Total de llamadas: {len(resultados)}")
    print("="*120)
    
    if not resultados:
        print("\n⚠️  No se encontraron llamadas entre estos números.\n")
        return
    
    # Contar llamadas por dirección
    idx_titular = columnas.index('linea_titular')
    llamadas_a_destino = sum(1 for r in resultados if r[idx_titular] == linea_titular)
    llamadas_desde_destino = len(resultados) - llamadas_a_destino
    
    print(f"\n📞 Llamadas de {linea_titular} → {numero_d_2}: {llamadas_a_destino}")
    print(f"📞 Llamadas de {numero_d_2} → {linea_titular}: {llamadas_desde_destino}")
    print("\n" + "-"*120)
    
    # Encabezados
    print(f"{'#':<5}", end="")
    for campo in CAMPOS_MOSTRAR:
        ancho = 18 if campo != 'linea_titular' else 15
        print(f"{campo.upper():<{ancho}}", end="")
    print("\n" + "-"*120)
    
    # Datos
    indices = [columnas.index(campo) for campo in CAMPOS_MOSTRAR]
    
    for num, fila in enumerate(resultados, 1):
        print(f"{num:<5}", end="")
        for i, idx in enumerate(indices):
            ancho = 18 if CAMPOS_MOSTRAR[i] != 'linea_titular' else 15
            valor = formatear_valor(fila[idx])
            print(f"{valor:<{ancho}}", end="")
        print()
    
    print("-"*120 + "\n")

def consultar_vinculaciones(linea_titular, numero_d_2):
    """Consulta las llamadas entre linea_titular y numero_d_2"""
    conexion = conectar_db()
    if not conexion:
        return
    
    try:
        cursor = conexion.cursor()
        
        # Consulta optimizada
        campos = ', '.join(CAMPOS_MOSTRAR)
        query = f"""
            SELECT {campos}
            FROM entel
            WHERE (linea_titular = %s AND numero_d_2 = %s)
               OR (linea_titular = %s AND numero_d_2 = %s)
            ORDER BY fecha2, hora2
        """
        
        cursor.execute(query, (linea_titular, numero_d_2, numero_d_2, linea_titular))
        resultados = cursor.fetchall()
        
        mostrar_resultados(resultados, CAMPOS_MOSTRAR, linea_titular, numero_d_2)
        
    except Exception as e:
        print(f"❌ Error al ejecutar consulta: {e}")
    finally:
        if conexion:
            cursor.close()
            conexion.close()

def solicitar_dato(mensaje):
    """Solicita y valida un dato al usuario"""
    while True:
        dato = input(mensaje).strip()
        if dato:
            return dato
        print("⚠️  El campo no puede estar vacío. Intente nuevamente.")

def main():
    """Función principal del programa"""
    print("\n" + "="*120)
    print("SISTEMA DE CONSULTA DE VINCULACIONES TELEFÓNICAS - DIVIAC")
    print("="*120 + "\n")
    
    while True:
        print("\n[INGRESO DE DATOS]")
        print("-" * 50)
        
        linea_titular = solicitar_dato("Ingrese LINEA_TITULAR (origen): ")
        numero_d_2 = solicitar_dato("Ingrese NUMERO_D_2 (destino): ")
        
        print("\n🔍 Buscando vinculaciones...")
        consultar_vinculaciones(linea_titular, numero_d_2)
        
        print("="*120)
        continuar = input("\n¿Desea realizar otra consulta? (S/N): ").strip().upper()
        
        if continuar != 'S':
            print("\n✓ Programa finalizado. ¡Hasta pronto!\n")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Programa interrumpido por el usuario.\n")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}\n")