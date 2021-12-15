# Creating a confusion matrix from the Seroja dataset

# Creating the confusion matrix
# Source: https://machinelearningmastery.com/confusion-matrix-machine-learning/
from sklearn.metrics import confusion_matrix
import pandas as pd

df_confm = pd.read_csv('Seroja Method 2.csv')
results = confusion_matrix(df_confm['Expected'],df_confm['Predicted'])
# print(results)

# Creating plot
# Source: https://stackoverflow.com/questions/35572000/how-can-i-plot-a-confusion-matrix
import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt

df_cm = pd.DataFrame(results, index = [i for i in "0123"],
                  columns = [i for i in "0123"])
plt.figure(figsize = (10,7))
sn.heatmap(df_cm, annot=True)
plt.xlabel("Predicted Number of Locations")
plt.ylabel("Expected Number of Locations")
plt.savefig("Seroja Confusion Matrix Method 2")
plt.show()
