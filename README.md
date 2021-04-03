## Altitude-and-Mortality-Data-Using-Panda
    import pandas as pd
    from pandas import DataFrame
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    from statsmodels.formula.api import ols
    import statsmodels.api as sm
    df = pd.read_csv("C:\\Users\\User\\Downloads\\lmdata.csv")
    print(df)
        latitude  mortality
        0       33.0        219
        1       34.0        222
        2       35.0        225
        3       36.0        228
        4       37.0        231
        5       38.0        234

##1: Load the data and print the column names
         Index(['latitude', 'mortality'], dtype='object')

##2: Generate descriptive statistics for the data
          latitude	mortality
          count	24.000000	24.000000
          mean	41.458333	255.250000
          std	4.476792	23.882411
          min	33.000000	219.000000
          25%	38.375000	236.250000
          50%	41.750000	253.500000
          75%	45.125000	271.250000
          max	48.500000	300.000000

##3: Create a line plot for the variables. Add a title and x & y axes.
       a) Beautify the x-labels
       b) plot a line graph
        x = df['latitude'] 
         y = df['mortality']
        plt.title('Latitude vs Mortality Relationship')
        plt.xlabel('Latitude')
        plt.ylabel('Mortality')
        plt.gcf().autofmt_xdate()
       plt.plot(x,y)
        plt.show()
     ![L v M relationship](https://user-images.githubusercontent.com/75600702/113462918-9de36f80-93f9-11eb-83ce-f2bc8a56035a.PNG)

##4: Create a scatter plot / Add title and (X,Y) axis names
        plt.title('Latitude vs Mortality Relationship')
        plt.xlabel('Latitude')
        plt.ylabel('Mortality')
        plt.gcf().autofmt_xdate()
       df.plot(kind='scatter',x='latitude',y='mortality')


##5: Create a boxplot for mortality
         results = sns.boxplot(x=df['mortality'])
         results.set(title='Mortality Rate',xlabel='Latitude',ylabel='Mortality')
        plt.show()

##6: Conduct a Pearson’s correlation test for the variables
           df.corr()
     	     latitude	mortality
           latitude	1.000000	0.985226
           mortality	0.985226	1.000000

##7: Create a pair plot for the data
       # Create the default pairplot
        sns.pairplot(df)
      (https://user-images.githubusercontent.com/75600702/113463083-5b6e6280-93fa-11eb-9250-75137a77e7e1.PNG)


##8: Type in this command: from statsmodels.formula.api import ols
![Seaborn](https://user-images.githubusercontent.com/75600702/113463438-003d6f80-93fc-11eb-8385-661aabf487b0.PNG)



##9: Create a Seaborn regplot of the regression model and a 95% confidence interval
         
        nancy = sns.regplot(df.latitude,df.mortality)
        nancy.set(title="Linear regression Model")
        plt.show()
     ![regression model](https://user-images.githubusercontent.com/75600702/113463205-ecddd480-93fa-11eb-84c4-6ec0e76a707b.PNG)


##10: Create the regression model using ols() from the statsmodel package
             njoki = df.latitude
             njoki1 = df.mortality
             model = ols("latitude ~ mortality", df)
             results = model.fit()
       ![OLS results](https://user-images.githubusercontent.com/75600702/113463275-4e05a800-93fb-11eb-8ba5-280e4218d3e6.PNG)

##11: Print the model Summary
             print(results.summary())
             Notes:
            [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
            [2] The condition number is large, 2.81e+03. This might indicate that there are
              strong multicollinearity or other numerical problems.
