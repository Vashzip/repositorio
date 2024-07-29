c1 = int(input("Votos do primeiro candidato "))
c2 = int(input("Votos do segundo candidato "))
c3 = int(input("Votos do terceiro candidato "))
c4 = int(input("Votos do quarto candidato "))
brancos = int(input("Votos em branco "))
nulos = int(input("Votos nulos "))

total_validos = c1 + c2 + c3 + c4
total_votos = total_validos + brancos + nulos

percentual1 = float((c1 / total_validos) * 100)
percentual2 = float((c2 / total_validos) * 100)
percentual3 = float((c3 / total_validos) * 100)
percentual4 = float((c4 / total_validos) * 100)
percentual_brancos = float((brancos / total_validos) * 100)
percentual_nulos = float((nulos / total_validos) * 100)

print(f"\nPercentual primeiro candidato: {percentual1:.2f}%")
print(f"Percentual segundo candidato:{percentual2:.2f}%")
print("Percentual terceiro candidato:{:.2f}%".format(percentual3))
print("Percentual quarto candidato:{:.2f}%".format(percentual4))
print("Percentual de votos brancos %.2f" % percentual_brancos, "%")
print("Percentual de votos nulos %.2f" % percentual_nulos, "%")

print("\nTeve um total de {} eleitores".format(total_votos))
print("Sendo {} os votos válidos".format(total_validos))