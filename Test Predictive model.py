# -*- coding: utf-8 -*-
"""
Created on Wed May  4 10:27:36 2022

@author: RuJ
"""
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from pycaret.regression import *
import pickle
import streamlit as st

loaded_model = pickle.load(open("C:/Users/RuJ/Desktop/Deploy ML/model_xgb_v3.pkl","rb"))
model = load_model("C:/Users/RuJ/Desktop/Deploy ML/model_xgb_v3")

def housePricePrediction(input_data):
    # convert to data frame
    input_data_df = pd.DataFrame(input_data)
    model_prediction = predict_model(model,input_data_df)
    y_pred = model_prediction['Label']
    price = '{:,}'.format(y_pred[0])
    return 'estimated price:  ' + price + ' THB'


def main():
    # for title
    st.title('House price prediction model')
    
    # getting input data from user
    District = st.selectbox('District',['คลองสาน','คลองสามวา','คลองเตย','คันนายาว','จตุจักร','จอมทอง','ดอนเมือง'
      ,'ดินแดง','ดุสิต','ตลิ่งชัน','ทวีวัฒนา','ทุ่งครุ','ธนบุรี','บางกอกน้อย','บางกอกใหญ่','บางกะปิ','บางขุนเทียน','บางคอแหลม','บางซื่อ'
      ,'บางนา','บางบอน','บางพลัด','บางรัก','บางเขน','บางแค','บึงกุ่ม','ปทุมวัน','ประเวศ','ป้อมปราบศัตรูพ่าย','พญาไท','พระนคร'
      ,'พระโขนง','ภาษีเจริญ','มีนบุรี','ยานนาวา','ราชเทวี','ราษฎร์บูรณะ','ลาดกระบัง','ลาดพร้าว','วังทองหลาง','วัฒนา','สวนหลวง'
      ,'สะพานสูง','สัมพันธวงศ์','สาทร','สายไหม','หนองจอก','หนองแขม','หลักสี่','ห้วยขวาง'])
    Latitude = st.text_input('Latitude (must be in range of 13.88-13.94)')
    Longitude = st.text_input("Longitude (must be in range of 100.39-100.69)")
    AreaUsable = st.text_input('Area usable')
    Bathroom = st.text_input('Bathroom')
    Bedroom = st.text_input('Bedroom')
    Floor = st.text_input('floor')
    Parking = st.text_input('Parking')
    st.write('Convenience')
    Fitness = st.checkbox('Fitness')
    Park = st.checkbox('Park')
    Pool = st.checkbox('Pool')
    FirstHand = st.checkbox('First hand')
    ทาวน์โฮม = 0
    บ้านเดี่ยว = 0
    house_categories = st.radio('House Categories',['Townhome','Detached house'])
    if house_categories == 'Townhome':
        ทาวน์โฮม = 1
    else:
        บ้านเดี่ยว = 1
    
    
    
    
    

    # code for prediction
    diagnosis = ''
    if st.button('Predict house price'):
        tmp_dict = {'District':District,'Latitude':Latitude,'Longitude':Longitude,'AreaUsable':AreaUsable
                    ,'Bathroom':Bathroom,'Bedroom':Bedroom,'Floor':Floor,'PriceStart':0,'Parking':Parking
                    ,'Fitness':Fitness,'Park':Park,'Pool':Pool,'FirstHand':FirstHand,'ทาวน์โฮม':ทาวน์โฮม
                    ,'บ้านเดี่ยว':บ้านเดี่ยว}
        diagnosis = housePricePrediction([tmp_dict])
    
    st.success(diagnosis)
    
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    