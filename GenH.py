import networkx as nx


Mapa = nx.Graph()

#Línea 1
Mapa.add_edge("Observatorio", "Tacubaya", weight=2)
Mapa.add_edge("Tacubaya", "Juanacatlán", weight= 3)
Mapa.add_edge("Juanacatlán", "Chapultepec", weight= 2)
Mapa.add_edge("Chapultepec", "Sevilla",  weight=2)
Mapa.add_edge("Sevilla", "Insurgentes",  weight=2)
Mapa.add_edge("Insurgentes", "Cuauhtémoc",  weight=2)
Mapa.add_edge("Cuauhtémoc", "Balderas",  weight=2)


#Línea 3
Mapa.add_edge("Juárez", "Balderas",  weight=2)
Mapa.add_edge("Balderas", "Niños Héroes",  weight=2)
Mapa.add_edge("Niños Héroes", "Hospital General",  weight=2)
Mapa.add_edge("Hospital General", "Centro Médico", weight= 2)
Mapa.add_edge("Centro Médico", "Etiopía",  weight=2)
Mapa.add_edge("Etiopía", "Eugenia",  weight=2)
Mapa.add_edge("Eugenia", "División del Norte",  weight=2)
Mapa.add_edge("División del Norte", "Zapata", weight= 2)
Mapa.add_edge("Zapata", "Coyoacán",  weight=2)
Mapa.add_edge("Coyoacán", "Viveros",  weight=2)
Mapa.add_edge("Viveros", "Miguel Ángel de Quevedo", weight=2)
Mapa.add_edge("Miguel Ángel de Quevedo", "Copilco", weight=2)
Mapa.add_edge("Copilco", "Universidad", weight=3)

#Línea 7
Mapa.add_edge("Polanco", "Auditorio", weight= 2)
Mapa.add_edge("Auditorio", "Constituyentes",weight= 2)
Mapa.add_edge("Constituyentes", "Tacubaya", weight=2)
Mapa.add_edge("Tacubaya", "San Pedro de los Pinos",weight= 2)
Mapa.add_edge("San Pedro de los Pinos", "San Antonio",weight= 2)
Mapa.add_edge("San Antonio", "Mixcoac",weight= 2)
Mapa.add_edge("Mixcoac", "Barranca del Muerto", weight=3)

#Línea 9
Mapa.add_edge("Tacubaya", "Patriotismo", weight=2)
Mapa.add_edge("Patriotismo", "Chilpancingo", weight=2)
Mapa.add_edge("Chilpancingo", "Centro Médico", weight=2)
Mapa.add_edge("Centro Médico", "Lázaro Cárdenas", weight=2)

#Línea 12
Mapa.add_edge("Mixcoac", "Insurgentes Sur", weight=2)
Mapa.add_edge("Insurgentes Sur", "Hospital 20 de Noviembre", weight=2)
Mapa.add_edge("Hospital 20 de Noviembre", "Parque de los Venados", weight=2)
Mapa.add_edge("Parque de los Venados", "Eje Central", weight=2)

for node_target in Mapa:
    for node_start in Mapa:
        if node_target == node_start:
            continue
        
        print(nx.dijkstra_path_length(Mapa, node_start, node_target))
