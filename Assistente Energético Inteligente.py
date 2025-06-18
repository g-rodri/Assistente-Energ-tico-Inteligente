# SmartEnergyBot - prototipo de automação de energia

import time
import random

# Limiar de consumo em Watts
CONSUMO_MAXIMO = 100

# Carga que será controlada
carga_ligada = False


def obter_dados_sensor():
    """Simula a saída de um sensor de energia."""
    return random.randint(50, 150)


def acionar_carga():
    """Liga a saída da carga."""
    global carga_ligada
    carga_ligada = True
    print("Carga ligada!")


def desacionar_carga():
    """Desativa a saída da carga."""
    global carga_ligada
    carga_ligada = False
    print("Carga desligada")


def processar_comando(comando):
    """Processa o comando de voz recebido pelo usuário."""
    comando = comando.strip().lower()
    if comando == "ligar carga":
        acionar_carga()
    elif comando == "desligar carga":
        desacionar_carga()
    elif comando == "status":
        print(f"Consumo atual: {obter_dados_sensor()} Watts")
        print(f"Carga ligada: {carga_ligada}")


def main():
    print("Assistente SmartEnergyBot iniciado.")
    print("Informe um comando (ligar carga, desligar carga, status ou saída).")

    try:
        while True:
            # Coleta o consumo de energia
            consumo = obter_dados_sensor()
            print(f"Dados do sensor: {consumo} Watts")

            if consumo > CONSUMO_MAXIMO and carga_ligada:
                print("⚡ Consumo excedeu o limiar! Desligando a carga.")
                desacionar_carga()

            # Aplicação de comando de voz
            comando = input("Comando de voz: ").strip()
            if comando == "saida":
                break
            processar_comando(comando)
            time.sleep(2)
    except KeyboardInterrupt:
        print("Saindo do SmartEnergyBot.")


if __name__ == "__main__":
    main()
