# BMI Calculator
This project implements a simple BMI calculator according to [these specifications](https://github.com/DerVogel101/wx-bmi/blob/master/other/task_BMI_Total_py.html).

As an additional gimmick, under the [Main branch](https://github.com/DerVogel101/wx-bmi/), a feature was implemented that offers the user (given an OpenAI API key is provided) recommendations for improving their health and BMI score.

### Installation
1. Clone this repository and step into the project's root.
2. Create a new virtual environment: `python -m venv .venv`.
3. Activate the virtual environment and install the requirements: `pip install -r requirements.txt`.
4. Start the app with `python main.py`.

### Additional Notes
Small UI changes were made from the original proposed [wireframe](https://github.com/DerVogel101/wx-bmi/blob/master/other/wireframe.png) to guarantee the best possible user experience. The AI feature was first conceived during development, so it was not included in the initial wireframe.

The vertical layout proposed in the wireframe was discarded during the testing of the application because we felt it unnecessary and irritating to introduce such a significant layout change for a small application that is only meant to be run on horizontal desktop screens. 
