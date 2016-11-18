import simpleai.machine_learning

with open("input/train.csv", "r") as f:
    train = f.readlines()
    for i in train:
        pass # print i
with open("input/test.csv", "r") as f:
    train = f.readlines()
    for i in train:
        pass # print i


import pandas as pd
import numpy as np
import pylab as plt
from sklearn.ensemble import RandomForestClassifier

plt.rc('figure', figsize=(10,5))

fitsize_with_subplots = (10, 10)

bin_size = 10

df_train = pd.read_csv('input/train.csv')
print df_train.head()
print df_train.tail()
print df_train.dtypes
print df_train.info()
print df_train.describe()


fig = plt.figure(figsize=fitsize_with_subplots)
fig_dims = (3,2)

plt.subplot2grid(fig_dims, (0,0))
df_train['Survived'].value_counts().plot(kind='bar', title='Death and Survival Counts')

plt.subplot2grid(fig_dims, (0,1))
df_train['Pclass'].value_counts().plot(kind='bar', title='Passenger Class Counts')

plt.subplot2grid(fig_dims, (1,0))
df_train['Sex'].value_counts().plot(kind='bar', title='Gender Counts')

plt.xticks(rotation=0)

plt.subplot2grid(fig_dims, (1,1))
df_train['Embarked'].value_counts().plot(kind='bar', title='Ports of Embarkation Counts')

plt.subplot2grid(fig_dims, (2,0))
df_train['Age'].hist()
plt.title('Age Histogram')

pclass_xt = pd.crosstab(df_train['Pclass'], df_train['Survived'])

sexes = sorted(df_train['Sex'].unique())

genders_mapping = dict(zip(sexes, range(0, len(sexes) + 1)))

df_train['Sex_Val'] = df_train['Sex'].map(genders_mapping).astype(int)

sex_val_xt = pd.crosstab(df_train['Sex_Val'], df_train['Survived'])
sex_val_xt_pct = sex_val_xt.div(sex_val_xt.sum(1).astype(float, axis=0))

passenger_classes = sorted(df_train['Pclass'].unique())



females_df = df_train[df_train['Sex'] == 'female']
females_xt = pd.crosstab(females_df['Pclass'], df_train['Survived'])
females_xt_pct = females_xt.div(females_xt.sum(1))

males_df = df_train[df_train['Sex'] == 'male']
males_xt = pd.crosstab(males_df['Pclass'], df_train['Survived'])
males_xt_pct = males_xt.div(males_xt.sum(1))


embarked_locs = sorted(df_train['Embarked'].unique())
embarked_locs_mapping = dict(zip(embarked_locs, range(0, len(embarked_locs) + 1)))


# if len(df_train[df_train['Embarked'].isnull()] > 0):
#     df_train.replace({ 'Embarked_Val':  {embarked_locs_mapping[embarked_locs[0]]:embarked_locs_mapping['S']}
#                        }, inplace=True)
#
# embarked_locs = sorted(df_train['Embarked_Val'].unique())


print df_train[df_train['Age'].isnull()][['Sex', 'Pclass', 'Age']].head()

df_train['AgeFill'] = df_train['Age']

df_train['AgeFill'] = df_train['AgeFill'].groupby([df_train['Sex_Val'], df_train['Pclass']]).apply(lambda x: x.fillna(x.median()))

df_train['FamilySize'] = df_train['SibSp'] + df_train['Parch']


print df_train.dtypes[df_train.dtypes.map(lambda x: x == 'object')]

df_train = df_train.drop(['Name', 'Sex', 'Ticket', 'Cabin', 'Embarked'], axis=1)
df_train = df_train.drop(['Age', 'SibSp', 'Parch', 'PassengerId'], axis=1)

train_data = df_train.values
print train_data

clf = RandomForestClassifier(n_estimators=100)

train_features = train_data[:, 1:]

train_target = train_data[:, 0]

clf = clf.fit(train_features, train_target)
score = clf.score(train_features, train_target)

print "Mean accuracy of Random Forest: {0}".format(score)

# plt.show()


