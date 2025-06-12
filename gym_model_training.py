import pandas as pd
import random
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib

# -----------------------------
# 1. Define Weekly Plans
# -----------------------------
# Weekly exercises for two goals: Muscle Gain and Fat Loss
weekly_exercises = {
    "Muscle Gain": {
        "Monday": "Chest (Bench Press 4x10, Dumbbell Fly 3x12)",
        "Tuesday": "Back (Deadlifts 4x8, Lat Pulldown 3x12)",
        "Wednesday": "Legs (Squats 4x10, Leg Press 3x12)",
        "Thursday": "Arms (Biceps Curl 4x12, Triceps Dips 3x12)",
        "Friday": "Shoulders (Overhead Press 4x10, Lateral Raises 3x12)",
        "Saturday": "Cardio (30 min Running)",
        "Sunday": "Rest"
    },
    "Fat Loss": {
        "Monday": "HIIT (Jump Squats, Burpees, Mountain Climbers - 30 min)",
        "Tuesday": "Full Body Strength (Squats, Push-ups, Plank - 3x15)",
        "Wednesday": "Cardio (Treadmill 40 min)",
        "Thursday": "Core (Abs Crunches, Russian Twists - 4x20)",
        "Friday": "Legs (Lunges, Deadlifts, Step-ups - 3x12)",
        "Saturday": "Cardio (Cycling 30 min)",
        "Sunday": "Rest"
    }
}

# Weekly diet plan for two diet types: Vegetarian and Non-Vegetarian
weekly_diet = {
    "Vegetarian": {
        "Monday": {
            "Breakfast": "Oats + Banana + Peanut Butter (50g + 1 banana + 1 tbsp)",
            "Lunch": "Brown Rice + Dal + Paneer (150g + 100g + 50g)",
            "Dinner": "Roti + Vegetable Curry + Curd (2 roti + 200g curry + 100g curd)"
        },
        "Tuesday": {
            "Breakfast": "Daliya + Nuts (50g + 20g)",
            "Lunch": "Chickpeas + Rice + Salad (100g + 150g + 100g)",
            "Dinner": "Quinoa + Stir-Fried Vegetables (150g + 200g)"
        },
        "Wednesday": {
            "Breakfast": "Poha + Curd (100g + 100g)",
            "Lunch": "Rajma + Rice + Salad (150g + 150g + 100g)",
            "Dinner": "Vegetable Pulao + Raita (200g + 100g)"
        },
        "Thursday": {
            "Breakfast": "Besan Chilla + Green Chutney (2 pieces + 50g chutney)",
            "Lunch": "Mixed Dal + Roti + Salad (150g + 2 roti + 100g)",
            "Dinner": "Stuffed Capsicum + Roti (2 capsicum + 2 roti)"
        },
        "Friday": {
            "Breakfast": "Sprouts Salad + Lemon Juice (100g + 1 tbsp)",
            "Lunch": "Bhindi + Dal + Rice (150g + 100g + 150g)",
            "Dinner": "Khichdi + Curd (200g + 100g)"
        },
        "Saturday": {
            "Breakfast": "Upma + Coconut Chutney (150g + 50g)",
            "Lunch": "Soya Chunks + Rice (100g + 150g)",
            "Dinner": "Paneer Bhurji + Roti (150g + 2 roti)"
        },
        "Sunday": {
            "Breakfast": "Idli + Sambar (3 idli + 150ml sambar)",
            "Lunch": "Chole + Rice + Salad (150g + 150g + 100g)",
            "Dinner": "Dal Khichdi + Curd (200g + 100g)"
        }
    },
    "Non-Vegetarian": {
        "Monday": {
            "Breakfast": "Boiled Eggs + Brown Bread + Peanut Butter (3 eggs + 2 slices + 1 tbsp)",
            "Lunch": "Grilled Chicken + Brown Rice + Salad (150g + 150g + 100g)",
            "Dinner": "Chapati + Fish Curry + Vegetables (2 roti + 150g fish + 200g veggies)"
        },
        "Tuesday": {
            "Breakfast": "Omelette + Whole Wheat Toast (3 eggs + 2 slices)",
            "Lunch": "Grilled Salmon + Quinoa + Salad (150g + 150g + 100g)",
            "Dinner": "Chicken Soup + Brown Bread (1 bowl + 2 slices)"
        },
        "Wednesday": {
            "Breakfast": "Scrambled Eggs + Avocado Toast (3 eggs + 1 slice + 50g avocado)",
            "Lunch": "Mutton Curry + Roti + Salad (150g + 2 roti + 100g)",
            "Dinner": "Grilled Prawns + Stir-Fried Vegetables (150g + 200g)"
        },
        "Thursday": {
            "Breakfast": "Chicken Sausage + Scrambled Eggs (100g + 3 eggs)",
            "Lunch": "Tandoori Chicken + Rice + Salad (150g + 150g + 100g)",
            "Dinner": "Fish Tikka + Quinoa (150g + 150g)"
        },
        "Friday": {
            "Breakfast": "Chicken Sandwich + Green Tea (2 slices + 100g chicken)",
            "Lunch": "Egg Curry + Rice (2 eggs + 150g rice)",
            "Dinner": "Grilled Lamb Chops + Vegetables (150g + 200g)"
        },
        "Saturday": {
            "Breakfast": "Egg Bhurji + Whole Wheat Toast (3 eggs + 2 slices)",
            "Lunch": "Fish Curry + Rice + Salad (150g + 150g + 100g)",
            "Dinner": "Grilled Chicken + Sweet Potatoes (150g + 150g)"
        },
        "Sunday": {
            "Breakfast": "Chicken Omelette + Green Tea (3 eggs + 100g chicken)",
            "Lunch": "Mutton Biryani + Raita (200g + 100g)",
            "Dinner": "Grilled Fish + Quinoa (150g + 150g)"
        }
    }
}

