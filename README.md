# 🏠 House Price Prediction using Linear Regression

## 🚀 Overview
This project builds a **Linear Regression model** to predict house prices based on various housing features.  
The model uses **log transformation** to improve performance and achieve better accuracy.

---

## 🎯 Objective
- Predict house prices accurately 📈  
- Improve model performance using transformations  
- Achieve a balance between simplicity and effectiveness  

---

## 🧰 Tech Stack
- Python 🐍  
- Pandas 📊  
- NumPy 🔢  
- Scikit-learn 🤖  

---

## 📂 Dataset
The dataset contains housing-related features such as:
- Property size  
- Number of rooms  
- Other structural attributes  

Basic preprocessing was performed by removing unnecessary columns.

---

## 🧹 Data Preprocessing
- Removed irrelevant columns (`id`, `date`)  
- Split dataset into:
  - Features (`X`)  
  - Target (`price`)  

---

## 🔄 Key Technique: Log Transformation

To improve model performance:

- Applied **log transformation** on the target variable  
- This helps:
  - Reduce skewness  
  - Handle large value variations  
  - Improve linear model performance  

---

## 🤖 Model Used
### Linear Regression
- Simple and interpretable model  
- Assumes linear relationships between features and target  
- Fast and efficient  

---

## 🔀 Train-Test Split
- 80% Training Data  
- 20% Testing Data  
- Random state used for reproducibility  

---

## 📊 Model Performance

| Metric | Value |
|--------|------|
| 📉 Mean Squared Error (Log Scale) | **0.0653** |
| 📈 R² Score (Log Scale) | **0.7710** |

---

## 📈 Interpretation

### ✅ R² Score ≈ 0.77
- The model explains **77% of the variance** in house prices  
- Good performance for a linear model  

### ✅ MSE ≈ 0.065 (Log Scale)
- Indicates low prediction error  
- Shows stable model performance  

---

## ⚡ Performance Summary

- ⚡ Fast training  
- 📈 Good accuracy for Linear Regression  
- 📉 Reduced error using log transformation  
- 🔄 Stable predictions

---

## 🧠 Key Learnings
- Log transformation significantly improves regression performance  
- Linear Regression has limitations with complex data  
- Feature selection and preprocessing are crucial  

---

## 🙌 Author
**Tanishq Panchal**

---

## ⭐ Support
If you found this project helpful, consider giving it a ⭐ on GitHub!
