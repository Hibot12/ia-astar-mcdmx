import networkx as nx


Mapa = nx.Graph()

# Línea 1  (Observatorio -> Balderas)
Mapa.add_edge("Observatorio", "Tacubaya", weight=3)  # ~2.8 min
Mapa.add_edge("Tacubaya", "Juanacatlán", weight=3)  # ~2.6 min
Mapa.add_edge("Juanacatlán", "Chapultepec", weight=2)  # ~2.2 min
Mapa.add_edge("Chapultepec", "Sevilla", weight=1)  # ~1.1 min
Mapa.add_edge("Sevilla", "Insurgentes", weight=2)  # ~1.6 min
Mapa.add_edge("Insurgentes", "Cuauhtémoc", weight=2)  # ~1.9 min
Mapa.add_edge("Cuauhtémoc", "Balderas", weight=1)  # ~1.1 min


# Línea 3  (Universidad -> Juárez)
Mapa.add_edge("Universidad", "Copilco", weight=3)  # ~2.6 min
Mapa.add_edge("Copilco", "Miguel Ángel de Quevedo", weight=3)  # ~2.7 min
Mapa.add_edge("Miguel Ángel de Quevedo", "Viveros", weight=2)  # ~1.8 min
Mapa.add_edge("Viveros", "Coyoacán", weight=2)  # ~1.9 min
Mapa.add_edge("Coyoacán", "Zapata", weight=2)  # ~2.3 min
Mapa.add_edge("Zapata", "División del Norte", weight=2)  # ~1.9 min
Mapa.add_edge("División del Norte", "Eugenia", weight=2)  # ~1.5 min
Mapa.add_edge("Eugenia", "Etiopía", weight=2)  # ~2.0 min
Mapa.add_edge("Etiopía", "Centro Médico", weight=2)  # ~2.4 min
Mapa.add_edge("Centro Médico", "Hospital General", weight=1)  # ~1.4 min
Mapa.add_edge("Hospital General", "Niños Héroes", weight=1)  # ~1.4 min
Mapa.add_edge("Niños Héroes", "Balderas", weight=1)  # ~1.4 min
Mapa.add_edge("Balderas", "Juárez", weight=1)  # ~1.4 min


# Línea 7 (Barranca del Muerto -> Polanco)
Mapa.add_edge("Barranca del Muerto", "Mixcoac", weight=3)  # ~2.7 min
Mapa.add_edge("Mixcoac", "San Antonio", weight=1)  # ~1.4 min
Mapa.add_edge("San Antonio", "San Pedro de los Pinos", weight=1)  # ~1.3 min
Mapa.add_edge("San Pedro de los Pinos", "Tacubaya", weight=2)  # ~2.0 min
Mapa.add_edge("Tacubaya", "Constituyentes", weight=2)  # ~1.9 min
Mapa.add_edge("Constituyentes", "Auditorio", weight=3)  # ~2.7 min
Mapa.add_edge("Auditorio", "Polanco", weight=1)  # ~1.4 min

# Línea 9  (Tacubaya -> Lázaro Cárdenas)
Mapa.add_edge("Tacubaya", "Patriotismo", weight=2)  # ~2.5 min
Mapa.add_edge("Patriotismo", "Chilpancingo", weight=2)  # ~1.8 min
Mapa.add_edge("Chilpancingo", "Centro Médico", weight=2)  # ~2.3 min
Mapa.add_edge("Centro Médico", "Lázaro Cárdenas", weight=2)  # ~2.0 min

# Línea 12  (Mixcoac -> Eje Central)
Mapa.add_edge("Mixcoac", "Insurgentes Sur", weight=2)  # ~2.1 min
Mapa.add_edge("Insurgentes Sur", "Hospital 20 de Noviembre", weight=2)  # ~1.8 min
Mapa.add_edge("Hospital 20 de Noviembre", "Zapata", weight=1)  # ~1.3 min
Mapa.add_edge("Zapata", "Parque de los Venados", weight=2)  # ~1.7 min
Mapa.add_edge("Parque de los Venados", "Eje Central", weight=3)  # ~3.3 min
