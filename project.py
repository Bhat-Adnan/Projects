"""
Project Start Date: 26/12/2023
Contributors: Adnan Fareed, Jasspreet Singh, Kamran Jeelani
Purpose: Result prediction of students using machine learning
"""


import PIL.Image
import pandas as pd
from PIL import Image,ImageFile
import tkinter as tk
from tkinter import *
from tkinter import messagebox

from tkinter.font import Font
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestRegressor 
from sklearn.model_selection import train_test_split 
from matplotlib.animation import FuncAnimation
from PIL import ImageTk, Image



if __name__=='__main__':
    global flag_csv
    flag_csv=0
    
    global df_pre
    global regressor_2,X_test_2,y_test_2
    global regressor_3,X_test_3,y_test_3
    global regressor_4,X_test_4,y_test_4
    global regressor_5,X_test_5,y_test_5
    global regressor_6,X_test_6,y_test_6
    global regressor_7,X_test_7,y_test_7
    global regressor_8,X_test_8,y_test_8
    df_pre=pd.read_csv("export_df.csv")
    
    #sem2
    df2=df_pre.copy()
    df2.dropna(subset = ['1','2'], inplace=True)
    #print(df2)
    X_2=df2[['1']]
    y_2=df2['2']
    
    X_train_2, X_test_2, y_train_2, y_test_2 = train_test_split(X_2, y_2, test_size=0.33, random_state=100) 
    regressor_2 = RandomForestRegressor(n_estimators = 100, random_state = 0) 
    regressor_2.fit(X_train_2, y_train_2)
    #sem3
    df3=df_pre.copy()
    df3.dropna(subset = ['1','2','3'], inplace=True)
    #print(df3)
    X_3=df3[['1','2']]
    y_3=df3['3']
    X_train_3, X_test_3, y_train_3, y_test_3 = train_test_split(X_3, y_3, test_size=0.33, random_state=100)
    regressor_3 = RandomForestRegressor(n_estimators = 100, random_state = 0) 
    regressor_3.fit(X_train_3, y_train_3)
    #sem4
    df4=df_pre.copy()
    df4.dropna(subset = ['1','2','3','4'], inplace=True)
    #print(df4)
    X_4=df4[['1','2','3']]
    y_4=df4['4']
    X_train_4, X_test_4, y_train_4, y_test_4 = train_test_split(X_4, y_4, test_size=0.33, random_state=100)
    regressor_4 = RandomForestRegressor(n_estimators = 100, random_state = 0) 
    regressor_4.fit(X_train_4, y_train_4)
    #sem5
    df5=df_pre.copy()
    df5.dropna(subset = ['1','2','3','4','5'], inplace=True)
    #print(df5)
    X_5=df5[['1','2','3','4']]
    y_5=df5['5']
    X_train_5, X_test_5, y_train_5, y_test_5 = train_test_split(X_5, y_5, test_size=0.33, random_state=100)
    regressor_5 = RandomForestRegressor(n_estimators = 100, random_state = 0) 
    regressor_5.fit(X_train_5, y_train_5)
    #sem6
    df6=df_pre.copy()
    df6.dropna(subset = ['1','2','3','4','5','6'], inplace=True)
    #print(df6)
    X_6=df6[['1','2','3','4','5']]
    y_6=df6['6']
    X_train_6, X_test_6, y_train_6, y_test_6 = train_test_split(X_6, y_6, test_size=0.33, random_state=100)
    regressor_6 = RandomForestRegressor(n_estimators = 100, random_state = 0) 
    regressor_6.fit(X_train_6, y_train_6)
    #sem7
    df7=df_pre.copy()
    df7.dropna(subset = ['1','2','3','4','5','6','7'], inplace=True)
    #print(df7)
    X_7=df7[['1','2','3','4','5','6']]
    y_7=df7['7']
    X_train_7, X_test_7, y_train_7, y_test_7 = train_test_split(X_7, y_7, test_size=0.33, random_state=100)
    regressor_7 = RandomForestRegressor(n_estimators = 100, random_state = 0) 
    regressor_7.fit(X_train_7, y_train_7)
    #sem8
    df8=df_pre.copy()
    df8.dropna(subset = ['1','2','3','4','5','6','7','8'], inplace=True)
    #print(df8)
    X_8=df8[['1','2','3','4','5','6','7']]
    y_8=df8['8']
    X_train_8, X_test_8, y_train_8, y_test_8 = train_test_split(X_8, y_8, test_size=0.33, random_state=100)
    regressor_8 = RandomForestRegressor(n_estimators = 100, random_state = 0) 
    regressor_8.fit(X_train_8, y_train_8)
    
