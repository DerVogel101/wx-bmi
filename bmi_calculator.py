from typing import Optional, Literal


class BmiCatSimple:
    def __init__(self):
        self.categories = (
            ("Untergewicht", (None, 18.5)),
            ("Normalgewicht", (18.5, 24.9)),
            ("Übergewicht", (25, 29.9)),
            ("Starkes Übergewicht (Adipositas Grad I)", (30, 34.9)),
            ("Adipositas Grad II", (35, 39.9)),
            ("Adipositas Grad III", (40, None))
        )

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
    def __init__(self):
        super().__init__()
        self.sex_offset = 0
        self.age = None
        self.categories_male = (
            ("Untergewicht", (None, 20)),
            ("Normalgewicht", (20, 24.9)),
            ("Übergewicht", (25, 29.9)),
            ("Starkes Übergewicht (Adipositas Grad I)", (30, 34.9)),
            ("Adipositas Grad II", (35, 39.9)),
            ("Adipositas Grad III", (40, None))
        )
        self.categories_female = (
            ("Untergewicht", (None, 19)),
            ("Normalgewicht", (19, 23.9)),
            ("Übergewicht", (24, 28.9)),
            ("Starkes Übergewicht (Adipositas Grad I)", (29, 33.9)),
            ("Adipositas Grad II", (34, 38.9)),
            ("Adipositas Grad III", (39, None))
        )
        self.selected_categories = self.categories

    def set_sex(self, sex: str | None):

        match sex:
            case 'm':
                self.selected_categories = self.categories_male
                self.sex_offset = 0.5
            case 'f':
                self.selected_categories = self.categories_female
                self.sex_offset = -0.5
            case _:
                self.selected_categories = self.categories
                self.sex_offset = 0

    def set_age(self, age: int | None):
        self.age = age

    def __getitem__(self, item) -> tuple[str, float | None]:
        category = "Unbekannt"
        ideal_bmi = None

        for cat, (lower, upper) in self.selected_categories:
            if lower is None and item < upper:
                category = cat
            elif upper is None and item >= lower:
                category = cat
            elif lower is not None and upper is not None and lower <= item < upper:
                category = cat

        if not self.age is None:
            if self.age < 18:
                age = 18
            elif self.age > 65:
                age = 65
            else:
                age = self.age
            ideal_bmi = (19.5576073 * (1.0045961 ** age)) + self.sex_offset

        return category, ideal_bmi



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

class BodyTypeError(BmiError):
    pass

class BmiCalc:
    def __init__(self):
        self.body_type = None
        self.__age = None
        self.__weight = None
        self.__sex = None
        self.__size = None
        self.bmi_cat = BmiAgeSex()

    def get_bmi(self) -> float:
        """ :return: current BMI """
        if self.__size is None:
            raise SizeError("Size is not set. Please set a size in meters")
        if self.__weight is None:
            raise WeightError("Weight is not set. Please set a weight in kg")
        return round(self.__weight / (self.__size ** 2), 2)

    def get_category(self) -> str:
        """
        :return: current weight category as string
        """
        return self.bmi_cat[self.get_bmi()][0]

    def get_age(self) -> int | None:
        """get current age
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
        self.bmi_cat.set_age(age)

    def get_sex(self) -> str | None:
        """ get current sex_offset as 'm' or 'f' or None
        :return: current sex_offset
        """
        return self.__sex

    def set_sex(self, sex_string: Optional[Literal['m', 'f']]) -> None:
        """ Set new or reset sex_offset
        :param sex_string: new sex_offset as 'm' or 'f' or None
        """
        if sex_string not in ['m', 'f', None]:
            raise SexError(f"The sex_offset: {sex_string} is not right. Please use 'm' or 'f' or None")
        self.__sex = sex_string
        self.bmi_cat.set_sex(sex_string)

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

    def set_body_type(self, body_type: Literal['s', 'M' ,'L']) -> None:
        """ Set new body type
        :param body_type: new body type as 's', 'M' or 'L'; 's' for small, 'M' for medium, 'L' for large
        """
        if body_type not in ['s', 'M', 'L']:
            raise BodyTypeError(f"The body type: {body_type} is not right. Please use 's', 'M' or 'L'")
        self.body_type = body_type

    def get_ideal_weight(self) -> float:
        """
        calculate ideal weight using the Creff formula
        :return: ideal weight in kg
        """
        if self.__age is None or self.__age < 0:
            raise AgeDiscriminationError("Ideal weight is not available for this age")
        if self.__size is None or self.__size < 0:
            raise SizeError("Ideal weight is not available for this size")
        body_type_multiplier = 1
        if self.body_type == 's':
            body_type_multiplier = 0.9
        elif self.body_type == 'L':
            body_type_multiplier = 1.1
        return round(float((((self.__size - 1) * 100) + (self.__age / 10)) * 0.9 * body_type_multiplier), 1)


if __name__ == '__main__':
    bmi = BmiCalc()
    bmi.set_age(-25)