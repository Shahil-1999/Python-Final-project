import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import voice.speak as sp
import voice.command as cmd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)

def parkinson():
    



    df = pd.read_csv('C:/Users/kshah/OneDrive/Desktop/test_major_project/Python-Final-project/disease_pred/parkinsons.csv')
    # print(df.info())
    # print(df.describe())
    df.isnull().sum()#checking for missing values


    #dropping column axis = 1; dropping row then axis = 0
    #Data Pre-Processing - Seperating Features and Target variables according to their Correlation

    df.drop(["name",'spread1', 'MDVP:Flo(Hz)','MDVP:Fhi(Hz)','MDVP:Fo(Hz)'], axis=1, inplace=True)
    columns = list(df.columns)
    for column in columns:
        if column == "status":
            continue

        filtered_columns = [column]
        for col in df.columns:
            if (column == col) | (column == "status"):
                continue
            cor_val = df[column].corr(df[col])
            if cor_val > 0.75:
                columns.remove(col)
                continue
            else:
                filtered_columns.append(col)
        df = df[filtered_columns]
        
        
    df.isnull().sum() #checking null value


    # converting Data in the form of hundred
    # df.iloc[:,:8] = (df.iloc[:, 8:9])
 





    #Plotting Heatmap
    # plt.figure(figsize=(25, 7))
    # p = sns.heatmap(df.corr(), annot=True)
    # plt.show()


    # plotting bar figure on STATUS column
    # sns.set_style('whitegrid')
    # sns.set_context('paper')
    # sns.set_palette('GnBu_d')
    # a = sns.catplot(x='status', data=df, kind='count')
    # plt.title('Number of Samples in Each Class')
    # a.set(ylabel='Number of Samples', xlabel='Have Parkinson')

    # plt.show()

    #histogram
    # df.hist(figsize=(25,7))
    # plt.show()
    #We can see some of the data is normally distributed and most of the attributes are right skewed



    # Splitting the data into testing and training set
    x_train, x_test, y_train, y_test = train_test_split(df.drop(columns=['status']), df['status'], test_size=0.2, random_state = 42)

    # Model Training (DecisionTreeClassifier)
    clf = DecisionTreeClassifier()
    clf.fit(x_train, y_train)

    # # Model Evaluation
    # # Accuracy Score

    # # Accuracy Score on training data
    # x_train_pred = clf.predict(x_train)
    # training_data_accuracy = accuracy_score(y_train, x_train_pred)
        
    # print('Accuracy (Training Data) :', training_data_accuracy*100,'%')


    # # Accuracy Score on test data
    # x_test_pred = clf.predict(x_test)
    # testing_data_accuracy = accuracy_score(y_test, x_test_pred)
        

    # print('Accuracy (Testing Data) :', testing_data_accuracy*100,'%')
    
    
    
    print("Enter your First nonlinear dynamical complexity measures (1.42 - 3.67)")
    sp.speak("Enter your First nonlinear dynamical complexity measures (1.42 - 3.67)")
    D2 = cmd.takeCommand().lower()
    print(D2)
    sp.speak(D2)
    
    print("if you satisfy with this value then press Y, else press N")
    sp.speak("if you satisfy with this value then press Y, else press N")
    
    D2_satisfaction = input("Enter your value : ")
    if D2_satisfaction.lower() == "n":
        sp.speak("Enter New Value: ")
        new_input_D2 = input("Enter New Value : ")
        D2 = (new_input_D2)
        print(D2)
        sp.speak(D2)
    # else:
    #     os.system("pause")
        
    
    
    
    
    
    print("Enter your second nonlinear dynamical complexity measures (0.25 - 0.68)")
    sp.speak("Enter your second nonlinear dynamical complexity measures (0.25 - 0.68)")
    RPDE = cmd.takeCommand().lower()
    print(RPDE)
    sp.speak(RPDE)
    
    print("if you satisfy with this value then press Y, else press N")
    sp.speak("if you satisfy with this value then press Y, else press N")
    RPDE_satisfaction = input("Enter your value : ")
    if RPDE_satisfaction.lower() == "n":
        sp.speak("Enter New Value: ")
        new_input_RPDE = input("Enter New Value : ")
        RPDE = (new_input_RPDE)
        print(RPDE)
        sp.speak(RPDE)
    # else:
    #     os.system("pause")
    
    
    print('Enter your third nonlinear measures of fundamental frequency variation (0.04 - 0.52)')
    sp.speak('Enter your third nonlinear measures of fundamental frequency variation (0.04 - 0.52)')
    PPE = cmd.takeCommand().lower()
    print(PPE)
    sp.speak(PPE)
    
    print("if you satisfy with this value then press Y, else press N")
    sp.speak("if you satisfy with this value then press Y, else press N")
    PPE_satisfaction = input("Enter your value : ")
    if PPE_satisfaction.lower() == "n":
        sp.speak("Enter New Value: ")
        new_input_PPE = input("Enter New Value : ")
        PPE = (new_input_PPE)
        print(PPE)
        sp.speak(PPE)
    # else:
    #     os.system("pause")
    
    print("Enter your nonlinear fundamental frequency variation (0.00 - 0.45)")
    sp.speak("Enter your nonlinear fundamental frequency variation (0.00 - 0.45)")
    spread2 = cmd.takeCommand().lower()
    print(spread2)
    sp.speak(spread2)
    
    print("if you satisfy with this value then press Y, else press N")
    sp.speak("if you satisfy with this value then press Y, else press N")
    spread2_satisfaction = input("Enter your value : ")
    if spread2_satisfaction.lower() == "n":
        sp.speak("Enter New Value: ")
        new_input_spread2 = input("Enter New Value : ")
        spread2 = (new_input_spread2)
        print(spread2)
        sp.speak(spread2)
    # else:
    #     os.system("pause")
    
    print("Enter your Signal fractal scaling exponent (0.57 - 0.82)")
    sp.speak("Enter your Signal fractal scaling exponent (0.57 - 0.82)")
    DFA = cmd.takeCommand().lower()
    print(DFA)
    sp.speak(DFA)
    
    print("if you satisfy with this value then press Y, else press N")
    sp.speak("if you satisfy with this value then press Y, else press N")
    DFA_satisfaction = input("Enter your value : ")
    if DFA_satisfaction.lower() == "n":
        sp.speak("Enter New Value: ")
        new_input_DFA = input("Enter New Value : ")
        DFA = (new_input_DFA)
        print(DFA)
        sp.speak(DFA)
    # else:
    #     os.system("pause")
    
    
    
    print("Enter your ratio of noise to tonal components in the voice (8.44 - 33.04)")
    sp.speak("Enter your ratio of noise to tonal components in the voice (8.44 - 33.04)")
    HNR = cmd.takeCommand().lower()
    print(HNR)
    sp.speak(HNR)
    
    print("if you satisfy with this value then press Y, else press N")
    sp.speak("if you satisfy with this value then press Y, else press N")
    HNR_satisfaction = input("Enter your value : ")
    if HNR_satisfaction.lower() == "n":
        sp.speak("Enter New Value: ")
        new_input_HNR = input("Enter New Value : ")
        HNR = (new_input_HNR)
        print(HNR)
        sp.speak(HNR)
    # else:
    #     os.system("pause")
    

    
    
    print("Enter your Several measures of variation in amplitude(0.00 - 0.05)")
    sp.speak("Enter your Several measures of variation in amplitude(0.00 - 0.05)")
    Shimar = cmd.takeCommand().lower()
    print(Shimar)
    sp.speak(Shimar)
    
    print("if you satisfy with this value then press Y, else press N")
    sp.speak("if you satisfy with this value then press Y, else press N")
    Shimar_satisfaction = input("Enter your value : ")
    if Shimar_satisfaction.lower() == "n":
        sp.speak("Enter New Value: ")
        new_input_Shimar = input("Enter New Value : ")
        Shimar = (new_input_Shimar)
        print(Shimar)
        sp.speak(Shimar)
    # else:
    #     os.system("pause")
  

    
    print("Enter your Several measures of variation in fundamental frequency (0.00 - 0.03)")
    sp.speak("Enter your Several measures of variation in fundamental frequency (0.00 - 0.03)")
    Jitter = cmd.takeCommand().lower()
    print(Jitter)
    sp.speak(Jitter)
    
    print("if you satisfy with this value then press Y, else press N")
    sp.speak("if you satisfy with this value then press Y, else press N")
    Jitter_satisfaction = input("Enter your value : ")
    if Jitter_satisfaction.lower() == "n":
        sp.speak("Enter New Value: ")
        new_input_Jitter = input("Enter New Value : ")
        Jitter = (new_input_Jitter)
        print(Jitter)
        sp.speak(Jitter)
    # else:
    #     os.system("pause")
    
    
 


    p_pred = clf.predict([[D2, RPDE, PPE, spread2, DFA, HNR,Shimar, Jitter]])

   
    predicted = ""

    if p_pred == 0:
        predicted = 'Not Affected'
        
        
    else:
        p_pred == 1
        predicted = 'Affected'
    
        print("pre:", predicted)    
 
        return predicted



