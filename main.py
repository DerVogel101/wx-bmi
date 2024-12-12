from typing import Optional


class BmiCatSimple:
    def __init__(self):
        self.categories = [
            ("Untergewicht", (None, 18.5)),
            ("Normalgewicht", (18.5, 24.9)),
            ("Übergewicht", (25, 29.9)),
            ("Starkes Übergewicht (Adipositas Grad I)", (30, 34.9)),
            ("Adipositas Grad II", (35, 39.9)),
            ("Adipositas Grad III", (40, None))
        ]

    def __getitem__(self, item: float) -> str:
        for cat, (lower, upper) in self.categories:
            if lower is None and item < upper:
                return cat
            if upper is None and item >= lower:
                return cat
            if lower is not None and upper is not None and lower <= item < upper:
                return cat
        return "Unbekannt"

class BmiAgeSex(BmiCatSimple):
    def __init__(self, sex: str, ):
        super().__init__()
        self.categories_male = [
            ("Untergewicht", (None, 20)),
            ("Normalgewicht", (20, 24.9)),
            ("Übergewicht", (25, 29.9)),
            ("Starkes Übergewicht (Adipositas Grad I)", (30, 34.9)),
            ("Adipositas Grad II", (35, 39.9)),
            ("Adipositas Grad III", (40, None))
        ]

    def __getitem__(self, item):
        for cat, (lower, upper) in self.categories:
            if lower is None and item < upper:
                return cat
            if upper is None and item >= lower:
                return cat
            if lower is not None and upper is not None and lower <= item < upper:
                return cat
        return "Unbekannt"
bmi = BmiCatSimple()  # Übergewicht
print(bmi[25])  # Übergewicht


class BmiError(Exception):
    pass

class SexError(BmiError):
    pass

class AgeDiscriminationError(BmiError):
    pass

class SizeError(BmiError):
    pass

class WeightError(BmiError):
    pass

class BmiCalc:
    def __init__(self):
        self.__age = None
        self.__weight = None
        self.__sex = None
        self.__size = None

    def get_bmi(self) -> float:
        """ :return: current BMI """
        if self.__size is None:
            raise SizeError("Size is not set. Please set a size in meters")
        if self.__weight is None:
            raise WeightError("Weight is not set. Please set a weight in kg")
        return self.__weight / (self.__size ** 2)

    def get_category(self) -> str:
        """
        :return: current weight category as string
        """
        pass  # TODO

    def get_age(self) -> int | None:
        """ get current age
        :return: current age
        """
        return self.__age

    def set_age(self, age: Optional[int]) -> None:
        """ Set new or reset age
        :param age: new age or None to reset
        """
        if age is not None and age < 0:
            raise AgeDiscriminationError(f"The age: {age} is not a valid age. Please use a positive number or None")

        self.__age = age

    def get_sex(self) -> str | None:
        """ get current sex as 'm' or 'f' or None
        :return: current sex
        """
        return self.__sex

    def set_sex(self, sex: Optional[str]) -> None:
        """ Set new or reset sex
        :param sex: new sex as 'm' or 'f' or None
        """
        if sex not in ['m', 'f', None]:
            raise SexError(f"The sex: {sex} is not right. Please use 'm' or 'f' or None")
        self.__sex = sex

    def get_size(self) -> float:
        """ get current size
        :return: current size in meters
        """
        if self.__size is None:
            raise SizeError("Size is not set. Please set a size in meters")
        return self.__size

    def set_size(self, size: float) -> None:
        """ Set new size in meters
        :param size: new size
        """
        if size < 0 or not isinstance(size, (int, float)):
            raise SizeError(f"The size: {size} is not a valid size. Please use a positive float number")
        self.__size = size

    def get_weight(self) -> float:
        """ get current weight
        :return: current weight in kg
        """
        if self.__weight is None:
            raise WeightError("Weight is not set. Please set a weight in kg")
        return float(self.__weight)

    def set_weight(self, weight: float) -> None:
        """ Set new weight in meters
        :param weight: new weight
        """
        if weight < 0 or not isinstance(weight, (int, float)):
            raise WeightError(f"The weight: {weight} is not a valid weight. Please use a positive float number")
        self.__weight = weight

    def get_ideal_weight(self) -> float:
        """ calculate ideal weight
        :return: ideal weight in gk
        """
        pass  # TODO


if __name__ == '__main__':
    bmi = BmiCalc()
    bmi.set_age(-25)