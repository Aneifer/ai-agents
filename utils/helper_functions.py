import os
import json
import re

def load_journal_entries(filepath):
    """
    Lädt Journaleinträge aus einer Textdatei.
    
    Args:
        filepath (str): Der Pfad zur Textdatei mit den Journaleinträgen.
        
    Returns:
        list: Eine Liste von Einträgen, wobei jede Zeile als ein Eintrag betrachtet wird.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Die Datei {filepath} wurde nicht gefunden.")
    
    with open(filepath, 'r', encoding='utf-8') as file:
        entries = file.readlines()
    return [entry.strip() for entry in entries if entry.strip()]  # Entferne Leerzeilen


def save_to_json(data, filepath):
    """
    Speichert Daten in einer JSON-Datei.
    
    Args:
        data (dict or list): Die zu speichernden Daten.
        filepath (str): Der Pfad, wo die Datei gespeichert werden soll.
    """
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def load_json(filepath):
    """
    Lädt Daten aus einer JSON-Datei.
    
    Args:
        filepath (str): Der Pfad zur JSON-Datei.
        
    Returns:
        dict or list: Die geladenen Daten.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Die Datei {filepath} wurde nicht gefunden.")
    
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)


def clean_text(text):
    """
    Bereinigt einen Text, indem überflüssige Leerzeichen und Zeilenumbrüche entfernt werden.
    
    Args:
        text (str): Der zu bereinigende Text.
        
    Returns:
        str: Der bereinigte Text.
    """
    return re.sub(r'\s+', ' ', text).strip()


def file_exists(filepath):
    """
    Prüft, ob eine Datei existiert.
    
    Args:
        filepath (str): Der Pfad zur Datei.
        
    Returns:
        bool: True, wenn die Datei existiert, sonst False.
    """
    return os.path.exists(filepath)