def predict():
    global prediction_fig
    try:
        prediction_fig.destroy()
    except:pass
    global ls_sgpa , sgpa_curr ,strrno,flag_rno
    ls_sgpa=[]
    sgpa_curr=[]
    if (len(rno.get().strip())!=0):
        strrno=rno.get().upper()
        flag_rno=0
        print("Enrollment No.: "+strrno)
        dfrno=df_pre[df_pre['rno']==strrno]
        #print(dfrno['rno'].values)
        if (dfrno['rno'].values==strrno):
            flag_rno=1
            ls=[]
            #print(dfrno.values)
            for i in range(8):
                if (dfrno[str(i+1)].values>0):
                    ls.append(dfrno[str(i+1)].values)
                    ls_sgpa.append(ls[i][0])    
            sgpa_curr=ls_sgpa.copy()
        else:
             tk.messagebox.showinfo("ERROR!", "Data not found for "+strrno)
    else:
        flag_rno=0
        s1=texts1.get()
        s2=texts2.get()
        s3=texts3.get()
        s4=texts4.get()
        s5=texts5.get()
        s6=texts6.get()
        s7=texts7.get()
        s8=texts8.get()
        
        ls_sgpa=[]
        sgpa_curr=[]
        ls_s=[]
        ls_s.append(s1)
        ls_s.append(s2)
        ls_s.append(s3)
        ls_s.append(s4)
        ls_s.append(s5)
        ls_s.append(s6)
        ls_s.append(s7)
        ls_s.append(s8)
        
        for i in ls_s:
            if len(i.strip())>0:
                try:
                    if 0<float(i)<=10:
                        ls_sgpa.append(float(i))
                    else:
                        tk.messagebox.showinfo("ERROR!", "Enter Valid Data")
                except:
                    tk.messagebox.showinfo("ERROR!", "Enter Valid Data")
        sgpa_curr=ls_sgpa.copy()        
        
    if (len(ls_sgpa)==8):
        sem()
    elif(len(ls_sgpa)==7):
        sem8()
    elif(len(ls_sgpa)==6):
        sem7()
    elif(len(ls_sgpa)==5):
        sem6()
    elif(len(ls_sgpa)==4):
        sem5()
    elif(len(ls_sgpa)==3):
        sem4()
    elif(len(ls_sgpa)==2):
        sem3()
    elif(len(ls_sgpa)==1):
        sem2()
def sem():
    #print("sem")
    plt.close()
    plt.cla()
    plt.plot(['Sem 1','Sem 2','Sem 3','Sem 4','Sem 5','Sem 6','Sem 7','Sem 8'],ls_sgpa ,c='orange',marker='o',lw=2.5 ,label="Current")
    
    plt.legend(framealpha=1,frameon=True)
    plt.ylim(0,10)
    plt.ylabel('SGPA')
    plt.tight_layout()
    #plt.show()
    

    
    pre_img=Image.open('prediction1.jpg')
    pre_img=pre_img.resize((550,350),Image.ANTIALIAS)
    pre_image=ImageTk.PhotoImage(pre_img)
    

    prediction_fig=tk.Label(tab2,image=pre_image)
    prediction_fig.image=pre_image
    #prediction_fig.place(x=800,y=100)
    prediction_fig.grid(row=1,rowspan=25,column=4,padx=150)
            
def sem2():
    predict_2 =regressor_2.predict([ls_sgpa,])
    predict_2=round(predict_2[0],2)
    #print(predict_6)
    str_accuracy=str(regressor_2.score(X_test_2,y_test_2)*100)
    print("Sem 2")
    print("Prediction: "+ str(predict_2)+" SGPA")
    ls_sgpa.append(predict_2)
   
    sem3()
    
def sem3():
    predict_3 =regressor_3.predict([ls_sgpa,])
    predict_3=round(predict_3[0],2)
    #print(predict_6)
    str_accuracy=str(regressor_3.score(X_test_3,y_test_3)*100)
    print("Sem 3")
    print("Prediction: "+ str(predict_3)+" SGPA")
    ls_sgpa.append(predict_3)

    sem4()
def sem4():
    predict_4 =regressor_4.predict([ls_sgpa,])
    predict_4=round(predict_4[0],2)
    #print(predict_6)
    str_accuracy=str(regressor_4.score(X_test_4,y_test_4)*100)
    print("Sem 4")
    print("Prediction: "+ str(predict_4)+" SGPA")
    ls_sgpa.append(predict_4)

    sem5()
def sem5():
    predict_5 =regressor_5.predict([ls_sgpa,])
    predict_5=round(predict_5[0],2)
    #print(predict_6)
    str_accuracy=str(regressor_5.score(X_test_5,y_test_5)*100)
    print("Sem 5")
    print("Prediction: "+ str(predict_5)+" SGPA")
    ls_sgpa.append(predict_5)


    sem6()
def sem6():
    predict_6 =regressor_6.predict([ls_sgpa,])
    predict_6=round(predict_6[0],2)
    #print(predict_6)
    str_accuracy=str(regressor_6.score(X_test_6,y_test_6)*100)
    print("Sem 6")
    print("Prediction: "+ str(predict_6)+" SGPA")
    ls_sgpa.append(predict_6)
    
    sem7()
def sem7():
    predict_7 =regressor_7.predict([ls_sgpa,])
    predict_7=round(predict_7[0],2)
    #print(predict_7)
    str_accuracy=str(regressor_7.score(X_test_7,y_test_7)*100)
    print('Sem 7')
    print("Prediction: "+ str(predict_7)+" SGPA")
    ls_sgpa.append(predict_7)
    
    sem8()
    
