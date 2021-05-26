
# Definición de parámetros de configuración

PeriodoDePoleo = 30000 # Milisegundos entre cada poleo de mediciones
AlmacenamientoLocal = False # Define si los datos se alamacenarán localmente o no
Compresion = False # Define si los datos que se almacenarán localmente serán comprimidos
EnvioAlaNube = True # Define si los datos serán enviados a Internet a traves del protocolo MQTT
TxRxPins = [33, 19] # Los pines donde está conectado el sensor [33, 19] para cancay a1,
LogEnTerminal = False # Habilita el envío de log a la consola repl
MQTT_PORT = 1883 # Parametros para el MQTT
MQTT_TOPIC = "cancay"
MQTT_HOST = "ec2-3-83-89-138.compute-1.amazonaws.com"
OTA_Files = ["Configuracion.py"] # Aquí se definen los archivos que formarán parte de la actualizacion OTA (Over The Air)

# Esta es solo una linea para probar el OTA
