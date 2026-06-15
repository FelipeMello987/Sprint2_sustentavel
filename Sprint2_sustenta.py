import random
 
random.seed(42)
 
HORAS = 24
CAPACIDADE_BATERIA = 100.0
bateria = 50.0
 
carregadores = [
    {"id": 1, "nome": "Carregador A - Emergencia", "prioridade": 1, "potencia": 11.0},
    {"id": 2, "nome": "Carregador B - Preferencial", "prioridade": 2, "potencia": 7.4},
    {"id": 3, "nome": "Carregador C - Padrao", "prioridade": 3, "potencia": 7.4},
    {"id": 4, "nome": "Carregador D - Padrao", "prioridade": 4, "potencia": 3.7},
]
 
 
def gerar_solar(hora):
    if hora < 6 or hora > 19:
        return 0.0
    pico = 13
    geracao = 30.0 * max(0, 1 - ((hora - pico) / 7) ** 2)
    geracao *= random.uniform(0.7, 1.0)
    return round(geracao, 1)
 
 
def simular_demanda(hora):
    demanda = {}
    for c in carregadores:
        if 7 <= hora <= 9 or 17 <= hora <= 20:
            ativo = random.random() < 0.85
        elif 10 <= hora <= 16:
            ativo = random.random() < 0.60
        else:
            ativo = random.random() < 0.20
        demanda[c["id"]] = c["potencia"] if ativo else 0.0
    return demanda
 
 
def distribuir_energia(energia_disponivel, demanda):
    distribuicao = {}
    restante = energia_disponivel
 
    carregadores_ordenados = sorted(carregadores, key=lambda c: c["prioridade"])
 
    nivel_pct = (bateria / CAPACIDADE_BATERIA) * 100
 
    for c in carregadores_ordenados:
        pedido = demanda[c["id"]]
        if pedido == 0:
            distribuicao[c["id"]] = 0.0
            continue
        if nivel_pct < 20 and c["prioridade"] > 2:
            distribuicao[c["id"]] = 0.0
            continue
        if restante >= pedido:
            distribuicao[c["id"]] = pedido
            restante -= pedido
        elif restante > 0:
            distribuicao[c["id"]] = round(restante, 1)
            restante = 0.0
        else:
            distribuicao[c["id"]] = 0.0
 
    return distribuicao
 
 
print("=" * 50)
print("  SISTEMA SOLAR + BATERIA + CARREGADORES EV")
print("=" * 50)
 
total_gerado = 0.0
total_consumido = 0.0
 
for hora in range(HORAS):
    solar = gerar_solar(hora)
    demanda = simular_demanda(hora)
 
    energia_disponivel = solar + bateria
    distribuicao = distribuir_energia(energia_disponivel, demanda)
 
    consumo = sum(distribuicao.values())
 
    energia_liquida = solar - consumo
    if energia_liquida > 0:
        espaco = CAPACIDADE_BATERIA - bateria
        bateria += min(energia_liquida, espaco)
    else:
        bateria -= min(abs(energia_liquida), bateria)
 
    bateria = max(0.0, min(CAPACIDADE_BATERIA, bateria))
    nivel = (bateria / CAPACIDADE_BATERIA) * 100
 
    if nivel < 20:
        status = "CRITICO"
    elif nivel < 40:
        status = "BAIXO"
    elif nivel < 80:
        status = "NORMAL"
    else:
        status = "CHEIO"
 
    total_gerado += solar
    total_consumido += consumo
 
    print(f"\n[HORA {hora:02d}:00]")
    print(f"  Solar: {solar:.1f} kW | Bateria: {bateria:.1f} kWh ({nivel:.0f}%) [{status}]")
    for c in carregadores:
        pot = distribuicao[c["id"]]
        estado = "ATIVO" if pot > 0 else "INATIVO"
        print(f"  {c['nome']}: {pot:.1f} kW [{estado}]")
 
print("\n" + "=" * 50)
print("  RELATORIO FINAL")
print("=" * 50)
print(f"Energia gerada   : {total_gerado:.1f} kWh")
print(f"Energia consumida: {total_consumido:.1f} kWh")
print(f"Bateria final    : {bateria:.1f} kWh ({(bateria / CAPACIDADE_BATERIA * 100):.0f}%)")
print("=" * 50)