
# **Thyroid Disease Prediction Using Machine Learning**

---

## **Table of Contents**

1. [Overview](#overview)  
2. [Features](#features)  
3. [Getting Started](#getting-started)  
   - [Prerequisites](#prerequisites)  
   - [Installation Instructions](#installation-instructions)  
4. [How to Run](#how-to-run)  
5. [Results & Discussion](#results--discussion)  
6. [Models & Performance](#models--performance)  
7. [Conclusion](#conclusion)  
8. [Future Scope](#future-scope)  
9. [Contributing](#contributing)  
10. [License](#license)  
11. [References](#references)

---

## **Overview**

This repository contains the implementation of a machine learning-based **Thyroid Disease Prediction System**. The project utilizes classification algorithms (Naive Bayes, SVM, and Random Forest) to predict whether a patient is likely to have thyroid disease using clinical data.  

The system preprocesses the dataset, applies machine learning models, and compares their performance, making it possible to predict thyroid disease at an early stage using minimal resources.

---

## **Features**

 Predicts thyroid diseases using machine learning classification models.  
 Preprocesses raw data by encoding non-numeric entries into numeric ones.  
 Compares model performance (Naive Bayes, SVM, Random Forest).  
 Trains the model with 80% of the dataset and tests on 20%.  
 Displays results graphically for intuitive analysis.  
 Predicts the presence of thyroid disease using uploaded test data.

---

## **Getting Started**

Follow the steps below to set up and run the project.

---

### **Prerequisites**

Before you get started, ensure you have the following:

- **Python** (>=3.6) installed on your local machine.
- Required Python libraries. Use the `requirements.txt` file to install these.

---

### **Installation Instructions**

Clone the repository and set up the environment:

```bash
# Clone the repository
git clone https://github.com/your-username/thyroid-disease-prediction.git
cd thyroid-disease-prediction

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate  # For Windows

# Install required dependencies
pip install -r requirements.txt
```

---

## **How to Run**

Once the environment is set up:

1. **Run the `run.bat` file** to initialize the GUI interface (Windows only).  
   - Navigate to the directory containing `run.bat` and execute it.
   
   Or you can execute manually:

   ```bash
   python main.py
   ```

2. The GUI interface will launch. Interact with the buttons as follows:
   - **Upload Thyroid Dataset**: Load the dataset into the system.
   - **Preprocess Dataset**: Converts non-numeric values into numeric values for compatibility.
   - **Run Naïve Bayes Algorithm**: Train and test using Naive Bayes and view prediction metrics.
   - **Run SVM Algorithm**: Train and test using SVM for comparison.
   - **Run Random Forest Algorithm**: Train and test with Random Forest for optimal performance.
   - **Comparison Graph**: Visualize the accuracy comparison of all three algorithms.
   - **Predict Disease from Test Data**: Upload new test data to predict thyroid presence.

---

## **Results & Discussion**

### 1. **Prediction Accuracy with Models**

| Model          | Accuracy |
|----------------|---------|
| Naive Bayes     | 57%     |
| SVM             | 98%     |
| Random Forest   | 99%     |

### 2. **Comparison Graph**
The Random Forest model consistently outperforms the other models in terms of accuracy, precision, and recall.

---

## **Models & Performance**

We tested three classification algorithms:
1. **Naive Bayes**: Achieved 57% accuracy on test data.
2. **Support Vector Machines (SVM)**: Achieved 98% accuracy.
3. **Random Forest**: Achieved the highest accuracy at 99%.

The Random Forest model was chosen as the most accurate and reliable model for predicting thyroid presence.

---

## **Conclusion**

The machine learning model proposed is:
- **Accurate**: Random Forest achieved 99% accuracy.
- **Cost-effective**: Utilizes minimal computing resources for predictions.
- **Fast & Efficient**: Trains and predicts with reduced computational overhead.

The system serves as a practical tool to help detect thyroid diseases early, allowing medical intervention at an early stage.

---

## **Future Scope**

The project can be further enhanced by:
1. Exploring more datasets to generalize findings better.
2. Testing additional machine learning algorithms or ensemble methods.
3. Deploying this system as a web application for easier accessibility.

---

## **Contributing**

We welcome contributions! If you'd like to contribute to this project:

1. Fork this repository.  
2. Create a branch for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Added/Fixed a feature"
   ```
4. Push your changes:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

---

## **License**

This project is licensed under the **MIT License**. For details, see [LICENSE](LICENSE).

---

## **References**

- Bibi Amina Begum, Dr. Parkavi, "Prediction of thyroid Disease Using Data Mining Techniques," ICACCS, 2019.  
- Ankith Tyagi, Ritika Mehra, Aditya Saxena, "Interactive Thyroid Disease Prediction System Using Machine Learning Technique," PDGC-2018.  
- A detailed study on Machine Learning techniques for disease detection from multiple medical journals and online sources.

---

### **Contact**

For any issues, suggestions, or collaboration inquiries, contact me at:  
saikrishnauggi@gmail.com 
