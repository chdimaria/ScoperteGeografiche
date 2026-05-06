# Istruzioni rapide per lo studente

## 1. Pubblicazione del sito

1. Accedi a GitHub.
2. Crea una nuova repository pubblica.
3. Nome repository consigliato: `sitostorianomecognome`.
4. Carica tutti i file del progetto.
5. Vai su Settings → Pages.
6. Seleziona:
   - Source: Deploy from a branch
   - Branch: main
   - Folder: / root
7. Salva e attendi la pubblicazione.

## 2. URL finale

Il sito sarà raggiungibile con un URL simile:

```text
https://usernamegithub.github.io/sitostorianomecognome/
```

## 3. QR code

Installa la libreria:

```bash
pip install qrcode[pil]
```

Esegui:

```bash
python genera_qrcode.py
```

Il programma creerà la cartella `qrcode_generato` con il QR code e il riepilogo.
