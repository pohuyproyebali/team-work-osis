import os
import sys

names = ["Аль-Хайтам", "Альбедо", "Аяка", "Аято", "Бай Джу", "Барбара", "Беннет","Бэй Доу", "Венти", "Гань Юй", "Горо", "Джинн", "Диюк", "Диона", "Дори", "Дэхья", "Е Лань", "Ёимия", 
        "Итто", "Кавех", "Кадзуха", "Кандакия", "Кирара", "Кли", "Кокоми", "Коллеи", "Кэ Цин", "Кэйа", "Лайла", "Лиза", "Линетт", "Лини", "Мика", "Мона", "Нахида", "Нёвиллет", "Нилу", "Нин Гуан",
        "Ноэль", "Путешественник", "Райден", "Ризли", "Розария", "Рейзор", "Сайно", "Сара", "Сахароза", "Саю", "Син Цю", "Синобу", "Синь Янь", "Странник", "Сян Лин", "Сяо", "Тарталья",
        "Тигнари", "Тома", "Фарузан", "Фишль", "Фремине", "Фурина","Ху Тао", "Хейдзо", "Ци ци", "Чжун Ли", "Чунь Юнь", "Шарлотта", "ШеньХе", "Элой", "Эмбер", "Эола", "Юнь Цзинь", "Янь Фей",
        "Яо Яо", "Яэ Мико"]

for i in range(0, len(names)):
    with open(names[i] + ".txt", "a+") as file:
        file.write("aboba" +str( i))


