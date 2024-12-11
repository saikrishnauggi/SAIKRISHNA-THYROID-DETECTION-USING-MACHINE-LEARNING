from tkinter import messagebox
from tkinter import *
from tkinter import simpledialog
import tkinter
from tkinter import filedialog
import matplotlib.pyplot as plt
from tkinter.filedialog import askopenfilename
import numpy as np
import os
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from imblearn.over_sampling import SMOTE

main = tkinter.Tk()
main.title("DETECTION OF THYROID DISORDERS USING MACHINE LEARNING APPOARCH")
main.geometry("1300x1200")

global filename, rf_cls, X, Y
global accuracy, precision, recall, fscore
global X_train, X_test, y_train, y_test
global labels
global label_encoder, scaler


def upload():
    global filename, labels, dataset
    filename = filedialog.askopenfilename(initialdir="Dataset")
    text.delete('1.0', END)
    text.insert(END, filename + " loaded\n")
    dataset = pd.read_csv(filename)
    text.insert(END, str(dataset) + "\n\n")
    text.update_idletasks()
    labels = np.unique("binaryClass")
    label = dataset.groupby('binaryClass').size()
    label.plot(kind="bar")
    plt.xlabel("P (Thyroid Presence) & N (Normal)")
    plt.ylabel("Count")
    plt.title("Normal & Thyroid Patient Graph")
    plt.show()


def preprocess():
    text.delete('1.0', END)
    global dataset, X, Y, label_encoder, scaler
    global X_train, X_test, y_train, y_test
    label_encoder = []
    dataset.fillna(0, inplace=True)
    dataset["age"] = dataset["age"].astype(float)
    dataset["TSH"] = dataset["TSH"].astype(float)
    dataset["T3"] = dataset["T3"].astype(float)
    dataset["TT4"] = dataset["TT4"].astype(float)
    dataset["T4U"] = dataset["T4U"].astype(float)
    dataset["FTI"] = dataset["FTI"].astype(float)
    columns = dataset.columns
    types = dataset.dtypes.values
    print(dataset.info())
    for i in range(len(types)):
        name = types[i]
        if name == 'object':
            le = LabelEncoder()
            dataset[columns[i]] = pd.Series(le.fit_transform(dataset[columns[i]].astype(str)))
            label_encoder.append(le)
    print(dataset.info())
    scaler = StandardScaler()
    text.insert(END, "Dataset Preprocessing & Normalization Process Completed\n\n")
    text.insert(END, str(dataset) + "\n\n")
    dataset = dataset.values
    X = dataset[:, 0:dataset.shape[1] - 1]
    Y = dataset[:, dataset.shape[1] - 1]
    print(X)
    print(Y)
    X = scaler.fit_transform(X)
    indices = np.arange(X.shape[0])
    np.random.shuffle(indices)
    X = X[indices]
    Y = Y[indices]
    sm = SMOTE(random_state=42)
    X, Y = sm.fit_resample(X, Y)
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
    text.insert(END, "Total records found in dataset : " + str(X.shape[0]) + "\n\n")
    text.insert(END, "Dataset split for train and test\n\n")
    text.insert(END, "80% dataset records used to train Machine Learning Algorithms : " + str(X_train.shape[0]) + "\n")
    text.insert(END, "20% dataset records used to test Machine Learning Algorithms : " + str(X_test.shape[0]) + "\n")


def calculateMetrics(algorithm, y_test, predict):
    a = accuracy_score(y_test, predict) * 100
    p = precision_score(y_test, predict, average='macro') * 100
    r = recall_score(y_test, predict, average='macro') * 100
    f = f1_score(y_test, predict, average='macro') * 100
    accuracy.append(a)
    precision.append(p)
    recall.append(r)
    fscore.append(f)
    text.insert(END, algorithm + " Accuracy  :  " + str(a) + "\n")
    text.insert(END, algorithm + " Precision : " + str(p) + "\n")
    text.insert(END, algorithm + " Recall    : " + str(r) + "\n")
    text.insert(END, algorithm + " FScore    : " + str(f) + "\n\n")
    conf_matrix = confusion_matrix(y_test, predict)
    label = ["Normal", "Thyroid Detected"]
    ax = sns.heatmap(conf_matrix, xticklabels=label, yticklabels=label, annot=True, cmap="viridis", fmt="g")
    ax.set_ylim([0, len(label)])
    plt.title(algorithm + " Confusion matrix")
    plt.ylabel('True class')
    plt.xlabel('Predicted class')
    plt.show()


def runNaiveBayes():
    text.delete('1.0', END)
    global X_train, X_test, y_train, y_test
    global accuracy, precision, recall, fscore
    accuracy = []
    precision = []
    recall = []
    fscore = []

    nb_cls = GaussianNB()
    nb_cls.fit(X_train, y_train)
    predict = nb_cls.predict(X_test)
    calculateMetrics("Naive Bayes", y_test, predict)


