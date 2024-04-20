import pandas as pd
import numpy as np
df=pd.read_csv('titanic.csv')
print(df)
print(df.columns)
print(pd.crosstab(df['Name'],df['SibSp']))
print(pd.crosstab(df['Sex'],df['Pclass']),'\n')
print(pd.crosstab([df['Embarked'],df["Survived"]],df['Sex']))
print(pd.crosstab([df['Embarked'],df["Survived"]],[df['Sex'],df['Pclass']])) #different methods
print(pd.crosstab([df['Embarked'],df["Survived"],df['Pclass']],df['Sex']))
print(pd.crosstab(df['Sex'],df['Pclass'], margins=True,),'\n') #gives the total value of each case
print(pd.crosstab(df['Sex'],df['Pclass'], normalize='all')) 
print(df.dtypes)
df=df.fillna(method='ffill')
print(pd.unique(df['Embarked']))
df['Cabin']=df['Cabin'].fillna(method='ffill')
print(pd.crosstab([df['Pclass'],df['Sex']],df['Survived']))
print(pd.crosstab(df['Sex'],df['Survived']))
print(df.columns)
print(pd.crosstab([df['Sex'],df['Survived']],df['Pclass']))
df1=df[df['Sex']=='female']
df2=df[df['Sex']=='male']
print(pd.crosstab(df1['Pclass'],df1['Survived']),'\n')
print(pd.crosstab(df2['Pclass'],df2['Survived']))
print(pd.value_counts(df['Survived']))
print(pd.crosstab([df['Sex'],df['SibSp']],df['Parch']))
print(df.insert(7,'family',''))
df['family']=df['SibSp']+df['Parch']
print(df['family'])
df1=df[df['Sex']=='female']
df2=df[df['Sex']=='male']
print(pd.crosstab(df['Sex'],df['family']))
print(sum(df1['family']))
print(sum(df2['family']))
print(pd.crosstab(df1['Age'],df1['Sex']))
print(df1['Age'].dtypes)
df11=(df1[(df1['Age']>25) & (df1['Age']<36)])  # dataset women of age between 25 and 35 
print(pd.crosstab(df11['Survived'],df11['Pclass'])) 
print(df11.value_counts('Survived'))
df22=df2[(df2['Age']>25) & (df2['Age']<36)]
print(pd.crosstab(df22['Survived'],df22['Pclass'])) 
print(df22.value_counts('Survived'))
iris=pd.read_csv('titanic.csv')
print(iris)
print(iris.columns)
print(iris.dtypes)
print(pd.unique(iris['Name']))
print(np.unique(iris['Name']))
print(np.unique(iris['Pclass']))
print(pd.unique(iris['Cabin']))
print(pd.unique(iris['Embarked']))
print(pd.unique(iris['Fare']))
print(pd.unique(iris['Survived']))
print(pd.crosstab(iris['Sex'],iris['Survived']))
f=iris[iris['Sex']=='female']
print(f)
m=iris[iris['Sex']=='male']
print(m)
print(sum(m['Survived']==1))
print(pd.crosstab((m['Survived']==1),(f['Survived']==1)))
iris=pd.read_csv('titanic.csv')
print(iris)
print(iris.columns)
print(iris.dtypes)
print(pd.unique(iris['Name']))
print(np.unique(iris['Name']))
print(np.unique(iris['Pclass']))
print(pd.unique(iris['Cabin']))
print(pd.unique(iris['Embarked']))
print(pd.unique(iris['Fare']))
print(pd.unique(iris['Survived']))
print(pd.crosstab(iris['Sex'],iris['Survived']))
f=iris[iris['Sex']=='female']
print(f)
m=iris[iris['Sex']=='male']
print(m)
print(sum(m['Survived']==1))
print(pd.crosstab((m['Survived']==1),(f['Survived']==1)))