import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import voice.speak as sp
import voice.command as cmd
from sklearn import svm
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)



def breast_cancer():

    df = pd.read_csv('C:/Users/kshah/OneDrive/Desktop/test_major_project/Python-Final-project/disease_pred/br.csv')
    
    # histogram before applying feature engineering
    # df.hist(figsize=(90,90))
    # plt.show()

    # Plotting Heatmap(before feature engineering)
    # plt.figure(figsize=(25, 7))
    # p = sns.heatmap(df.corr(), annot=True)
    # plt.show()

    # Feature Selection
    # a1 = body_p.corr()   
    # x1 = a1['class'].sort_values(ascending=False)
    df = df.iloc[:, 1:6]
    x_train, x_test, y_train, y_test = train_test_split(df.drop(columns=['diagnosis']), df['diagnosis'], test_size=0.2, random_state=42)
    clf = svm.SVC(kernel='linear')
    clf.fit(x_train, y_train)
    
    # Accuracy Score on training data
    # x_train_pred = clf.predict(x_train)
    # training_data_accuracy = accuracy_score(y_train, x_train_pred)  
    # print('Accuracy (Training Data) :', training_data_accuracy*100,'%')


    # # Accuracy Score on test data
    # x_test_pred = clf.predict(x_test)
    # testing_data_accuracy = accuracy_score(y_test, x_test_pred)
    # print('Accuracy (Testing Data) :', testing_data_accuracy*100,'%')


    # histogram after applying feature engineering
    # df.hist(figsize=(25,7))
    # plt.show()

    # plotting bar figure on Diagnosis column after feature engineering
    # sns.set_style('whitegrid')
    # sns.set_context('paper')
    # sns.set_palette('GnBu_d')
    # a = sns.catplot(x='diagnosis', data=df, kind='count')
    # plt.title('Number of Samples in Each Class')
    # a.set(ylabel='Number of Samples', xlabel='M = Malignant, B = Benign')
    # plt.show()
    


    print("Please enter radius_mean Range(6.981 - 28.11): ")                                  
    sp.speak("Please enter radius_mean Range(6.981 - 28.11): ")
    radius_mean = cmd.takeCommand().lower()
    print(radius_mean)
    sp.speak(radius_mean)

    print("Please enter texture_mean (9.71 - 39.28): ")
    sp.speak("Please enter texture_mean (9.71 - 39.28): ")
    texture_mean = cmd.takeCommand().lower()
    print(texture_mean)
    sp.speak(texture_mean)


    print("Please enter perimeter_mean (43.79 - 188.5): ")
    sp.speak("Please enter perimeter_mean (43.79 - 188.5): ")
    perimeter_mean = cmd.takeCommand().lower()
    print(perimeter_mean)
    sp.speak(perimeter_mean)


    print("Please enter area_mean(143.5 - 2501): ")
    sp.speak("Please enter area_mean(143.5 - 2501): ")
    area_mean = cmd.takeCommand().lower()
    print(area_mean)
    sp.speak(area_mean)


    preds = clf.predict([[radius_mean, texture_mean, perimeter_mean, area_mean]])
    f_pred = (' '.join(preds))
    
    if f_pred == 'B':
        f_pred = 'Benign'
    else:
        f_pred = 'Malignant'
    sp.speak(f_pred)
    return f_pred