def runSVM():
    svm_cls = svm.SVC()
    svm_cls.fit(X_train, y_train)
    predict = svm_cls.predict(X_test)
    calculateMetrics("SVM", y_test, predict)


def runRF():
    global rf_cls
    rf_cls = RandomForestClassifier()
    rf_cls.fit(X_train, y_train)
    predict = rf_cls.predict(X_test)
    calculateMetrics("Random Forest", y_test, predict)


def graph():
    df = pd.DataFrame([['Naive Bayes', 'Precision', precision[0]], ['Naive Bayes', 'Recall', recall[0]],
                       ['Naive Bayes', 'F1 Score', fscore[0]], ['Naive Bayes', 'Accuracy', accuracy[0]],
                       ['SVM', 'Precision', precision[1]], ['SVM', 'Recall', recall[1]], ['SVM', 'F1 Score', fscore[1]],
                       ['SVM', 'Accuracy', accuracy[1]], ['Random Forest', 'Precision', precision[2]],
                       ['Random Forest', 'Recall', recall[2]], ['Random Forest', 'F1 Score', fscore[2]],
                       ['Random Forest', 'Accuracy', accuracy[2]],
                       ], columns=['Parameters', 'Algorithms', 'Value'])
    df.pivot("Parameters", "Algorithms", "Value").plot(kind='bar')
    plt.show()


def predict():
    text.delete('1.0', END)
    global rf_cls, scaler, label_encoder
    filename = filedialog.askopenfilename(initialdir="Dataset")
    dataset = pd.read_csv(filename)
    dataset.fillna(0, inplace=True)
    columns = dataset.columns
    types = dataset.dtypes.values
    for i in range(len(columns)):
        dataset[columns[i]] = dataset[columns[i]].astype(str)
    dataset["age"] = dataset["age"].astype(float)
    dataset["TSH"] = dataset["TSH"].astype(float)
    dataset["T3"] = dataset["T3"].astype(float)
    dataset["TT4"] = dataset["TT4"].astype(float)
    dataset["T4U"] = dataset["T4U"].astype(float)
    dataset["FTI"] = dataset["FTI"].astype(float)
    columns = dataset.columns
    types = dataset.dtypes.values
    print(dataset.info())
    index = 0
    for i in range(len(types)):
        name = types[i]
        if name == 'object':
            dataset[columns[i]] = pd.Series(label_encoder[index].fit_transform(dataset[columns[i]].astype(str)))
            index = index + 1

    print(dataset.info())
    dataset = dataset.values
    testData = scaler.transform(dataset)
    predict = rf_cls.predict(testData)
    print(predict)
    for i in range(len(predict)):
        if predict[i] != 1:
            print(str(i) + " " + str(predict[i]))
    for i in range(len(predict)):
        pred = predict[i]
        if pred == 0:
            text.insert(END, "Test Data = " + str(dataset[i]) + "=====> Predicted AS NORMAL\n\n")
        if pred == 0:
            text.insert(END, "Test Data = " + str(dataset[i]) + "=====> Predicted AS THYROID DETECTED\n\n")


font = ('times', 16, 'bold')
title = Label(main, text='DETECTION OF THYROID DISORDERS USING MACHINE LEARNING APPOARCH')
title.config(bg='firebrick4', fg='dodger blue')
title.config(font=font)
title.config(height=3, width=120)
title.place(x=0, y=5)

font1 = ('times', 12, 'bold')
text = Text(main, height=24, width=150)
scroll = Scrollbar(text)
text.configure(yscrollcommand=scroll.set)
text.place(x=40, y=120)
text.config(font=font1)

font1 = ('times', 13, 'bold')
uploadButton = Button(main, text="Upload Thyroid Dataset", command=upload, bg='#ffb3fe')
uploadButton.place(x=50, y=600)
uploadButton.config(font=font1)

processButton = Button(main, text="Preprocess Dataset", command=preprocess, bg='#ffb3fe')
processButton.place(x=370, y=600)
processButton.config(font=font1)

nbButton1 = Button(main, text="Run Naive Bayes Algorithm", command=runNaiveBayes, bg='#ffb3fe')
nbButton1.place(x=610, y=600)
nbButton1.config(font=font1)

svmButton = Button(main, text="Run SVM Algorithm", command=runSVM, bg='#ffb3fe')
svmButton.place(x=900, y=600)
svmButton.config(font=font1)

rfButton = Button(main, text="Run Random Forest Algorithm", command=runRF, bg='#ffb3fe')
rfButton.place(x=50, y=650)
rfButton.config(font=font1)

graphButton = Button(main, text="Comparison Graph", command=graph, bg='#ffb3fe')
graphButton.place(x=360, y=650)
graphButton.config(font=font1)

predictButton = Button(main, text="Predict Disease from Test Data", command=predict, bg='#ffb3fe')
predictButton.place(x=610, y=650)
predictButton.config(font=font1)

main.config(bg='LightSalmon3')
main.mainloop()