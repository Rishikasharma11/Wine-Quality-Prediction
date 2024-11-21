# Wine Quality Prediction

## **Overview**
This project predicts the quality of wine based on its chemical properties using machine learning models. The dataset includes various features like acidity, sugar content, pH, and alcohol levels, which influence wine quality. The target is to classify wines into two categories:  
- **Good Quality** (quality ≥ 7)  
- **Bad Quality** (quality < 7)

---


## **Usage**
1. **Preprocessing**:  
   - Standardized the dataset using `StandardScaler`.  
   - Converted the quality scores into binary categories.  
2. **Model Training**:  
   - Used classifier:  
     - Random Forest Classifier  
3. **Evaluation**:  
   - Accuracy and confusion matrix were used to assess model performance.  
4. **Prediction**:  
   - The trained model predicts wine quality for custom input data.  

---


## **Technologies Used**
- **Python**: Core language for implementation.  
- **NumPy & Pandas**: For data handling and preprocessing.  
- **Scikit-learn**: For machine learning models and evaluation.  
- **Matplotlib & Seaborn**: For exploratory data analysis (EDA) and visualizations.  
