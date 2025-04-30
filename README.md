# 🧮 Calculadora Python + Bash

Este projeto foi criado como parte do meu aprendizado no curso de **Análise de Dados**, demonstrando conhecimentos básicos de automação com Bash e lógica de programação com Python. A aplicação é uma calculadora interativa executada a partir de um script Bash.

## 📂 Estrutura de Arquivos

```
📁 calculator/
├── calculator.py         # Lógica da calculadora em Python
├── calculator.sh         # Script Bash que dá boas-vindas e executa o programa Python
└── comandos.txt          # Arquivo com comandos úteis para execução
```

## ▶️ Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/DevGuiPereira/Curso_Analise_de_Dados
cd Curso_Analise_de_Dados
```

### 2. Dê permissão de execução aos arquivos

```bash
chmod 755 calculator.sh
chmod 755 calculator.py
```

### 3. Execute o script principal

```bash
./calculator.sh
```

## 💡 Sobre o Funcionamento

- Ao rodar `calculator.sh`, o terminal exibe uma saudação personalizada com o nome do usuário.
- Em seguida, a calculadora é aberta e você pode realizar operações matemáticas como:
  - Soma (+)
  - Subtração (-)
  - Multiplicação (*)
  - Divisão (/)
  - Potenciação (**)
- A cada operação, o usuário pode optar por continuar calculando ou encerrar.

## 🧠 Conhecimentos Aplicados

- Scripts Bash (mensagens, execução de programas)
- Lógica condicional e funções em Python
- Estrutura interativa com `input()` e `while`
- Permissões de execução no Linux (`chmod`)

## 📌 Observações

- Certifique-se de ter o **Python 3** instalado no seu sistema.
- O script deve ser executado em ambientes Unix/Linux. Para Windows, recomenda-se o uso do Git Bash ou WSL.

## 🤝 Contribuição

Sinta-se livre para sugerir melhorias, abrir issues ou criar pull requests! Esse projeto é simples, mas ótimo para treinar boas práticas.
