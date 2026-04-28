def failure_function(pattern: str) ->  list[int]:

    n = len(pattern)
    f = [0] * (n + 1)
    t = 0
    f[1] = 0
    for s in range(1, n):
        while t > 0 and pattern[s] != pattern[t]:
            t = f[t]

        if pattern[s] == pattern[t]:
            t += 1
            f[s + 1] = t
        else:
            f[s + 1] = 0

    return f

def solution_3_4_3(pattern: str) -> None:
    f = failure_function(pattern)
    n = len(pattern)

    print("=" * 62)
    print(f"  Función de falla para el patrón: '{pattern}'")
    print("=" * 62)
 
    # Tabla idéntica a la del libro: fila s | fila f(s)
    header_s = "  s    |" + "".join(f" {s:>4} " for s in range(1, n + 1))
    header_b = "  b[s] |" + "".join(f"  {pattern[s-1]:>2} " for s in range(1, n + 1))
    header_f = "  f(s) |" + "".join(f" {f[s]:>4} " for s in range(1, n + 1))
    sep = "  " + "-" * (len(header_s) - 2)
 
    print(header_s)
    print(sep)
    print(header_b)
    print(sep)
    print(header_f)
    print("=" * 62)
 
    # Interpretación de cada valor
    print("  Interpretación:")
    for s in range(1, n + 1):
        prefix_s = pattern[:s]
        if f[s] > 0:
            longest = pattern[:f[s]]
            print(f"    f({s}) = {f[s]}  →  prefijo propio más largo de '{prefix_s}'"
                  f" que es sufijo: '{longest}'")
        else:
            print(f"    f({s}) = 0  →  '{prefix_s}' no tiene prefijo propio que sea sufijo")
    print()
 
 
def main():
    print()
    print("#" * 62)
    print("#   Assignment 1: Función de Falla — Figura 3.19, pág. 137  #")
    print("#   Dragon Book — Sección 3.4.5                              #")
    print("#" * 62)
    print()
 
    # Ejercicio 3.4.3 (página 137) 

    print("─── Ejercicio 3.4.3 a)  patrón 'abababaab' ───")
    solution_3_4_3("abababaab")
 
    print("─── Ejercicio 3.4.3 b)  patrón 'aaaaaa' ───")
    solution_3_4_3("aaaaaa")
 
    print("─── Ejercicio 3.4.3 c)  patrón 'abbaabb' ───")
    solution_3_4_3("abbaabb")
 
 
if __name__ == "__main__":
    main()

