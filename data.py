import random
import pandas as pd

# Lists of therapy types and disorders
therapies = ["CBT", "DBT", "Exposure Therapy", "Family Therapy", "Interpersonal Therapy"]
disorders = ["PTSD", "Depression", "Self-Harm", "Anxiety", "Substance Abuse"]

# Create an empty DataFrame
data = []

# Generate 1000 records
for _ in range(1000):
    person = f"Person {_ + 1}"
    therapy = random.choice(therapies)  # Random therapy type
    disorder = random.choice(disorders)  # Random disorder
    features = [random.choice(["Yes", "No"]) for _ in range(8)]  # Random features
    data.append([person, therapy, disorder] + features)

# Create the DataFrame
df = pd.DataFrame(data, columns=["Person", "Therapy", "Disorder"] + [
    "Self-harm thoughts", "Post-traumatic disorder", "Communication problems",
    "Relationship problems", "Alcohol", "Nightmare", "Dental issues", "Hair loss"
])

# Save the DataFrame to a CSV file
df.to_csv("synthetic_dataset.csv", index=False)

