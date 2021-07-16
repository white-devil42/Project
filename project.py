import streamlit as st
import pickle
from sklearn.preprocessing import LabelEncoder
st.header("Titanic")

model = open('log.pkl', 'rb')
log_reg = pickle.load(model)
model.close()

model = open('svm.pkl', 'rb')
svm = pickle.load(model)
model.close()

model = open('dtree.pkl', 'rb')
dtree = pickle.load(model)
model.close()

model = open('rf.pkl', 'rb')
rf = pickle.load(model)
model.close()


#encoders
pkl_file = open('Sex_encoder.pkl', 'rb')
Sex_encoder = pickle.load(pkl_file) 
pkl_file.close()

pkl_file = open('Embarked_encoder.pkl', 'rb')
Embarked_encoder = pickle.load(pkl_file) 
pkl_file.close()

Pclass=st.selectbox('Pclass',('1', '2','3'))
Sex=st.selectbox('Sex',('male', 'female'))
Age = st.text_input("Age")
SibSp=st.selectbox('SibSp',('1', '2','3','4','5'))
Parch=st.selectbox('Pclass',('1', '2','3','4','5','6'))
Fare=st.text_input("Fare")
Embarked=st.selectbox('Pclass',('S', 'C','Q','Unknown'))
submit = st.button('Check')


if submit:
    with st.spinner("Checking"):
        Pclass=int(Pclass)
        Sex=Sex_encoder.transform([Sex])[0]
        Fare=int(Fare)
        Age=int(Age)
        try:
            if Age<512 and Age>=0 :
                pass
            else:
                st.error('Age out of Limits')
        except:
            st.error('Enter valid Age')

        SibSp=int(SibSp)
        Parch=int(Parch)
        try:
            if Fare<512 and Fare>=0 :
                pass
            else:
                st.error('Fare out of Limits')
        except:
            st.error('Enter valid Fare')

        Embarked=Embarked_encoder.transform([Embarked])[0]
        result_log = log_reg.predict([[Pclass,Sex,Age,SibSp,Parch,Fare,Embarked]])
        result_svm=svm.predict([[Pclass,Sex,Age,SibSp,Parch,Fare,Embarked]])
        result_dtree=dtree.predict([[Pclass,Sex,Age,SibSp,Parch,Fare,Embarked]])
        result_rf=rf.predict([[Pclass,Sex,Age,SibSp,Parch,Fare,Embarked]])
        Results=[result_log,result_svm,result_dtree,result_rf]
        for i in Results:
            if i ==1:
                st.write('Will Survive')
            else:
                st.write('Will not Survive')
