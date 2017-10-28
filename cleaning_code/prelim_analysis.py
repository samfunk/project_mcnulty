import pandas as pd
import matplotlib.pyplot as plt
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, roc_curve, auc

np.random.seed(42)

with open('/Users/samfunk/ds/metis/project_mcnulty/datafiles/master_df.pkl', 'rb') as f:
    master = pickle.load(f)


shuffle = master.sample(frac=1)

X = np.array(shuffle.loc[:, 'free_cash_flow':])
y = np.array(shuffle.buckets)

X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.25, random_state=42)

ss = StandardScaler()
ss.fit(X_train)
X_train_std = ss.transform(X_train)
X_test_std = ss.fit_transform(X_test)

k_range = list(range(1,21))
k_scores = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X_std, y, cv=3, scoring='accuracy')
    k_scores.append(np.mean(scores))

for i, k in enumerate(k_scores):
    print(i, k)


model = KNeighborsClassifier(n_neighbors=8)
scores = [np.mean(cross_val_score(model, X, y, cv=3, scoring=score)) for score in ['accuracy', 'precision_macro', 'recall_macro', 'f1_macro']]

print('KNN (k=8)',
          'Accuracy: %0.3f,' % scores[0],
          'Precision: %0.3f,' % scores[1],
          'Recall: %0.3f,' % scores[2],
          'F1: %0.3f' % scores[3],
    )




'''yprobpred = model.predict_proba(X_test)[:,1]
fpr, tpr, _ = roc_curve(Y_test, yprobpred)
roc_auc = auc(fpr, tpr)
lw = 2
plt.plot(fpr, tpr, color='darkorange',
         lw=lw, label='%s ROC curve (area = %0.2f)' % (name, roc_auc))
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('%s ROC Curve' % name)
plt.legend(loc="lower right")
plt.show()'''
groups = shuffle.groupby('bucket')
fig, ax = plt.subplots()
for name, group in groups:
    ax.plot(group[('return', 'mean')], group[('return', 'std')], marker='o', linestyle='', ms=12, label=name)
plt.xlabel('Mean Return')
plt.ylabel('Std Return')
plt.title('Mean vs. Std Returns for Basket of Companies')
plt.legend()
#plt.scatter(master[('return', 'mean')], master[('return', 'std')])
plt.show()