def sem8():
    sem=[]
    for i in range(len(sgpa_curr)):
        sem.append("Sem "+str(i+1))
    predict_8 =regressor_8.predict([ls_sgpa,])
    predict_8=round(predict_8[0],2)
    #print(predict_6)
    str_accuracy=str(regressor_8.score(X_test_8,y_test_8)*100)
    print('Sem 8')
    print("Prediction: "+ str(predict_8)+" SGPA")
    ls_sgpa.append(predict_8)
    #print(sgpa_curr)
    if flag_rno==1:
        #print(strrno[6:8])
        rno=strrno[6:8]
        df=df_pre.copy()
        plt.close()
        plt.cla()
        plt.plot(sem,marker='.',c='green',lw=2.5,label='Batch Avg')
    else:
        plt.close()
        plt.cla()
    plt.plot(['Sem 1','Sem 2','Sem 3','Sem 4','Sem 5','Sem 6','Sem 7','Sem 8'],ls_sgpa ,marker='*',lw=2.0 ,label="Prediction")
    plt.plot(sem,sgpa_curr ,marker='o',lw=2.5,label='Current')
    plt.legend(framealpha=1,frameon=True)
    plt.ylim(0,10)
    plt.ylabel('SGPA')
    plt.tight_layout()
    plt.savefig('prediction1.jpg')
    #plt.show()
    

    
    pre_img=Image.open('prediction1.jpg')
    pre_img=pre_img.resize((550,350),Image.ANTIALIAS)
    pre_image=ImageTk.PhotoImage(pre_img)
    
    global prediction_fig
    prediction_fig=tk.Label(tab2,image=pre_image)
    prediction_fig.image=pre_image
    prediction_fig.grid(row=1,rowspan=25,column=4,padx=150)
       

   
root=tk.Tk()
frame = tk.Frame(root)
frame.pack()
root.title("NORTH CAMPUS,UNIVERSITY OF KASHMIR STUDENT RESULT PREDICTION")     

tab_parent = ttk.Notebook(root)
tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)
tab_parent.add(tab1, text="Result Analysis")
tab_parent.add(tab2, text="Result Prediction")


var = tk.IntVar()
label = tk.LabelFrame(tab1, text="Select Course:")
label.config(font=("Times New Roman", 26))
label.pack(fill="both")
R1 = tk.Radiobutton(label, text="B.E.     ", variable=var, value=0)
R1.config(font=("Times New Roman", 18))
R1.pack( anchor = CENTER)
R2 = tk.Radiobutton(label, text="B.Tech", variable=var, value=1)
R2.config(font=("Times New Roman", 18))
R2.pack( anchor = CENTER)

label1 = tk.LabelFrame(tab1, text="Select Sem:")
label1.config(font=("Times New Roman", 26))
label1.pack(fill="both")
num_sem = tk.Spinbox(label1, from_=1, to=8)
num_sem.config(font=("Times New Roman", 18))
num_sem.pack(anchor = CENTER )

label4=tk.LabelFrame(tab1,text="Choose File (for Enrollment No.)")
label4.config(font=("Times New Roman", 26))
label4.pack(fill="both")
button = tk.Button(label4,text ="Open")
button.config(font=("Times New Roman", 18))
button.pack(anchor = CENTER )


label_sub = tk.LabelFrame(tab1, text="Enter count of Subjects:")
label_sub.pack(fill="both")
label_sub.config(font=("Times New Roman", 26))
count_subjects = tk.Spinbox(label_sub, from_=10, to=11)
count_subjects.config(font=("Times New Roman", 18))
count_subjects.pack(anchor = CENTER)

button = tk.Button(tab1,text ="Submit")
button.config(font=("Times New Roman", 26))
button.pack(anchor = CENTER)

label_rno = tk.Label(tab2, text="Enrollment No.:")
label_rno.config(font=("Times New Roman", 26))
rno=tk.Entry(tab2)
rno.config(font=("Times New Roman", 20))

labelor = tk.Label(tab2, text="OR")
labelor.config(font=("Times New Roman", 26))

label_sem = tk.Label(tab2, text="Individual SGPA's:-")
label_sem.config(font=("Times New Roman", 24))


labels1 = tk.Label(tab2, text="Sem 1:")
texts1=tk.Entry(tab2)
labels2 = tk.Label(tab2, text="Sem 2:")
texts2=tk.Entry(tab2)
labels3 = tk.Label(tab2, text="Sem 3:")
texts3=tk.Entry(tab2)
labels4 = tk.Label(tab2, text="Sem 4:")
texts4=tk.Entry(tab2)
labels5 = tk.Label(tab2, text="Sem 5:")
texts5=tk.Entry(tab2)
labels6 = tk.Label(tab2, text="Sem 6:")
texts6=tk.Entry(tab2)
labels7 = tk.Label(tab2, text="Sem 7:")
texts7=tk.Entry(tab2)
labels8 = tk.Label(tab2, text="Sem 8:")
texts8=tk.Entry(tab2)
button_generate = tk.Button(tab2,text ="Generate")
button_generate.config(font=("Times New Roman", 26))
tab_parent.pack(expand=1,fill="both")

root.mainloop()
