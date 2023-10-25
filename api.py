from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI()
columns_to_drop = ['Therapy_CBT', 'Therapy_DBT','Therapy_Exposure Therapy','Therapy_Family Therapy', 'Therapy_Interpersonal Therapy']

class request_body(BaseModel):
    Self_harm_thoughts: float
    Post_traumatic_disorder: float
    Communication_problems: float
    Relationship_problems: float
    Alcohol: float
    Nightmare: float
    Dental_issues: float
    Hair_loss: float
    Anxiety: float
    Depression: float
    PTSD: float
    Self_Harm: float
    Substance_Abuse: float
	
	
@app.post('/mottayo')
def mottayo(data : request_body):

    with open ("new.pkl","rb") as f:
        model= pickle.load(f)

    test_data = [[
			data.Self_harm_thoughts,
            data.Post_traumatic_disorder,
            data.Communication_problems,
            data.Relationship_problems,
            data.Alcohol,
            data.Nightmare,
            data.Dental_issues,
            data.Hair_loss,
            data.Anxiety,
            data.Depression,
            data.PTSD,
            data.Self_Harm,
            data.Substance_Abuse
	]]
	
    pred = model.predict(test_data)[0]
	
    
    max_indices = np.argmax(pred)
    return { 'class' : columns_to_drop[max_indices]}