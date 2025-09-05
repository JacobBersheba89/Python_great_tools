import itertools
from openpyxl import Workbook

# 🔹 Zadání vstupních dat
pairs = [
    ("Irena", "Alča"),
    ("Kristina", "JanaD"),
    ("Víťa", "Michal"),
    ("Filip", "Zdeněk"),
    ("Petra", "Lucka"),
    ("Miloš", "JanaG")
]

extra = "Jakub"   # extra osoba
weeks = 4         # počet týdnů k vygenerování

days = ["Pondělí", "Úterý", "Středa", "Čtvrtek", "Pátek"]

# 🔹 Funkce pro generování rozpisu
def generate_schedule(pairs, extra, weeks):
    schedule = []
    pair_cycle = itertools.cycle(pairs)
    extra_index = 0

    for week in range(1, weeks + 1):
        for i, day in enumerate(days):
            pair = next(pair_cycle)

            # každý sudý týden otočíme role (telefon ↔ osobně)
            if week % 2 == 0:
                phone, desk = pair[1], pair[0]
            else:
                phone, desk = pair[0], pair[1]

            # Jakub se vměšuje cca 2× týdně
            if day in ["Úterý", "Čtvrtek"] and extra_index % len(pairs) == 0:
                if week % 2 == 0:
                    desk = extra
                else:
                    phone = extra
                extra_index += 1

            schedule.append((f"Týden {week}", day, phone, desk))
    return schedule

# 🔹 Generování rozpisu
schedule = generate_schedule(pairs, extra, weeks)

# 🔹 Export do Excelu
wb = Workbook()
ws = wb.active
ws.title = "Rozpis služeb"

# Hlavička
ws.append(["Týden", "Den", "Telefon", "Osobně"])

# Data
for row in schedule:
    ws.append(row)

# Uložení souboru
wb.save("rozpis_infolinka.xlsx")
print("✅ Rozpis vygenerován do souboru rozpis_infolinka.xlsx")