# -----------------------------
# 2. Generate Enhanced Dummy Data
# -----------------------------
data = []
for _ in range(1000):  # Create 1000 samples
    age = random.randint(18, 50)
    weight = random.randint(50, 100)
    goal = random.choice(["Muscle Gain", "Fat Loss"])
    fitness_level = random.choice(["Beginner", "Intermediate", "Advanced"])
    diet_type = random.choice(["Vegetarian", "Non-Vegetarian"])
    
    # Choose the corresponding weekly plans based on goal and diet
    exercise_plan = weekly_exercises[goal]
    diet_plan = weekly_diet[diet_type]
    
    data.append([age, weight, goal, fitness_level, diet_type, exercise_plan, diet_plan])

df = pd.DataFrame(data, columns=["Age", "Weight", "Goal", "Fitness_Level", "Diet_Type", "Exercise_Plan", "Diet_Plan"])

# Save the dataset (optional)
df.to_csv("weekly_fitness_data.csv", index=False)

# -----------------------------
# 3. Encode Categorical Features for Model Training
# -----------------------------
# Encode the input features (Goal, Fitness_Level, Diet_Type)
general_label_encoders = {}
for col in ["Goal", "Fitness_Level", "Diet_Type"]:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    general_label_encoders[col] = le

# Features: Age, Weight, Goal, Fitness_Level, Diet_Type
X = df[["Age", "Weight", "Goal", "Fitness_Level", "Diet_Type"]]

# For the targets, we need to predict the weekly plans (as strings).
# We convert the dictionary to string for encoding.
exercise_labels = df["Exercise_Plan"].apply(lambda x: str(x))
diet_labels = df["Diet_Plan"].apply(lambda x: str(x))

le_exercise = LabelEncoder()
y_exercise = le_exercise.fit_transform(exercise_labels)

le_diet = LabelEncoder()
y_diet = le_diet.fit_transform(diet_labels)

# -----------------------------
# 4. Train the Models
# -----------------------------
# We perform a train-test split (here using 80% for training)
X_train, X_test, y_ex_train, y_ex_test = train_test_split(X, y_exercise, test_size=0.2, random_state=42)
X_train, X_test, y_diet_train, y_diet_test = train_test_split(X, y_diet, test_size=0.2, random_state=42)

# Train a RandomForestClassifier for both tasks
exercise_model = RandomForestClassifier()
exercise_model.fit(X_train, y_ex_train)

diet_model = RandomForestClassifier()
diet_model.fit(X_train, y_diet_train)

# -----------------------------
# 5. Save Trained Models and Encoders
# -----------------------------
joblib.dump(exercise_model, "weekly_exercise_model.pkl")
joblib.dump(diet_model, "weekly_diet_model.pkl")
joblib.dump(le_exercise, "le_exercise.pkl")
joblib.dump(le_diet, "le_diet.pkl")
joblib.dump(general_label_encoders, "general_label_encoders.pkl")

print("Training complete and models saved!")