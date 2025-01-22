import turtle, math  # Импортируем необходимые библиотеки

# Функция кластеризации
def clusterization(data, r):
    clusters = []
    while data:
        cluster = [data.pop()]
        for p1 in cluster:
            neighbors = [p2 for p2 in data if math.dist(p1, p2) <= r]
            cluster.extend(neighbors)
            for p in neighbors:
                data.remove(p)
        clusters.append(cluster)
    return clusters

# Функция для визуализации кластеров на экране
def visual(clusters):
    turtle.up()
    turtle.tracer(0)
    colors = ["red", "yellow", "blue", "purple", "black"]
    for i, cluster in enumerate(clusters):
        for x, y in cluster:
            turtle.goto(x * 30, y * 30)
            turtle.dot(10, colors[i % len(colors)])
    turtle.done()

# Функция для вычисления центроида (среднего центра) кластера
def get_centroid(cluster):
    x_mean = sum(p[0] for p in cluster) / len(cluster)
    y_mean = sum(p[1] for p in cluster) / len(cluster)
    return (x_mean, y_mean)  # Возвращаем кортеж (x_mean, y_mean) — центр кластера

# Функция для вычисления средних значений центров всех кластеров
def calculate_average_centroids(clusters):
    centroids = [get_centroid(cluster) for cluster in clusters]  # Находим центры всех кластеров
    # Рассчитываем среднее арифметическое для абсцисс и ординат центров
    Px = sum(centroid[0] for centroid in centroids) / len(centroids)
    Py = sum(centroid[1] for centroid in centroids) / len(centroids)
    return Px, Py

def read_data(filename):
    # Считываем все строки из файла и преобразуем их в список координат
    return [list(map(float, line.split())) for line in open(filename)]

# Основная логика программы
data_a = read_data("27data/27-53a.txt")
clusters_a = clusterization(data_a, 0.8)  # Выполняем кластеризацию с радиусом 0.8
Px_a, Py_a = calculate_average_centroids(clusters_a)  # Рассчитываем среднее значение для файла A

data_b = read_data("27data/27-53b.txt")
clusters_b = clusterization(data_b, 0.8)  # Выполняем кластеризацию с радиусом 0.8
Px_b, Py_b = calculate_average_centroids(clusters_b)  # Рассчитываем среднее значение для файла B

print(f"{int(Px_a * 100000)} {int(Py_a * 100000)}")
print(f"{int(Px_b * 100000)} {int(Py_b * 100000)}")

visual(clusters_a)  # Визуализируем кластеры для файла A
