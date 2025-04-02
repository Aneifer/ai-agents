def load_journal_entries(filepath):
    """Lädt Journaleinträge aus einer Textdatei."""
    with open(filepath, 'r', encoding='utf-8') as file:
        entries = file.readlines()  # Jede Zeile wird als eigener Eintrag betrachtet
    return [entry.strip() for entry in entries if entry.strip()]  # Entferne Leerzeilen

# Beispielnutzung
if __name__ == "__main__":
    filepath = 'data/journals.txt'  # Pfad zur Datei
    journal_entries = load_journal_entries(filepath)

    print(f"Geladene Einträge ({len(journal_entries)}):")
    for i, entry in enumerate(journal_entries, 1):
        print(f"{i}: {entry}")
