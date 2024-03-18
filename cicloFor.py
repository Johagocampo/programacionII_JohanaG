vuelo={
    "aerolinea": "avianca",
    "vuelo": "AV3102",
    "origen": "CTG",
    "destino": "MDE",
    "tipo.maleta": ["cabina", "mano", "bodega"]
}
print("valores del diccionario de vuelo ")
for key, value in vuelo.items():
    print(f"{key}: {value}")

print("valores del diccionario de maleta ")
for maleta in vuelo["tipo.maleta"]:
    print(maleta)