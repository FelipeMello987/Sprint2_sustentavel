# Sistema de Energia Solar + Bateria + Carregadores EV

Simulação de um sistema de captação de energia solar, armazenamento em bateria e distribuição inteligente para carregadores de veículos elétricos.

---

## Descrição

O sistema simula 24 horas de operação de uma microrrede energética renovável. Painéis solares geram energia ao longo do dia, o excedente é armazenado em uma bateria, e um algoritmo de prioridade distribui essa energia para até 4 carregadores de veículos elétricos de forma inteligente e eficiente.

---

## Arquitetura do Sistema

```
[Painéis Solares]
       |
       v
[Controlador de Carga]
       |
  _____|_____
 |           |
 v           v
[Bateria]  [Algoritmo de Distribuição]
            |
     ________|________
     |    |    |    |
     v    v    v    v
    [EV1][EV2][EV3][EV4]
```

**Componentes:**

- **Painéis Solares** — geram energia entre 6h e 19h com pico ao meio-dia, com variação simulada de cobertura de nuvens
- **Bateria** — capacidade de 100 kWh, inicia com 50% de carga, carrega com excedente solar e descarrega para suprir déficit
- **Algoritmo de Distribuição** — ordena os carregadores por prioridade e aloca energia de forma inteligente, protegendo a bateria em situações críticas
- **Carregadores EV** — 4 pontos de recarga com potências e prioridades diferentes

---

## Carregadores e Prioridades

| ID | Nome | Prioridade | Potência |
|----|------|------------|----------|
| 1 | Carregador A - Emergência | 1 (mais alta) | 11.0 kW |
| 2 | Carregador B - Preferencial | 2 | 7.4 kW |
| 3 | Carregador C - Padrão | 3 | 7.4 kW |
| 4 | Carregador D - Padrão | 4 (mais baixa) | 3.7 kW |

---

## Algoritmo de Distribuição Inteligente

1. Calcula a energia disponível (geração solar + carga atual da bateria)
2. Ordena os carregadores do mais prioritário ao menos prioritário
3. Atende cada carregador na ordem, respeitando a energia restante
4. Se a bateria estiver abaixo de 20%, desativa carregadores de prioridade 3 e 4 para proteger o sistema
5. O excedente solar é armazenado na bateria até o limite de capacidade

---

## Princípios de Energias Renováveis e Sustentabilidade

- **Aproveitamento solar** — toda a energia consumida pelos EVs vem de fonte renovável (solar), com a bateria como buffer
- **Eficiência energética** — o algoritmo de prioridade evita desperdício, garantindo que a energia disponível seja usada onde é mais necessária
- **Gestão de armazenamento** — a bateria é protegida de descargas profundas, aumentando sua vida útil
- **Mobilidade elétrica** — integração direta com carregadores de EV, promovendo transporte limpo alimentado por energia solar

---

## Como Executar

**Pré-requisitos:**
- Python 3.x instalado

**Instalação:**
```bash
git clone https://github.com/FelipeMello987/Sprint2_sustentavel.git
cd Sprint2_sustentavel
```

**Execução:**
```bash
python Sprint2_sustenta.py
```

Não são necessárias bibliotecas externas além do `random`, que já vem com o Python.

---

## Exemplo de Saída

```
==================================================
  SISTEMA SOLAR + BATERIA + CARREGADORES EV
==================================================

[HORA 13:00]
  Solar: 28.4 kW | Bateria: 72.3 kWh (72%) [NORMAL]
  Carregador A - Emergencia: 11.0 kW [ATIVO]
  Carregador B - Preferencial: 7.4 kW [ATIVO]
  Carregador C - Padrao: 7.4 kW [ATIVO]
  Carregador D - Padrao: 0.0 kW [INATIVO]

==================================================
  RELATORIO FINAL
==================================================
Energia gerada   : 232.1 kWh
Energia consumida: 282.1 kWh
Bateria final    : 0.0 kWh (0%)
==================================================
```

---
