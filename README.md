
### Bank Churn Prediction

This project is a web application that predicts whether a bank customer is likely to churn using Machine Learning models. The application allows users to input various customer-related features and select a prediction model (SVC or Logistic Regression) to get the prediction.

## Project Structure

- `app.py`: The main Flask application file.
- `templates/`: Contains HTML templates for the web pages.
  - `index.html`: The form for user input.
  - `result.html`: Displays the prediction result.
- `static/`: Contains static files such as images and CSS.
  - `custom_bg.jpg`: The custom background image.
- `svc_model1.pkl`: The serialized SVC model.
- `logistic_model.pkl`: The serialized Logistic Regression model.

## Setup Instructions

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/bank-churn-prediction.git
    cd bank-churn-prediction
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Flask application:**

    ```bash
    python app.py
    ```

5. **Open your browser and navigate to:**

    ```
    http://127.0.0.1:5000/
    ```

## Usage

1. **Open the application in your browser.**
2. **Select the prediction model (SVC Model or Logistic Model).**
3. **Input the required customer-related features.**
4. **Click on the "Predict" button.**
5. **View the prediction result on the result page.**
6. **Use the "Go Back" button to return to the input form.**

## Project Files

### `app.py`

This file contains the Flask application that handles the routes and prediction logic. It loads the pre-trained models and processes the user input to make predictions.

### `templates/index.html`

This HTML file provides the form for users to input customer-related features and select the prediction model.

### `templates/result.html`

This HTML file displays the prediction result and includes a "Go Back" button to return to the input form.

### `static/custom_bg.jpg`

This is the custom background image used in the web application.

## Models

### `svc_model1.pkl`

This file contains the serialized SVC (Support Vector Classifier) model used for prediction.

### `logistic_model.pkl`

This file contains the serialized Logistic Regression model used for prediction.

## Dependencies

The project dependencies are listed in the `requirements.txt` file. Install them using:

```bash
pip install -r requirements.txt
```

## License

This project is licensed under the MIT License. See the LICENSE file for more information.

## Acknowledgements

- This project was created with the help of Flask, a lightweight WSGI web application framework in Python.
- Special thanks to all contributors and the open-source community for their invaluable support and resources.