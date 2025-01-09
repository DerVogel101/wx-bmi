from openai.types.chat import ChatCompletionMessage
from openai import OpenAI
from pprint import pprint
# client = OpenAI()
#
# completion = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {
#             "role": "user",
#             "content": "Write a haiku about recursion in programming."
#         }
#     ]
# )
#
# print(completion.choices[0].message)

class AiLib:
    def __init__(self):
        self.__client = OpenAI(api_key="")
        self.__model = "gpt-4o-mini"

        self.weigth = "-Leer-" #
        self.height = "-Leer-" #
        self.age = "-Leer-" #
        self.sex = "-Leer-" #
        self.btype = "-Leer-" #

        self.bmi_score = "-Leer-" #
        self.bmi_cat = "-Leer-" #
        self.craff_score = "-Leer-" #

        self.personallity = "als wärst du ein Fitness Influenza" #

        self.__messages = None

    def set_api_key(self, api_key: str):
        self.__client.api_key = api_key

    def assemble_messages(self) -> None:
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
        completion = self.__client.chat.completions.create(
            model=self.__model,
            messages=self.__messages
        )
        return completion.choices[0].message

