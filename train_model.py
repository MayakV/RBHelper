import os
import openai
import pandas as pd

openai.api_key = os.getenv("RBH_OpenAI_Token")
model_engine = "ada"
model = openai.Model(engine=model_engine)

data = pd.read_json("dataset.jsonl")

# Create a training set by selecting a subset of the data
train_data = data.sample(frac=0.8, random_state=123)

# Create a test set using the remaining data
test_data = data.drop(train_data.index)

# Convert the training set into a list of strings
train_strings = train_data["text"].tolist()

# Fine-tune the model on the training set
model.finetune(train_strings)

# Test the model on the test set
test_strings = test_data["text"].tolist()
results = model.generate(test_strings)

# validation
# gives tips on how to improve dataset
# - openai tools fine_tunes.prepare_data -f dataset.jsonl -q

# train new model
# - openai api fine_tunes.create -t dataset.jsonl -m davinci --suffix "<YOUR_MODEL_NAME>"