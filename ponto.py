from datetime import timedelta

def horasTrabalhadas(pontoInicial, pontoFinal, cargahoraria):
    totalhrs = pontoFinal - pontoInicial
    cincominutos = timedelta(minutes=5)

    if totalhrs < cargahoraria - cincominutos:
        negativo = cargahoraria - totalhrs
        return print(f"\nSaldo de negativo {negativo} horas")
    
    elif totalhrs > cargahoraria + cincominutos:
        positivo = totalhrs - cargahoraria
        return print(f"\nSaldo positivo de {positivo} horas")

    else: 
        return print("\nCarga horária cumprida")
    
def main():
    iniciohoras = int(input("Digite a hora incial: "))
    iniciominutos = int(input("Digite o minuto incial: "))
    inicial = timedelta(hours=iniciohoras, minutes=iniciominutos)

    finalhoras = int(input("\nDigite a hora final: "))
    finalminutos = int(input("Digite o minuto final: "))
    final = timedelta(hours=finalhoras, minutes=finalminutos)   

    cchr = int(input("\nDigite a hora da carga horaria: "))
    ccmin = int(input("Digite o minuto da carga horaria: "))
    cargahr = timedelta(hours=cchr, minutes=ccmin)

    horasTrabalhadas(inicial, final, cargahr)


main()

