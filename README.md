O SmartEnergyBot foi pensado para ser um assistente simples e funcional na automação de energia. Toda a estrutura do código foi organizada de forma bem clara, separando cada tarefa em funções específicas, o que deixa tudo mais fácil de se utilizar
As funções obter_dados_sensor(), acionar_carga() e desacionar_carga() são responsáveis por simular a leitura dos sensores e controlar o acionamento da carga.
A função processar_comando() permite a interação do usuário com o sistema através de comandos de voz simulados, como “ligar carga”, “desligar carga” e “status”.
A função principal main() nos ajuda a concentrar o fluxo principal do programa, fazendo a leitura contínua dos dados inputados pelo sensor, avaliando se o consumo ultrapassa o limite e permitindo que o usuário insira comandos para interagir com o sistema.
Além disso, o uso do try-except permite uma finalização segura da aplicação, seja por comando ou por interrupção manual.
