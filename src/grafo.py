import networkx as nx

# creamos el grafo
Mapa = nx.Graph()

# definicion de lineas y pesos basados en gtfs oficial
# los pesos representan minutos

# linea 1 (rosa) observatorio - balderas
Mapa.add_edge("Observatorio_L1", "Tacubaya_L1", weight=2.83)
Mapa.add_edge("Tacubaya_L1", "Juanacatlan_L1", weight=2.56)
Mapa.add_edge("Juanacatlan_L1", "Chapultepec_L1", weight=2.20)
Mapa.add_edge("Chapultepec_L1", "Sevilla_L1", weight=1.12)
Mapa.add_edge("Sevilla_L1", "Insurgentes_L1", weight=1.65)
Mapa.add_edge("Insurgentes_L1", "Cuauhtemoc_L1", weight=1.85)
Mapa.add_edge("Cuauhtemoc_L1", "Balderas_L1", weight=1.08)

# linea 3 (verde oliva) universidad - juarez
Mapa.add_edge("Juarez_L3", "Balderas_L3", weight=1.40)
Mapa.add_edge("Balderas_L3", "Ninos Héroes_L3", weight=1.43)
Mapa.add_edge("Ninos Héroes_L3", "Hospital General_L3", weight=1.42)
Mapa.add_edge("Hospital General_L3", "Centro Medico_L3", weight=1.37)
Mapa.add_edge("Centro Medico_L3", "Etiopia_L3", weight=2.40)
Mapa.add_edge("Etiopia_L3", "Eugenia_L3", weight=1.98)
Mapa.add_edge("Eugenia_L3", "Division del Norte_L3", weight=1.48)
Mapa.add_edge("Division del Norte_L3", "Zapata_L3", weight=1.88)
Mapa.add_edge("Zapata_L3", "Coyoacan_L3", weight=2.33)
Mapa.add_edge("Coyoacan_L3", "Viveros_L3", weight=1.90)
Mapa.add_edge("Viveros_L3", "Miguel Ángel de Quevedo_L3", weight=1.80)
Mapa.add_edge("Miguel Ángel de Quevedo_L3", "Copilco_L3", weight=2.70)
Mapa.add_edge("Copilco_L3", "Universidad_L3", weight=2.63)

# linea 7 (naranja) barranca del muerto - polanco
Mapa.add_edge("Polanco_L7", "Auditorio_L7", weight=1.40)
Mapa.add_edge("Auditorio_L7", "Constituyentes_L7", weight=2.68)
Mapa.add_edge("Constituyentes_L7", "Tacubaya_L7", weight=1.88)
Mapa.add_edge("Tacubaya_L7", "San Pedro de los Pinos_L7", weight=2.01)
Mapa.add_edge("San Pedro de los Pinos_L7", "San Antonio_L7", weight=1.28)
Mapa.add_edge("San Antonio_L7", "Mixcoac_L7", weight=1.45)
Mapa.add_edge("Mixcoac_L7", "Barranca del Muerto_L7", weight=2.66)

# linea 9 (marron) tacubaya - lazaro cardenas
Mapa.add_edge("Tacubaya_L9", "Patriotismo_L9", weight=2.78)
Mapa.add_edge("Patriotismo_L9", "Chilpancingo_L9", weight=1.70)
Mapa.add_edge("Chilpancingo_L9", "Centro Medico_L9", weight=2.28)
Mapa.add_edge("Centro Medico_L9", "Lazaro Cardenas_L9", weight=1.87)

# linea 12 (oro) mixcoac - eje central
Mapa.add_edge("Mixcoac_L12", "Insurgentes Sur_L12", weight=2.08)
Mapa.add_edge("Insurgentes Sur_L12", "Hospital 20 de Noviembre_L12", weight=1.80)
Mapa.add_edge("Hospital 20 de Noviembre_L12", "Zapata_L12", weight=1.28)
Mapa.add_edge("Zapata_L12", "Parque de los Venados_L12", weight=1.67)
Mapa.add_edge("Parque de los Venados_L12", "Eje Central_L12", weight=3.30)

# transbordos permitidos
# 1 mixcoac
Mapa.add_edge("Mixcoac_L7", "Mixcoac_L12", weight=4.0)

# 2 zapata
Mapa.add_edge("Zapata_L3", "Zapata_L12", weight=3.5)

# 3 tacubaya
Mapa.add_edge("Tacubaya_L1", "Tacubaya_L7", weight=3.5)
Mapa.add_edge("Tacubaya_L7", "Tacubaya_L9", weight=3.5)
Mapa.add_edge("Tacubaya_L9", "Tacubaya_L1", weight=3.5)

# 4 centro medico
Mapa.add_edge("Centro Medico_L3", "Centro Medico_L9", weight=3.0)

# 5 balderas
Mapa.add_edge("Balderas_L1", "Balderas_L3", weight=2.5)
