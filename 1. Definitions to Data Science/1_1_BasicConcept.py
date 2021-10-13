##### INTRO
#To answer these questions, data scientists use a process of experimentation and exploration to find answers. 
#Like other scientific fields, data science follows the scientific method. ]
#But the data science process also includes steps particular to working with large, digital datasets.

#The process generally goes as follows:

#Ask a question
#Determine the necessary data
#Get the data
#Clean and organize the data
#Explore the data
#Model the data
#Communicate your findings

##### VARIABLE RELATIONSHIPS
#In data science, we want to know the effect that different things have on each other. 
#One way of framing a question is to think of the relationship between the different variables,

##### SCOPE
#Another thing to keep in mind while forming a question is scope. 
#A question should be specific enough that we know it is answerable, but it shouldn’t be too specific to the point where no relevant data exist, and we are unable to draw any real conclusions.

##### Determine the Necessary Data
#After you have a question, you have to make an educated guess about what you think the answer might be. This educated guess is known as a hypothesis and helps to determine the data you need to collect.
#It’s important to remember that the data you decide to collect can’t just be the data that you think is going to answer your question
#First, we need to determine what data could disprove our hypothesis.
#Next, we need to figure out how much data to collect.
#Rule of thumb: the larger the sample size and the more diverse your dataset is, the more confident you’ll be in your results. 


###### Getting Data
#Once you’ve determined which data you need, it’s time to collect it!
#Data collection can be as simple as locating a file or as complicated as designing and running an experiment.

#Active data collection—you’re setting up specific conditions in which to get data.
#Passive data collection—you’re looking for data that already exists.

#An important one is the size of our dataset. Remember that we usually can’t get data from an entire population, so we need to have an appropriate sample that is representative of the larger population. If you’re ever unsure about the size of your dataset, use a sample size calculator.
#Another thing to keep in mind is that errors and bias can occur in data collection.



####### Cleaning Data
#Data is typically organized in columns and rows, like you’d see in a spreadsheet. But raw data can actually come in a variety of file types and formats. This is especially true if you’re getting your data from elsewhere, like public datasets.
#An important part of the data science process is to clean and organize our datasets, sometimes referred to as data wrangling.
#The Python library Pandas is a great tool for importing and organizing datasets. 


## Example of pre-processing data
import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import the CSV files and create the DataFrames:
user_data = pd.read_csv("user_data.csv")
pop_data = pd.read_csv("pop_data.csv")

# Check the code by printing it
print(user_data.head(15))

# Paste merge code here:
new_df = pd.merge(user_data, pop_data)
print(new_df.head(15))

# Paste location code here:
#Copy and paste the following code to create and populate a new location column, based on how a user’s location is classified.

new_df.loc[new_df.population_proper < 100000, "location"] = "rural"
new_df.loc[new_df.population_proper >= 100000, "location"] = "urban"
print(new_df.head(15))


###### Explore the data
# But just because our data is all cleaned up, we still can’t learn a lot by staring at tables. In order to truly explore our data, we’ll need to go a few steps further.
#Changes could include some additional dataset cleaning, collecting more data, or even modifying the initial question we’re trying to answer

## Statical calculations (NumPy)
#When we first get a dataset, we can use descriptive statistics to get a sense of what it contains. 
#Descriptive statistics summarize a given dataset using statistical calculations, such as the average (also known as mean), median, and standard deviation.

## Data Visualization (Matplotlib/Seaborn)
# The practice of data visualization enables us to see patterns, relationships, and outliers, and how they relate to the entire dataset

#let’s use a histogram to visualize the distribution of all of the ages in our dataset.
age = new_df["age"]
sns.displot(age)
 
plt.show() 


# Now that we have a sense of the age distribution of our user base, let’s see if there is a relationship between a user’s age and their location.

location_mean_age = new_df.groupby("location").age.mean() 
 
print(location_mean_age)

# the following code to visualize the means using a barplot
plt.close()
sns.barplot(
    data=new_df,
    x= "location",
    y= "age"
)
plt.show()

# Other visualizations provide other information about the relationship between age and location. 
#For example, a violin plot shows distributions of age like a histogram, but creates separate distributions for each category.
plt.close()
sns.violinplot(x="location", y="age", data=new_df)
 
plt.show()


###### Modeling and Analysis (code applied before "explore the data")

#Data in hand, we can begin to dig in and analyze what we have. To analyze our data, we’ll want to create a model.
#Models are abstractions of reality, informed by real data, that allow us to understand situations and make guesses about how things might change given different variables.

#A model gives us the relationship between two or more variables.
#Models allow us to analyze our data because once we begin to understand the relationships between different variables, we can make inferences about certain circumstances.

#Models are also useful for informing decisions, since they can be used to predict unknowns. 
#Once we understand a relationship between variables, we can introduce unknown variables and calculate different possibilities

#As we collect more data, our model can change, allowing us to draw new insights and get a better idea of what might happen in different circumstances
#Our models can tell us whether or not an observed variance is within reason, is due to an error, or possibly carries significance

#Models can be expressed as mathematical equations, such as the equation for a line. You can use data visualization libraries like Matplotlib and Seaborn to visualize relationships. 
#If you pursue machine learning, you can use the Python package scikit-learn to build predictive models, such as linear regressions.

# We want to understand the relationship between age and location, so let’s make a plot that compares the two. #In this case, we want to know if age is dependent on location
x = new_df["population_proper"]
y = new_df["age"]
 
plt.scatter(x, y, alpha=0.5)

#One useful model that works with a scatter plot is a linear regression because it draws a line of best fit.
sns.regplot(x="population_proper", y="age", data=new_df)

# Show plot
plt.show()

##### Communicating Findings
#Two important parts of communicating data are visualizing and storytelling.

##VISUALIZING
## Storytelling
# Contextualizing your findings and giving them a narrative draws people into your work and enables you to convince them as to why these results are important and why they should make a certain decision.


# Let’s improve this graph so we can include it in a presentation to our product team!
#let’s change the style and colors of the figure so that the line is more visible.

plt.close()
 
sns.set_style("darkgrid")
sns.set_palette("bright")
sns.despine()
 
sns.regplot(x="population_proper", y="age", data=new_df)
 
plt.show()


# change the tick marks on the axes so the population sizes are clearer
ax = plt.subplot(1, 1, 1)
ax.set_xticks([100000, 1000000, 2000000, 4000000, 8000000])
ax.set_xticklabels(["100k", "1m", "2m","4m", "8m"])
 
plt.show()


# re-title the axes and give the plot a title to improve the presentation of the data
ax.set_xlabel("City Population")
ax.set_ylabel("User Age")
plt.title("Age vs Population")
 
plt.show()












