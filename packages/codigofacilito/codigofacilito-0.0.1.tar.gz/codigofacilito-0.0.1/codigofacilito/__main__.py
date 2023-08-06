import logging

from codigofacilito import unreleased

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    logging.debug('>>> Estamos comenzando la ejecución del paquete.')
    
    workshops = unreleased()
    
    logging.debug('>>> Estamos finalizando la ejecución del paquete.')