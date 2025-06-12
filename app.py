from flask import Flask, request, render_template
import pandas as pd
import joblib

app = Flask(__name__)

# Load trained models and encoders
exercise_model = joblib.load("weekly_exercise_model.pkl")
diet_model = joblib.load("weekly_diet_model.pkl")
le_exercise = joblib.load("le_exercise.pkl")
le_diet = joblib.load("le_diet.pkl")
general_label_encoders = joblib.load("general_label_encoders.pkl")

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get user input from the form
        age = int(request.form["age"])
        weight = int(request.form["weight"])
        goal = request.form["goal"]
        fitness_level = request.form["fitness_level"]
        diet_type = request.form["diet_type"]
        
        # Encode categorical features using the saved encoders
        goal_enc = general_label_encoders["Goal"].transform([goal])[0]
        fitness_level_enc = general_label_encoders["Fitness_Level"].transform([fitness_level])[0]
        diet_type_enc = general_label_encoders["Diet_Type"].transform([diet_type])[0]
        
        # Prepare input for prediction
        input_data = [[age, weight, goal_enc, fitness_level_enc, diet_type_enc]]
        
        # Predict weekly exercise and diet plans
        ex_pred = exercise_model.predict(input_data)[0]
        dt_pred = diet_model.predict(input_data)[0]
        
        # Decode predictions back to readable string (dictionary string)
        exercise_plan_str = le_exercise.inverse_transform([ex_pred])[0]
        diet_plan_str = le_diet.inverse_transform([dt_pred])[0]
        
        # Evaluate string back to dictionary (using eval, note: in production, use a safer alternative)
        exercise_plan = eval(exercise_plan_str)
        diet_plan = eval(diet_plan_str)
        
        return render_template("result.html", 
                               age=age, weight=weight, goal=goal, fitness_level=fitness_level, diet_type=diet_type,
                               exercise_plan=exercise_plan, diet_plan=diet_plan)
    return render_template("index.html")

if __name__== '__main__':
    app.run(debug=True)