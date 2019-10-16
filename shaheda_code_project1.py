#shaheda choudhury code for the project and her assigned questions 

# Dependencies and Setup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# File to Load 
border_data_to_load = "Border_Crossing_Entry_Data.csv"

# Read the Border Corssing Entry Data file and store into a Pandas Data Frame
border_data_df = pd.read_csv(border_data_to_load)

# Confirm full file was loaded
len(border_data_df)

# Preview the data frame
border_data_df.head(5)

# Convert 'Date' from str to datetime format and store in a new field called 'Date_dt'
border_data_df ['Date_dt'] = pd.to_datetime(border_data_df['Date'])
# Preview the data frame
border_data_df.head(5)

#question: What is the total value of border crossings by single person mesures? 

#save the og df to another variable so that I'm not messing it up
sc_df1 = border_data_df
sc_df = sc_df1
#changing the date_df column to just a date on a new data frame
sc_df['Date'] = pd.to_datetime(sc_df1['Date_dt'])
sc_df.head(5)

#converting the DT to seperate year, months, and days
sc_df = pd.DataFrame(sc_df1, columns = ['Port Name', 'State','Measure', 'Value', 'Border'])

#parsing the date to year month and day
sc_df['Year'] = sc_df1['Date_dt'].dt.year
sc_df['Month'] = sc_df1['Date_dt'].dt.month
sc_df['Day'] = sc_df1['Date_dt'].dt.day

#seeing the data frame
sc_df.head()

#list all measures of boarder crossing
sc_df['Measure'].unique()

#the data frame total value
sc_df.shape

#creates a loop to loop the data to see if meets the measures we are looking for. 
booleans = []
for l in sc_df.Measure: 
    if l == 'Personal Vehicle Passengers':
        booleans.append(True)
    elif l == 'Personal Vehicles': 
        booleans.append(True)
    elif l == 'Pedestrians': 
         booleans.append(True)
    else: 
        booleans.append(False)

#test to see if values work 
print(booleans[0:21])
#test to see if it worked on all the rows of data
print(len(booleans))

measures = pd.Series(booleans)
measures.head()

sc_df[measures].head(10)

sc_df[measures].head()

#finding the full total of all the data crossing for each way of transportation
values_gb = sc_df[measures].groupby(['Measure', 'Border'])['Value'].sum()
values_total = values_gb
print(values_total)

#reset the index of the total values and creating a new df for it. 
values_df = values_gb.reset_index()
print(values_df)

#splitting the data so that the US/CAN and US/MEX border are in different data frames. 
us_can_df = values_df [values_df['Border'] == 'US-Canada Border']

us_mex_df = values_df [values_df['Border'] == 'US-Mexico Border']

#printing the US CAN DF to test that it shows properly
print(us_can_df)

#printing the US MEX DF to test that it shows properly
print(us_mex_df)


#creating the bar graph side by side
#y_label = values_df['Value']

label = us_can_df['Measure']
x = np.arange(len(label))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2,us_can_df['Value'], width, label = ' US-Canada' )
rects2 = ax.bar(x + width/2,us_mex_df['Value'], width, label = ' US-Mexico' )

ax.set_ylabel('Values of Crossings')
ax.set_title('USA Inbound Crossing by Measures')
ax.set_xticks(x)
ax.set_xticklabels(label)
ax.legend()

#Labeling the bars with numbers on top of the graph copied,pasted and no changeed done:from matplotlib official documentations
def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
autolabel(rects1)
autolabel(rects2)
fig.tight_layout()
plt.show()

