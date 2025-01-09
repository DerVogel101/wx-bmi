from openai.types.chat import ChatCompletionMessage
from openai import OpenAI
from pprint import pprint

class AiLib:
    """
    Library class for handling AI-related functionalities.

    Attributes:
        __client (OpenAI): The OpenAI client for making API requests.
        __model (str): The model name to be used for generating responses.
        weigth (str): The weight of the user.
        height (str): The height of the user.
        age (str): The age of the user.
        sex (str): The sex of the user.
        btype (str): The body type of the user.
        bmi_score (str): The BMI score of the user.
        bmi_cat (str): The BMI category of the user.
        craff_score (str): The Craff ideal weight score of the user.
        personallity (str): The personality description for the AI response.
        __messages (list): The list of messages to be sent to the AI model.
    """
    def __init__(self):
        """
        Initializes the AiLib class with default values.
        """
        self.__client = OpenAI(api_key="")
        self.__model = "gpt-4o-mini"

        self.weigth = "-Leer-"
        self.height = "-Leer-"
        self.age = "-Leer-"
        self.sex = "-Leer-"
        self.btype = "-Leer-"

        self.bmi_score = "-Leer-"
        self.bmi_cat = "-Leer-"
        self.craff_score = "-Leer-"

        self.personallity = "als wärst du ein Fitness Influenza"

        self.__messages = None

    def set_api_key(self, api_key: str):
        """
        Sets the API key for the OpenAI client.

        Args:
            api_key (str): The API key to be set.
        """
        self.__client.api_key = api_key

    def assemble_messages(self) -> None:
        """
        Assembles the messages to be sent to the AI model.
        """
        self.__messages = [
            {"role": "system", "content": f"Du bist ein Assistenz Programm welches einmalig einen Tipp zu der eingabe Generieren soll, achte auf unrealistische eingaben und sprich der Person gut zu, schreibe die Antwort {self.personallity}. Antworte im HTML Format, benutze kein code markdown, nur raw, formatiere deinen HTML Sourcecode mit css."},
            {"role": "user", "content": f"----Körperwerte----\n"
                                        f"Alter: {self.age} Jahre\n"
                                        f"Geschlecht: {self.sex}\n"
                                        f"Körpertyp: {self.btype}\n"
                                        f"Größe: {self.height} cm\n"
                                        f"Gewicht: {self.weigth} kg\n"
                                        f"----Ergebnisse----\n"
                                        f"BMI: {self.bmi_score}\n"
                                        f"Craff Idealgewicht: {self.craff_score}\n"
                                        f"BMI Kategorie: {self.bmi_cat}\n"
                                        f"----Ende----"}
        ]

    def get_response(self) -> ChatCompletionMessage:
        """
        Gets the response from the AI model based on the assembled messages.

        Returns:
            ChatCompletionMessage: The response message from the AI model.
        """
        completion = self.__client.chat.completions.create(
            model=self.__model,
            messages=self.__messages
        )
        return completion.choices[0].message

