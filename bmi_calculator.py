from typing import Optional, Literal


class BmiCatSimple:
    """
    A class to categorize BMI values into predefined categories.

    Attributes:
        categories (tuple): A tuple of BMI categories and their corresponding ranges.
    """
    def __init__(self):
        """
        Initializes the BmiCatSimple class with predefined BMI categories.
        """
        self.categories = (
            ("Untergewicht", (None, 18.5)),
            ("Normalgewicht", (18.5, 24.9)),
            ("Übergewicht", (25, 29.9)),
            ("Starkes Übergewicht (Adipositas Grad I)", (30, 34.9)),
            ("Adipositas Grad II", (35, 39.9)),
            ("Adipositas Grad III", (40, None))
        )

    def __getitem__(self, item: float) -> str:
        """
        Gets the BMI category for a given BMI value.

        Args:
            item (float): The BMI value.

        Returns:
            str: The category corresponding to the BMI value.
        """
        for cat, (lower, upper) in self.categories:
            if lower is None and item < upper:
                return cat
            if upper is None and item >= lower:
                return cat
            if lower is not None and upper is not None and lower <= item < upper:
                return cat
        return "Unbekannt"

class BmiAgeSex(BmiCatSimple):
    """
    A class to categorize BMI values into predefined categories based on age and sex.

    Inherits from:
        BmiCatSimple: The base class for BMI categorization.

    Attributes:
        sex_offset (float): The offset value based on sex.
        age (int | None): The age of the individual.
        categories_male (tuple): The BMI categories for males.
        categories_female (tuple): The BMI categories for females.
        selected_categories (tuple): The currently selected BMI categories.
    """
    def __init__(self):
        """
        Initializes the BmiAgeSex class with predefined BMI categories for males and females.
        """
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
        """
        Sets the sex and updates the selected BMI categories and sex offset.

        Args:
            sex (str | None): The sex of the individual ('m' for male, 'f' for female, or None).
        """
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
        """
        Sets the age of the individual.

        Args:
            age (int | None): The age of the individual.
        """
        self.age = age

    def __getitem__(self, item) -> tuple[str, float | None]:
        """
        Gets the BMI category and ideal BMI for a given BMI value.

        Args:
            item (float): The BMI value.

        Returns:
            tuple[str, float | None]: The category and ideal BMI corresponding to the BMI value.
        """
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
    """
    Base class for exceptions in the BMI module.
    """
    pass

class SexError(BmiError):
    """
    Exception raised for errors in the sex attribute.
    """
    pass

class AgeDiscriminationError(BmiError):
    """
    Exception raised for invalid age values.
    """
    pass

class SizeError(BmiError):
    """
    Exception raised for errors in the size attribute.
    """
    pass

class WeightError(BmiError):
    """
    Exception raised for errors in the weight attribute.
    """
    pass

class BodyTypeError(BmiError):
    """
    Exception raised for errors in the body type attribute.
    """
    pass

class BmiCalc:
    """
    A class to calculate BMI and categorize it based on age, sex, and body type.

    Attributes:
        body_type (str | None): The body type of the individual.
        __age (int | None): The age of the individual.
        __weight (float | None): The weight of the individual in kg.
        __sex (str | None): The sex of the individual.
        __size (float | None): The height of the individual in meters.
        bmi_cat (BmiAgeSex): An instance of the BmiAgeSex class for BMI categorization.
    """
    def __init__(self):
        """
        Initializes the BmiCalc class with default values.
        """
        self.body_type = None
        self.__age = None
        self.__weight = None
        self.__sex = None
        self.__size = None
        self.bmi_cat = BmiAgeSex()

    def get_bmi(self) -> float:
        """
        Calculates and returns the current BMI.

        Returns:
            float: The current BMI.

        Raises:
            SizeError: If the size is not set.
            WeightError: If the weight is not set.
        """
        if self.__size is None:
            raise SizeError("Size is not set. Please set a size in meters")
        if self.__weight is None:
            raise WeightError("Weight is not set. Please set a weight in kg")
        return round(self.__weight / (self.__size ** 2), 2)

    def get_category(self) -> str:
        """
        Returns the current weight category as a string.

        Returns:
            str: The current weight category.
        """
        return self.bmi_cat[self.get_bmi()][0]

    def get_age(self) -> int | None:
        """
        Gets the current age.

        Returns:
            int | None: The current age.
        """
        return self.__age

    def set_age(self, age: Optional[int]) -> None:
        """
        Sets a new age or resets the age.

        Args:
            age (Optional[int]): The new age or None to reset.

        Raises:
            AgeDiscriminationError: If the age is not a valid positive number.
        """
        if age is not None and age < 0:
            raise AgeDiscriminationError(f"The age: {age} is not a valid age. Please use a positive number or None")

        self.__age = age
        self.bmi_cat.set_age(age)

    def get_sex(self) -> str | None:
        """
        Gets the current sex as 'm', 'f', or None.

        Returns:
            str | None: The current sex.
        """
        return self.__sex

    def set_sex(self, sex_string: Optional[Literal['m', 'f']]) -> None:
        """
        Sets a new sex or resets the sex.

        Args:
            sex_string (Optional[Literal['m', 'f']]): The new sex as 'm', 'f', or None.

        Raises:
            SexError: If the sex is not 'm', 'f', or None.
        """
        if sex_string not in ['m', 'f', None]:
            raise SexError(f"The sex: {sex_string} is not right. Please use 'm' or 'f' or None")
        self.__sex = sex_string
        self.bmi_cat.set_sex(sex_string)

    def get_size(self) -> float:
        """
        Gets the current size in meters.

        Returns:
            float: The current size in meters.

        Raises:
            SizeError: If the size is not set.
        """
        if self.__size is None:
            raise SizeError("Size is not set. Please set a size in meters")
        return self.__size

    def set_size(self, size: float) -> None:
        """
        Sets a new size in meters.

        Args:
            size (float): The new size.

        Raises:
            SizeError: If the size is not a valid positive float number.
        """
        if size < 0 or not isinstance(size, (int, float)):
            raise SizeError(f"The size: {size} is not a valid size. Please use a positive float number")
        self.__size = size

    def get_weight(self) -> float:
        """
        Gets the current weight in kg.

        Returns:
            float: The current weight in kg.

        Raises:
            WeightError: If the weight is not set.
        """
        if self.__weight is None:
            raise WeightError("Weight is not set. Please set a weight in kg")
        return float(self.__weight)

    def set_weight(self, weight: float) -> None:
        """
        Sets a new weight in kg.

        Args:
            weight (float): The new weight.

        Raises:
            WeightError: If the weight is not a valid positive float number.
        """
        if weight < 0 or not isinstance(weight, (int, float)):
            raise WeightError(f"The weight: {weight} is not a valid weight. Please use a positive float number")
        self.__weight = weight

    def set_body_type(self, body_type: Literal['s', 'M' ,'L']) -> None:
        """
        Sets a new body type.

        Args:
            body_type (Literal['s', 'M', 'L']): The new body type as 's', 'M', or 'L'.

        Raises:
            BodyTypeError: If the body type is not 's', 'M', or 'L'.
        """
        if body_type not in ['s', 'M', 'L']:
            raise BodyTypeError(f"The body type: {body_type} is not right. Please use 's', 'M' or 'L'")
        self.body_type = body_type

    def get_ideal_weight(self) -> float:
        """
        Calculates and returns the ideal weight using the Creff formula.

        Returns:
            float: The ideal weight in kg.

        Raises:
            AgeDiscriminationError: If the age is not set or is invalid.
            SizeError: If the size is not set or is invalid.
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
