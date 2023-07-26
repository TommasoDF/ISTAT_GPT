import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
import numpy as np

fontsize= 14
ticksize = 14
figsize = (12, 9)
params = {'font.family':'serif',
    "figure.figsize":figsize, 
    'figure.dpi': 80,
    'figure.edgecolor': 'k',
    'font.size': fontsize, 
    'axes.labelsize': fontsize,
    'axes.titlesize': fontsize,
    'xtick.labelsize': ticksize,
    'ytick.labelsize': ticksize
}
plt.rcParams.update(params) 

#Set a color for scatter points and one for the line
abs_1 = np.array([60, 9, 108])/255
abs_2 = np.array([36, 0, 70])/255
abs_3 = np.array([218, 44, 56])/255
correct_color = (abs_1[0], abs_1[1], abs_1[2])
incorrect_color = (abs_3[0], abs_3[1], abs_3[2])
line_color = (abs_2[0], abs_2[1], abs_2[2])
scatter_colors = [incorrect_color, correct_color]

# df1 = pd.read_csv("Explain in three lines how ChatGPT can help individuals to obtain information.csv") 
# df2 = pd.read_csv("prompt_2_reduced.csv")
# df3 = pd.read_csv("prompt_3.csv")

# # Extract the two columns from each DataFrame
# column1_data = pd.concat([df1['Temperature'], df2['Temperature'], df3['Temperature']], ignore_index=True)
# column2_data = pd.concat([df1['Similarity'], df2['Similarity'], df3['Similarity']], ignore_index=True)

# Create the new DataFrame with the extracted columns
df = pd.read_csv("prompt_3.csv")
#df = pd.DataFrame({'Temperature': column1_data, 'Similarity': column2_data})
df = df.dropna()
# Compute the impact of temperature on similarity, by OLS regression
x = df.Temperature
y = df.Similarity
X = sm.add_constant(x)
model = sm.OLS(y, X)
results = model.fit()
print(results.summary())

#Plot a scatterplot and the best line
fig, ax = plt.subplots()
ax.set_xlabel("Temperature")
ax.set_ylabel("Similarity")
#Scatter with different colors, based on the column "Correct"
#point_colors = [scatter_colors[int(val)] for val in df['Correct']]
ax.scatter(df.Temperature, df.Similarity, c= correct_color, label = "Actual", alpha = 0.9)
#make legend for the two colors
#ax.scatter([], [], c= incorrect_color, label = 'Incorrect', alpha = 0.9)
#ax.scatter([], [], c= correct_color, label = 'Correct', alpha = 0.9)

#plot the best line given by OLS results
ax.plot(df.Temperature, results.fittedvalues, '--', color = line_color, label="Fitted")
ax.legend()
#save the picture
#fig.savefig("total.png")