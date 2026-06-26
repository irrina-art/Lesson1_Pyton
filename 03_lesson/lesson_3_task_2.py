from smartphone import Smartphone
catalog = [
    Smartphone("Apple", "iPhone 15 Pro", "+79867651243"),
    Smartphone("Samsung", "Galaxy S24 Ultra", "+79812319875"),
    Smartphone("Xiaomi", "Redmi Note 13", "+79139210796"),
    Smartphone("Google", "Pixel 8", "+79139451235"),
    Smartphone("OnePlus", "Nord CE 4 Lite", "+79139450792")
]

for smartphone in catalog:
    print(f"{smartphone.marka} - {smartphone.model}.{smartphone.number}")
