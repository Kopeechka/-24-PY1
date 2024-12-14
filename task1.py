import doctest
from typing import Union


class Tree:
    def __init__(self, branch_amount: Union[int], stem_division: Union[int]):
        self.branch_amount = branch_amount
        self.stem_division = stem_division

        if not isinstance(branch_amount, int):
            raise TypeError
        if branch_amount < 0:
            raise ValueError
        self.branch_amount = branch_amount

        if not isinstance(stem_division, int):
            raise TypeError
        if stem_division < 0:
            raise ValueError
        self.stem_division = stem_division

    def grow(self, branch_amount: int):
        """
        Рост дерева (branch_amount растёт)

        Примеры:
        >>> tree = Tree(10, 5)
        >>> tree.grow()
        """
        if not isinstance(branch_amount, int):
            raise TypeError
        self.branch_amount += branch_amount
        ...

    def prune(self, branches_to_remove: int):
        """
        Обрезка дерева (branch_amount уменьшается)

        :param branches_to_remove: Количество ветвей для обрезки

        Примеры:
        >>> tree = Tree(10, 5)
        >>> tree.prune(2)
        """
        if not isinstance(branches_to_remove, int):
            raise TypeError
        self.branch_amount -= branches_to_remove
        ...


tree = Tree(254, 4)
help(tree)


class Comics:
    def __init__(self, author: str, pages: int):
        """ Инициализация экземпляра класса. """
        self.author = author
        self.pages = pages

    def increment_last_read_page(self, read_pages: int):
        """
        Метод увеличивает последнюю прочитанную страницу.

        :param read_pages: Количество прочитанных страниц
        """
        if not isinstance(read_pages, int):
            raise TypeError

        if read_pages < 0:
            raise ValueError

        self.pages += read_pages

    def author_name_correction(self, new_author: str):
        """
        Метод изменяет имя автора в случае опечатки

        :param new_author: имя автора
        """
        if not isinstance(new_author, str):
            raise TypeError("Новое имя автора должно быть строкой")

        self.author = new_author


comics = Comics("Автор", 500)
comics.increment_last_read_page(1)
help(comics)


class Car:
    def __init__(self, brand: str, model: str, fuel_capacity: float):
        """
        :param brand: Бренд автомобиля
        :param model: Модель автомобиля
        :param fuel_capacity: Емкость топливного бака в литрах
        Примеры:
        >>> car = Car("Toyota", "Camry", 50.0)
        """
        self.brand = brand
        self.model = model
        self.fuel_capacity = fuel_capacity
        self.current_fuel_level = 0.0  # начальный уровень топлива

        if not isinstance(brand, str):
            raise TypeError
        if not isinstance(model, str):
            raise TypeError
        if not isinstance(fuel_capacity, (int, float)):
            raise TypeError
        if fuel_capacity <= 0:
            raise ValueError

    def refuel(self, fuel_amount: float) -> None:
        """
        Заправка автомобиля топливом

        :param fuel_amount: Количество добавляемого топлива в литрах

        :raise ValueError: Если количество добавляемого топлива превышает емкость бака, то вызываем ошибку

        Примеры:
        >>> car = Car("Toyota", "Camry", 50.0)
        >>> car.refuel(20.0)
        """
        if not isinstance(fuel_amount, (int, float)):
            raise TypeError
        if fuel_amount < 0:
            raise ValueError

        self.current_fuel_level += fuel_amount
        if self.current_fuel_level > self.fuel_capacity:
            self.current_fuel_level = self.fuel_capacity

    def drive(self, distance: float) -> None:
        """
        Вождение автомобиля на определенное расстояние.

        :param distance: Расстояние в километрах

        :raise ValueError: Если расстояние отрицательное, то вызываем ошибку

        Примеры:
        >>> car = Car("Toyota", "Camry", 50.0)
        >>> car.drive(100.0)
        """
        if not isinstance(distance, (int, float)):
            raise TypeError
        if distance < 0:
            raise ValueError

        # расход 1 л на 10 км
        fuel_consumption = distance / 10.0
        if fuel_consumption > self.current_fuel_level:
            raise ValueError

        self.current_fuel_level -= fuel_consumption

    def check_fuel_level(self) -> float:
        """
        Проверка текущего уровня топлива.

        :return: Текущий уровень топлива в литрах

        Примеры:
        >>> car = Car("Toyota", "Camry", 50.0)
        >>> car.check_fuel_level()
        """
        ...


car = Car("Toyota", "Camry", 50.0)
help(car)


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
