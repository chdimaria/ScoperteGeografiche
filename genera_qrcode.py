from pathlib import Path
import re

try:
    import qrcode
except ImportError:
    print("Libreria mancante. Installa con:")
    print("pip install qrcode[pil]")
    raise SystemExit


def pulisci_testo(testo):
    testo = testo.lower().strip()
    testo = testo.replace(" ", "")
    testo = testo.replace("à", "a").replace("è", "e").replace("é", "e")
    testo = testo.replace("ì", "i").replace("ò", "o").replace("ù", "u")
    testo = re.sub(r"[^a-z0-9]", "", testo)
    return testo


print("GENERATORE QR CODE - PROGETTO SITO STORIA")
print("-----------------------------------------")

nome = input("Inserisci il nome: ")
cognome = input("Inserisci il cognome: ")
username_github = input("Inserisci lo username GitHub: ")

nome_pulito = pulisci_testo(nome)
cognome_pulito = pulisci_testo(cognome)
username_github = username_github.strip()

if nome_pulito == "" or cognome_pulito == "":
    print("Errore: nome o cognome non validi.")
    raise SystemExit

if username_github == "":
    print("Errore: username GitHub non valido.")
    raise SystemExit

nome_repository = f"sitostoria{nome_pulito}{cognome_pulito}"
url_sito = f"https://{username_github}.github.io/{nome_repository}/"

cartella_output = Path("qrcode_generato")
cartella_output.mkdir(exist_ok=True)

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)

qr.add_data(url_sito)
qr.make(fit=True)

immagine = qr.make_image(fill_color="black", back_color="white")

nome_file_qr = f"qr_{nome_pulito}_{cognome_pulito}.png"
percorso_qr = cartella_output / nome_file_qr
immagine.save(percorso_qr)

riepilogo = f"""DATI PROGETTO SITO STORIA

Nome studente:
{nome} {cognome}

Repository GitHub da usare:
{nome_repository}

URL GitHub Pages:
{url_sito}

File QR code generato:
{nome_file_qr}

Istruzioni:
1. Crea una repository GitHub chiamata:
   {nome_repository}

2. Carica nella repository tutti i file del sito.

3. Attiva GitHub Pages.

4. Verifica che il sito sia raggiungibile a questo indirizzo:
   {url_sito}

5. Usa il QR code generato nel documento di progetto o nella presentazione.
"""

file_riepilogo = cartella_output / "riepilogo_progetto.txt"
file_riepilogo.write_text(riepilogo, encoding="utf-8")

print()
print("QR code generato correttamente.")
print()
print("Repository da creare:")
print(nome_repository)
print()
print("URL del sito:")
print(url_sito)
print()
print("File creati nella cartella 'qrcode_generato':")
print(f"- {nome_file_qr}")
print("- riepilogo_progetto.txt")
