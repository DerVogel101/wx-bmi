# BMI Calculator
This project implements a simple BMI calculator according to [these specifications](https://github.com/DerVogel101/wx-bmi/blob/master/other/task_BMI_Total_py.html).

As an additional gimmick, we implemented a feature that offers the user (given an OpenAI API key is provided) recommendations for improving their health and BMI score.

We Provide a non AI version of the app that can be run without an API key, in a diffrent [branch](https://github.com/DerVogel101/wx-bmi/tree/no_ai).

### Documentation
The project is documented using docstrings and comments.
The documentation can be viewed in the sphinx generated `./docs/build/html/index.html` file.
At `./uml` you can find the UML diagrams for the project.

### Installation
1. Clone this repository and step into the project's root.
2. Create a new virtual environment: `python -m venv .venv`.
3. Activate the virtual environment and install the requirements: `pip install -r requirements.txt`.
4. Start the app with `python main.py`.

### Additional Notes
Small UI changes were made from the original proposed [wireframe](https://github.com/DerVogel101/wx-bmi/blob/master/other/wireframe.png) to guarantee the best possible user experience. The AI feature was first conceived during development, so it was not included in the initial wireframe.

The vertical layout proposed in the wireframe was discarded during the testing of the application because we felt it unnecessary and irritating to introduce such a significant layout change for a small application that is only meant to be run on horizontal desktop screens. 
