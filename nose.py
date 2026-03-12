import time
import sys

def escribir_con_ritmo(texto, velocidad=0.04):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velocidad)
    print()

letra = [
    ("Y si te parece que yo estoy enamorado tuyo", 0.06, 1.5),
    ("Eso es un invento, intuyo, no des crédito a murmullos", 0.06, 1.5),
    ("Porque casi nunca llamo para decir que te amo", 0.08, 1.5),
    ("Y más de una vez lo hice a un número equivocado", 0.07, 1.5),
    ("Casi nunca nadie dice que yo estoy enamorado tuuuuuuyo", 0.0, 2)
]

print("\n🎵 Reproduciendo 'Enamorado Tuyo'...\n")
time.sleep(1)

for linea, velocidad, pausa in letra:
    escribir_con_ritmo(linea, velocidad)
    time.sleep(pausa)

print("\nFin")