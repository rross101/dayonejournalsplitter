
file = open("2016-10-16 - Entries.md", "r", encoding="utf-8")

writefile = open("temp", "w")

for line in file:
    if "Date:" in line:
        writefile.close()
        writefile = open(line[7:-1] + ".md", "w", encoding="utf-8")
        writefile.writelines(line)
    else:
        writefile.writelines(line)


file.close()
