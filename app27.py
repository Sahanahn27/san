{
 "cells": [
  {
   
   "outputs": [],
   "source": [
    "from flask import Flask, request, jsonify, render_template\n",
    "import pickle\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "\n",
    "# Initialize the Flask application\n",
    "app = Flask(__name__)\n",
    "\n",
    "# Load the saved model\n",
    "with open('C:\\Users\\Lenovo\\Documents\\project files\\rf_model.pkl', 'rb') as file:\n",
    "    model = pickle.load(file)\n",
    "\n",
    "# Define the home route\n",
    "@app.route('/')\n",
    "def home():\n",
    "    return render_template('index.html')  # Make sure to create 'index.html' for input\n",
    "\n",
    "# Prediction route\n",
    "@app.route('/predict', methods=['POST'])\n",
    "def predict():\n",
    "    # Retrieve input data from the form\n",
    "    input_data = [float(x) for x in request.form.values()]\n",
    "    features = np.array(input_data).reshape(1, -1)\n",
    "    \n",
    "    # Make prediction\n",
    "    prediction = model.predict(features)\n",
    "    output = 'Churn' if prediction[0] == 1 else 'No Churn'\n",
    "    \n",
    "    # Display the result\n",
    "    return render_template('index.html', prediction_text=f'Customer is likely to: {output}')\n",
    "\n",
    "# Run the app\n",
    "if __name__ == \"__main__\":\n",
    "    app.run(debug=True)\n"
   ]
  },
  {
   
   "id": "bd4864a4-b1c9-4554-baf3-b0c0431e16c7",
   "metadata": {},
   "outputs": [],
   "source": [
    "<!DOCTYPE html>\n",
    "<html lang=\"en\">\n",
    "<head>\n",
    "    <meta charset=\"UTF-8\">\n",
    "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n",
    "    <title>Churn Prediction</title>\n",
    "</head>\n",
    "<body>\n",
    "    <h2>Predict Customer Churn</h2>\n",
    "    <form action=\"/predict\" method=\"post\">\n",
    "        <label>Feature 1:</label>\n",
    "        <input type=\"text\" name=\"feature1\"><br><br>\n",
    "        \n",
    "        <label>Feature 2:</label>\n",
    "        <input type=\"text\" name=\"feature2\"><br><br>\n",
    "        \n",
    "        <!-- Add additional input fields for each feature in your model -->\n",
    "        \n",
    "        <button type=\"submit\">Predict</button>\n",
    "    </form>\n",
    "    <h3>{{ prediction_text }}</h3>\n",
    "</body>\n",
    "</html>\n"
   ]
  }
 ],
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 }

