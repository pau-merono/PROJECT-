# PROJECT TECNOLOGIA-
# Analisi dei fattori che influenzano la fertilità maschile

## Introduzione
Questo studio analizza la relazione tra vari fattori sociodemografici e ambientali, stato di salute e abitudini di vita con la qualità dello sperma in un campione di 100 volontari. I campioni sono stati analizzati seguendo i criteri dell'OMS 2010 per determinare la concentrazione di sperma.

##Set di dati
### Descrizione generale
- **Dimensione del campione**: 100 volontari
- **Variabili**: 9 caratteristiche + 1 variabile obiettivo
- **Tipo**: dati multivarianti
- **Area**: Sanità e Medicina
- **Compiti associati**: Classificazione e Regressione
- **Valori mancanti**: No

### Variabili dello studio
1. **Stazione** (-1, -0,33, 0,33, 1)
 - Inverno, Primavera, Estate, Autunno

2. **Età** (normalizzata tra 0 e 1)
 - Gamma: 18-36 anni

3. **Malattie infantili** (0, 1)
 - Include: varicella, morbillo, parotite, poliomielite
 - 1: sì, 0: no

4. **Incidenti o traumi gravi** (0, 1)
 - 1: sì, 0: no

5. **Interventi chirurgici** (0, 1)
 - 1: sì, 0: no

6. **Febbre alta nell'ultimo anno** (-1, 0, 1)
 - -1: Meno di 3 mesi fa
 - 0: più di 3 mesi fa
 - 1: No

7. **Consumo di alcol** (normalizzato tra 0 e 1)
 - Frequenza da "più volte al giorno" a "quasi mai o mai"

8. **Abitudine al fumo** (-1, 0, 1)
 - -1: Mai
 - 0: occasionale
 - 1: Diario

9. **Ore di seduta al giorno** (normalizzato tra 0 e 1)
 - Intervallo: 1-16 ore

### Variabile di destinazione
- **Diagnosi**:
 -N: normale
 - O: Alterato

## Obiettivi dell'analisi
1. Identificare i fattori più influenti sulla qualità dello sperma
2. Analizzare le correlazioni tra le variabili
3. Sviluppare modelli predittivi per classificare la qualità dello sperma
4. Fornire approfondimenti sui fattori di rischio modificabili

## Metodologia
L’analisi verrà effettuata seguendo questi passaggi:
1. Preelaborazione e pulizia dei dati
2. Analisi esplorativa dei dati (EDA)
3. Analisi statistica
4. Modellazione predittiva
5. Interpretazione dei risultati
