data_files = ["vanguard_etfs.txt", "state_street_etfs.txt",
    "ishares_etfs.txt", "dimensional_etfs.txt", "invesco_etfs.txt",
    "schwab_etfs.txt"]
symbols = []
for data_file in data_files:
    lines = open(data_file, "r").readlines()
    for line in lines:
        if line.strip().startswith("Symbol"):
            continue
        end = line.find("$")
        if end == -1:
            continue
        line = line[:end]
        symbol = line.split()[0]
        print(symbol, line)
        if symbol not in symbols:
            symbols.append(symbol)
symbols = sorted(symbols)
print(len(symbols), symbols)
fp = open("etf_symbols.txt", "w")
print("\n".join(symbols), file=fp)
