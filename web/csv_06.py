# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 06:27:02 2018

@author: LUISFERNANDO
"""
from flask import Flask, Request, jsonify
import psycopg2 as pg
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)


def get_connection():
    
    connection = pg.connect("host='127.0.0.1' dbname='usco1' user='usco1' password='usco1'")
    return connection

def get_dataset():
    
    sql = "SELECT sepal_lenght, sepal_width, petal_lenght,"
    sql = sql + " petal_width, class FROM iris"
    dataset = pd.read_sql_query(sql, con=get_connection())
    
    return dataset


@app.route('/')
def hello_world():
   return "Hello World"

@app.route('/build')
def build():
    # Python version
    import sys
    print('Python: {}'.format(sys.version))
    # scipy
    import scipy
    print('scipy: {}'.format(scipy.__version__))
    # numpy
    import numpy
    print('numpy: {}'.format(numpy.__version__))
    # matplotlib
    import matplotlib
    print('matplotlib: {}'.format(matplotlib.__version__))
    # pandas
    import pandas
    print('pandas: {}'.format(pandas.__version__))
    # scikit-learn
    import sklearn
    print('sklearn: {}'.format(sklearn.__version__))
    
    
    # Load libraries
    import pandas
    from pandas.plotting import scatter_matrix
    import matplotlib.pyplot as plt
    from sklearn import model_selection
    from sklearn.metrics import classification_report
    from sklearn.metrics import confusion_matrix
    from sklearn.metrics import accuracy_score
    from sklearn.linear_model import LogisticRegression
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    from sklearn.naive_bayes import GaussianNB
    from sklearn.svm import SVC
    
    # Load libraries
    import pandas
    from pandas.plotting import scatter_matrix
    import matplotlib.pyplot as plt
    from sklearn import model_selection
    from sklearn.metrics import classification_report
    from sklearn.metrics import confusion_matrix
    from sklearn.metrics import accuracy_score
    from sklearn.linear_model import LogisticRegression
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    from sklearn.naive_bayes import GaussianNB
    from sklearn.svm import SVC
    
    
    # Load libraries
    import pandas
    from pandas.plotting import scatter_matrix
    import matplotlib.pyplot as plt
    from sklearn import model_selection
    from sklearn.metrics import classification_report
    from sklearn.metrics import confusion_matrix
    from sklearn.metrics import accuracy_score
    from sklearn.linear_model import LogisticRegression
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    from sklearn.naive_bayes import GaussianNB
    from sklearn.svm import SVC
    
    # Load dataset
    """
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
    names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
    dataset = pandas.read_csv(url, names=names)
    """
    
    
    dataset = get_dataset()
    
    
    # shape
    print(dataset.shape)
    
    
    # head
    print(dataset.head(20))
    
    # descriptions
    print(dataset.describe())
    
    # class distribution
    print(dataset.groupby('class').size())
    
    # Split-out validation dataset
    array = dataset.values
    X = array[:,0:4]
    Y = array[:,4]
    validation_size = 0.20
    seed = 7
    X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)
    
    # Test options and evaluation metric
    seed = 7
    scoring = 'accuracy'
    
    # Spot Check Algorithms
    models = []
    models.append(('LR', LogisticRegression()))
    models.append(('LDA', LinearDiscriminantAnalysis()))
    models.append(('KNN', KNeighborsClassifier()))
    models.append(('CART', DecisionTreeClassifier()))
    models.append(('NB', GaussianNB()))
    models.append(('SVM', SVC()))
    # evaluate each model in turn
    results = []
    names = []
    for name, model in models:
    	kfold = model_selection.KFold(n_splits=10, random_state=seed)
    	cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
    	results.append(cv_results)
    	names.append(name)
    	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    	print(msg)

    # Compare Algorithms
    fig = plt.figure()
    fig.suptitle('Algorithm Comparison')
    ax = fig.add_subplot(111)
    plt.boxplot(results)
    ax.set_xticklabels(names)
    plt.show()

    # Make predictions on validation dataset
    knn = KNeighborsClassifier()
    knn.fit(X_train, Y_train)
    
    # Save the model
    filehandler = open("../models/modelo.mod", "wb")
    pickle.dump(knn, filehandler)
    filehandler.close()
    
    predictions = knn.predict(X_validation)
    print(accuracy_score(Y_validation, predictions))
    print(confusion_matrix(Y_validation, predictions))
    print(classification_report(Y_validation, predictions))
    return 'fin construcción'


@app.route('/clasificar', methods=['POST'])
def clasificar():
    
    file = open("../models/modelo.mod", "rb")
    knn = pickle.load(file)
    file.close()
    
    json_data = request.json
    sl = json_data['sl']
    sw = json_data['sw']
    pl = json_data['pl']
    pw = json_data['pw']
    
    datos = np.array([sl, sw, pl, pw], ndmin = 2 )
    
    predictions = knn.predict(datos)
    print(type(predictions))
    print(predictions)
    
    
    return jsonify(clase=predictions[0])
    
    
if __name__ == '__main__':
   app.run()
