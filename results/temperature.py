import openai
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import time

# get API_key
with open("APIkey.txt", "r") as f:
    openai.api_key = f.read().strip()
  # Replace with your OpenAI API key

prompt = "Solve the equation 2x^2 + 4x - 3 = 0."

def generate_response(prompt, temperature):
    send_to_gpt = []
    send_to_gpt.append({"role": "user",
                    "content": f"{prompt}"})
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',  # Replace with the desired GPT model
        temperature=temperature,
        messages = send_to_gpt
    )
    return response["choices"][0]["message"]["content"]
    

# List of temperature values in the range 0 to 1.0
temperatures = np.arange(0.0, 2.02, 0.02)
df = pd.DataFrame({'Temperature': np.array(temperatures.round(2))})
responses = []
for temp in temperatures:
    try: 
        response = generate_response(prompt, temp)
    except Exception as e:
        time.sleep(5)
        response = np.nan
        print(e, "retrying in 5 seconds")
    responses.append(response)
    if temp % .5 == 0:
        print(f"Temperature: {temp}, Response: {response}")
df[prompt] = responses


# Analyze the similarity of the responses
def jaccard_similarity(str1, str2):
    a = set(str1.split())
    b = set(str(str2).split())
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c) + 1e-10)

df[prompt] = df[prompt].astype(str)
base_sentence = str(df[prompt].iloc[0])

# Calculate the Jaccard similarity of each response to the prompt
df["Similarity"] = df[prompt].apply(lambda x: jaccard_similarity(base_sentence, x))

# Save the responses to a CSV file
filename = prompt + ".csv"
df.to_csv("prompt_2.csv", index=False)

# Plot the similarity of each response to the prompt
plt.scatter(df.Temperature, df.Similarity)
plt.show()

# Compute the impact of temperature on similarity, by OLS regression
x = df.Temperature
y = df.Similarity
X = sm.add_constant(x)
model = sm.OLS(y, X)
results = model.fit()
print(results.summary())