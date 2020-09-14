#simple Linear Regression
library(readr)

#imorting the dataset
#"C:\Users\Aishwarya\Desktop\360DigitTMg\linear regression\Salary_Data.csv"
salary_data <- read.csv("C:\\Users\\Aishwarya\\Desktop\\360DigitTMg\\linear regression\\Salary_Data.csv")
colnames(salary_data)
str(salary_data)
summary(salary_data)

#splitting the dataset into training set and test set
library(caTools)
set.seed(123)
split = sample.split(salary_data$Salary, SplitRatio = 2/3)
training_set = subset(salary_data , split == TRUE)
test_set = subset(salary_data , split == FALSE)

#Training the model with linear regression
regressor = lm(formula = Salary ~ YearsExperience,data = training_set)
summary(regressor)

#predicting the test set results
y_pred = predict(regressor , newdata = test_set)
y_pred

#visualizing the training set results
library(ggplot2) #for the visualization
ggplot() + 
  geom_point(aes(x = training_set$YearsExperience,y = training_set$Salary),
              colour = "red") + 
  geom_line(aes(x = training_set$YearsExperience , y =predict(regressor , newdata = training_set)),
            colour = "Blue") +
  ggtitle("Salary Vs YearOfExperience(Training set)") +
  xlab("year of experience") +
  ylab("Salary")

#visualizing the test set results
library(ggplot2) #for the visualization
ggplot() + 
  geom_point(aes(x = test_set$YearsExperience,y = test_set$Salary),
             colour = "red") + 
  geom_line(aes(x = test_set$YearsExperience , y =predict(regressor , newdata = test_set)),
            colour = "Blue") +
  ggtitle("Salary Vs YearOfExperience(Test set)") +
  xlab("year of experience") +
  ylab("Salary")
  

