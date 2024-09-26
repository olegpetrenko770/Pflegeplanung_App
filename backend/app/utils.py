import os
import json
import logging
from datetime import datetime

# Logger konfigurieren
def setup_logger(name, log_file, level=logging.INFO):
    """Konfiguriert den Logger."""
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
    """Liest eine JSON-Datei und gibt die Daten zurück."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logging.error(f"Error reading JSON file {file_path}: {e}")
        return None

# JSON-Datei schreiben
def write_json(data, file_path):
    """Schreibt Daten in eine JSON-Datei."""
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        logging.error(f"Error writing JSON file {file_path}: {e}")

# Überprüfen, ob ein Pfad existiert
def ensure_dir(directory):
    """Stellt sicher, dass ein Verzeichnis existiert."""
    os.makedirs(directory, exist_ok=True)

# Aktuelles Datum und Uhrzeit abrufen
def get_current_datetime():
    """Gibt das aktuelle Datum und die aktuelle Uhrzeit zurück."""
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Beispiel für eine Hilfsfunktion
def example_helper_function(param1, param2):
    """Beispiel einer Hilfsfunktion."""
    result = param1 + param2
    return result
