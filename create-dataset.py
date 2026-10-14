# Build worldcups.csv, the dataset for the quiz 02 make-up.
# One row per men's FIFA World Cup, 1930 to 2022. Teams, matches and
# goals are official FIFA totals. Attendance is the total for each
# tournament, rounded to thousands. The data is intended for teaching.
#
# Run: python create-dataset.py
# The file worldcups.csv appears in the current directory.

import csv

# year, host, host_continent, winner, teams, matches, goals, attendance_k
CUPS = [
    (1930, "Uruguay", "South America", "Uruguay", 13, 18, 70, 591),
    (1934, "Italy", "Europe", "Italy", 16, 17, 70, 363),
    (1938, "France", "Europe", "Italy", 15, 18, 84, 376),
    (1950, "Brazil", "South America", "Uruguay", 13, 22, 88, 1045),
    (1954, "Switzerland", "Europe", "West Germany", 16, 26, 140, 769),
    (1958, "Sweden", "Europe", "Brazil", 16, 35, 126, 820),
    (1962, "Chile", "South America", "Brazil", 16, 32, 89, 893),
    (1966, "England", "Europe", "England", 16, 32, 89, 1563),
    (1970, "Mexico", "North America", "Brazil", 16, 32, 95, 1604),
    (1974, "West Germany", "Europe", "West Germany", 16, 38, 97, 1866),
    (1978, "Argentina", "South America", "Argentina", 16, 38, 102, 1546),
    (1982, "Spain", "Europe", "Italy", 24, 52, 146, 2110),
    (1986, "Mexico", "North America", "Argentina", 24, 52, 132, 2394),
    (1990, "Italy", "Europe", "West Germany", 24, 52, 115, 2516),
    (1994, "United States", "North America", "Brazil", 24, 52, 141, 3588),
    (1998, "France", "Europe", "France", 32, 64, 171, 2785),
    (2002, "South Korea and Japan", "Asia", "Brazil", 32, 64, 161, 2705),
    (2006, "Germany", "Europe", "Italy", 32, 64, 147, 3359),
    (2010, "South Africa", "Africa", "Spain", 32, 64, 145, 3179),
    (2014, "Brazil", "South America", "Germany", 32, 64, 171, 3430),
    (2018, "Russia", "Europe", "France", 32, 64, 169, 3032),
    (2022, "Qatar", "Asia", "Argentina", 32, 64, 172, 3404),
]

HEADER = ["year", "host", "host_continent", "winner", "teams", "matches",
          "goals", "attendance_k"]

with open("worldcups.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(HEADER)
    writer.writerows(CUPS)

print(f"Wrote worldcups.csv with {len(CUPS)} tournaments.")
