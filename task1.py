import networkx as nx
import matplotlib.pyplot as plt

# Створюємо порожній граф
G = nx.Graph()

# Додаємо станції метро (вершини графа)
stations = [
    'Лісова', 'Чернігівська', 'Дарниця', 'Лівобережна', 'Гідропарк', 'Арсенальна',
    'Хрещатик', 'Театральна', 'Університет', 'Вокзальна', 'Політехнічний інститут',
    'Шулявська', 'Берестейська', 'Нивки', 'Святошин', 'Житомирська', 'Академмістечко',

    'Героїв Дніпра', 'Мінська', 'Оболонь', 'Почайна', 'Тараса Шевченка', 'Контрактова площа',
    'Поштова площа', 'Майдан Незалежності', 'Площа Льва Толстого', 'Олімпійська', 'Палац Україна',
    'Либідська', 'Деміївська', 'Голосіївська', 'Васильківська', 'Виставковий центр', 'Іподром', 'Теремки',

    'Сирець', 'Дорогожичі', 'Лук’янівська', 'Золоті ворота', 'Палац спорту', 'Кловська',
    'Печерська', 'Дружби народів', 'Видубичі', 'Славутич', 'Осокорки', 'Позняки', 'Харківська', 'Вирлиця', 'Бориспільська', 'Червоний хутір'
]

# Додаємо станції як вершини графа
G.add_nodes_from(stations)

# Зв'язки між станціями (ребра графа)
connections = [
    # Червона лінія
    ('Лісова', 'Чернігівська'), ('Чернігівська', 'Дарниця'), ('Дарниця', 'Лівобережна'),
    ('Лівобережна', 'Гідропарк'), ('Гідропарк', 'Арсенальна'), ('Арсенальна', 'Хрещатик'),
    ('Хрещатик', 'Театральна'), ('Театральна', 'Університет'), ('Університет', 'Вокзальна'),
    ('Вокзальна', 'Політехнічний інститут'), ('Політехнічний інститут', 'Шулявська'),
    ('Шулявська', 'Берестейська'), ('Берестейська', 'Нивки'), ('Нивки', 'Святошин'),
    ('Святошин', 'Житомирська'), ('Житомирська', 'Академмістечко'),

    # Синя лінія
    ('Героїв Дніпра', 'Мінська'), ('Мінська', 'Оболонь'), ('Оболонь', 'Почайна'),
    ('Почайна', 'Тараса Шевченка'), ('Тараса Шевченка', 'Контрактова площа'),
    ('Контрактова площа', 'Поштова площа'), ('Поштова площа', 'Майдан Незалежності'),
    ('Майдан Незалежності', 'Площа Льва Толстого'), ('Площа Льва Толстого', 'Олімпійська'),
    ('Олімпійська', 'Палац Україна'), ('Палац Україна', 'Либідська'), ('Либідська', 'Деміївська'),
    ('Деміївська', 'Голосіївська'), ('Голосіївська', 'Васильківська'), ('Васильківська', 'Виставковий центр'),
    ('Виставковий центр', 'Іподром'), ('Іподром', 'Теремки'),

    # Зелена лінія
    ('Сирець', 'Дорогожичі'), ('Дорогожичі', 'Лук’янівська'), ('Лук’янівська', 'Золоті ворота'),
    ('Золоті ворота', 'Палац спорту'), ('Палац спорту', 'Кловська'), ('Кловська', 'Печерська'),
    ('Печерська', 'Дружби народів'), ('Дружби народів', 'Видубичі'), ('Видубичі', 'Славутич'),
    ('Славутич', 'Осокорки'), ('Осокорки', 'Позняки'), ('Позняки', 'Харківська'),
    ('Харківська', 'Вирлиця'), ('Вирлиця', 'Бориспільська'), ('Бориспільська', 'Червоний хутір'),

    # Пересадочні станції
    ('Хрещатик', 'Майдан Незалежності'), ('Театральна', 'Золоті ворота'),
    ('Палац спорту', 'Площа Льва Толстого')
]

# Додаємо ребра до графа
G.add_edges_from(connections)

# Малюємо граф
plt.figure(figsize=(12, 12))
pos = nx.spring_layout(G)  # Оптимізована схема розташування вершин

nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_weight="bold", edge_color="gray")

plt.title("Граф станцій метро Києва")
plt.show()

print(f"Кількість вершин: {G.number_of_nodes()}")
print(f"Кількість ребер: {G.number_of_edges()}")
print("Максимальна ступінь вершин - 3 для пересадочних станцій, мінімальна - 1, для кінцевих.")