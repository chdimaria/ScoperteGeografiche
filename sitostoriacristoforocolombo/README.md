# SitoStoria - Cristoforo Colombo e il 1492

Progetto completo pronto per GitHub Pages.

## Tema
Sito storico sul primo viaggio di Cristoforo Colombo e sulle conseguenze dell'incontro tra Europa e Americhe.

## Struttura

```text
sitostoriacristoforocolombo/
├── index.html
├── contesto.html
├── viaggio.html
├── incontri.html
├── eredita.html
├── fonti.html
├── css/
│   └── style.css
├── js/
│   └── script.js
├── img/
│   ├── hero-caravelle.svg
│   ├── compasso-mappa.svg
│   ├── rotta-atlantica.svg
│   └── isole-caraibi.svg
├── genera_qrcode.py
└── README.md
```

## Come pubblicare su GitHub Pages

1. Crea una repository chiamata `sitostoriacristoforocolombo`.
2. Carica tutti i file del progetto nella repository.
3. Vai su **Settings → Pages**.
4. Scegli:
   - Source: `Deploy from a branch`
   - Branch: `main`
   - Folder: `/ root`
5. Salva.
6. Il sito sarà raggiungibile all'indirizzo:

```text
https://USERNAME.github.io/sitostoriacristoforocolombo/
```

## Funzionalità JavaScript presenti

- menu responsive per dispositivi mobili;
- cambio tema chiaro/scuro;
- barra di avanzamento lettura;
- mini quiz interattivo;
- timeline cliccabile;
- accordion nelle FAQ storiche.

## QR code

Dopo la pubblicazione, esegui:

```bash
pip install qrcode[pil]
python genera_qrcode.py
```

Lo script genera una cartella `qrcode_generato` con:
- immagine PNG del QR code;
- file di riepilogo del progetto.

## Fonti principali

- Encyclopaedia Britannica: primo viaggio di Colombo.
- Library of Congress: Colombo e i Taíno.
- Encyclopaedia Britannica: Columbian Exchange.
- Smithsonian Magazine: Alfred W. Crosby e lo scambio colombiano.
