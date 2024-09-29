import os
import json
import logging
from datetime import datetime

# Logger konfigurieren
def setup_logger(name, log_file, level=logging.INFO):
    """Konfiguriert den Logger.

    Args:
        name (str): Name des Loggers.
        log_file (str): Pfad zur Logdatei.
        level (int): Logging-Level.

    Returns:
        logging.Logger: Konfigurierter Logger.
    """
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        logger.setLevel(level)
        logger.addHandler(handler)

    return logger

# JSON-Datei lesen
def read_json(file_path):
    """Liest eine JSON-Datei und gibt die Daten zurück.

    Args:
        file_path (str): Pfad zur JSON-Datei.

    Returns:
        dict: Daten aus der JSON-Datei oder None bei Fehler.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        logging.error(f"JSON file not found: {file_path}")
    except json.JSONDecodeError:
        logging.error(f"Error decoding JSON file: {file_path}")
    except Exception as e:
        logging.error(f"Unexpected error reading JSON file {file_path}: {e}")
    return None

# JSON-Datei schreiben
def write_json(data, file_path):
    """Schreibt Daten in eine JSON-Datei.

    Args:
        data (dict): Daten, die in die JSON-Datei geschrieben werden sollen.
        file_path (str): Pfad zur JSON-Datei.
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        logging.error(f"Error writing JSON file {file_path}: {e}")
    except Exception as e:
        logging.error(f"Unexpected error writing JSON file {file_path}: {e}")

# Überprüfen, ob ein Pfad existiert
def ensure_dir(directory):
    """Stellt sicher, dass ein Verzeichnis existiert.

    Args:
        directory (str): Pfad zum Verzeichnis.
    """
    try:
        os.makedirs(directory, exist_ok=True)
    except Exception as e:
        logging.error(f"Error ensuring directory {directory}: {e}")

# Aktuelles Datum und Uhrzeit abrufen
def get_current_datetime():
    """Gibt das aktuelle Datum und die aktuelle Uhrzeit zurück.

    Returns:
        str: Aktuelles Datum und Uhrzeit im Format 'YYYY-MM-DD HH:MM:SS'.
    """
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Beispiel für eine Hilfsfunktion
def example_helper_function(param1, param2):
    """Beispiel einer Hilfsfunktion.

    Args:
        param1 (int, float): Erster Parameter.
        param2 (int, float): Zweiter Parameter.

    Returns:
        int, float: Ergebnis der Addition der beiden Parameter.
    """
    return param1 + param2
