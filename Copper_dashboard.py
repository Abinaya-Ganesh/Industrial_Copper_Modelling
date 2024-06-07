#================================ /   IMPORTING LIBRARIES   / ======================================#

#File handling libraries
import numpy as np
import pickle

#Dashboard Library
import streamlit as st


#================================ /   DASHBOARD SETUP   / ======================================#

#Page_configuration
st.set_page_config(
    page_title = 'Copper Modelling',
    page_icon = '🏭',
    layout = 'wide')

st.title(":blue[Industrial Copper Modelling Project⚛️]")

tab1,tab2 = st.tabs(['**Get Price**','**Get Status**'])

with tab1:
    st.subheader(":green[Get the predicted Selling price of Copper]")
    st.markdown("**Enter the following parameters to get the price**")

    status_options = ['Won', 'Draft', 'To be approved', 'Lost', 'Not lost for AM', 'Wonderful', 'Revised', 'Offered', 'Offerable']
    item_type_options = ['W', 'WI', 'S', 'Others', 'PL', 'IPL', 'SLAWR']
    country_options = [28., 25., 30., 32., 38., 78., 27., 77., 113., 79., 26., 39., 40., 84., 80., 107., 89.]
    application_options = [10., 41., 28., 59., 15., 4., 38., 56., 42., 26., 27., 19., 20., 66., 29., 22., 40., 25., 67., 79., 3., 99., 2., 5., 39., 69., 70., 65., 58., 68.]
    product_options=['611112', '611728', '628112', '628117', '628377', '640400', '640405', '640665', 
                    '611993', '929423819', '1282007633', '1332077137', '164141591', '164336407', 
                    '164337175', '1665572032', '1665572374', '1665584320', '1665584642', '1665584662', 
                    '1668701376', '1668701698', '1668701718', '1668701725', '1670798778', '1671863738', 
                    '1671876026', '1690738206', '1690738219', '1693867550', '1693867563', '1721130331', '1722207579']


    with st.form('Predict Selling Price Form '):
        try:
            col1,col2 = st.columns(2)
            with col1:
                st.write(' ')
                status = st.selectbox("**Select Status**", status_options, index=None, key='status')
                item_type = st.selectbox("**Select Item Type**", item_type_options, index=None, key='item_type')
                country = st.selectbox("**Select Country**", sorted(country_options), index=None, key='country')
                application = st.selectbox("**Select Application**", sorted(application_options), index=None, key='application')
                product_ref = st.selectbox("**Select Product Reference**", product_options, index=None, key='product_ref')

            with col2:
                st.write(' ')
                quantity_tons = st.text_input("**Enter the Quantity needed in tonnes**", placeholder='Eg:150', key='quantity')
                thickness = st.text_input("**Enter the Thickness needed**", placeholder='Eg:20', key='thickness')
                width = st.text_input("**Enter the Width needed**", placeholder='Eg:50', key='width')
                customer = st.text_input("**Enter the Customer ID**", placeholder='Eg:30408185', key='customer')
                st.write(' ')
                st.write(' ')
                submit_button = st.form_submit_button(label="**PREDICT SELLING PRICE**")

            if submit_button:
                with open("reg_model.pkl", 'rb') as file:
                    r_loaded_model = pickle.load(file)

                with open("scaler.pkl", 'rb') as f:
                    reg_scaler_loaded = pickle.load(f)

                with open("item_type.pkl", 'rb') as f:
                    reg_le_loaded = pickle.load(f)

                with open("status.pkl", 'rb') as f:
                    reg_ord_loaded = pickle.load(f)

                X_new = np.array([[np.log(float(quantity_tons)), status, item_type, application, np.log(float(thickness)), float(width), country, float(customer), int(product_ref)]])
                X_new[:,[2]]=reg_le_loaded.transform(np.ravel(X_new[:,[2]]))
                X_new[:,[1]]=reg_ord_loaded.transform(X_new[:,[1]])
                X_new = reg_scaler_loaded.transform(X_new)
                y_pred = r_loaded_model.predict(X_new)
                st.subheader(f"**:violet[PREDICTED SELLING PRICE:] ${np.around(np.exp(y_pred[0]),decimals=2)}**")
        except:
            st.error('**Please enter the details without including any special charaters or space**')

with tab2: 
    st.subheader(":green[Get the predicted Status of the Lead]")
    st.markdown("**Enter the following parameters to get the status**")

    with st.form("my_form1"):
        try:
            col1,col2=st.columns(2)
            with col1:
                st.write(' ')
                c_quantity_tons = st.text_input("**Enter the Quantity needed in tonnes**", placeholder='Eg:150', key='c_quantity')
                c_thickness = st.text_input("**Enter the Thickness needed**", placeholder = 'Eg:20', key='c_thickness')
                c_width = st.text_input("**Enter the Width needed**", placeholder='Eg:50', key='c_width')
                c_customer = st.text_input("**Enter the Customer ID**", placeholder='Eg:30408185', key='c_customer')
                c_price = st.text_input('Enter Selling Price in dollars:', placeholder='Eg:800', key = 'c_price')
                
            with col2:    
                st.write(' ')
                c_item_type = st.selectbox("**Select Item Type**", item_type_options, index=None, key='c_item_type')
                c_country = st.selectbox("**Select Country**", sorted(country_options), index=None, key='c_country')
                c_application = st.selectbox("**Select Application**", sorted(application_options), index=None, key='c_application')
                c_product_ref = st.selectbox("**Select Product Reference**", product_options, index=None, key='c_product_ref')
                st.write(' ')
                st.write(' ')       
                c_submit_button = st.form_submit_button(label="**PREDICT STATUS**")

                
            if c_submit_button:
                with open("clf_model.pkl", 'rb') as file:
                    c_loaded_model = pickle.load(file)

                with open("clf_scaler.pkl", 'rb') as f:
                    clf_scaler_loaded = pickle.load(f)

                with open("clf_le.pkl", 'rb') as f:
                    clf_le_loaded = pickle.load(f)

                X_new1 = np.array([[np.log(float(c_quantity_tons)),np.log(float(c_price)),np.log(float(c_thickness)),float(c_width),c_application,c_item_type,c_country,float(c_customer),int(c_product_ref)]])
                X_new1[:,[5]]=clf_le_loaded.transform(np.ravel(X_new1[:,[5]]))
                X_new1 = clf_scaler_loaded.transform(X_new1)
                y_pred1 = c_loaded_model.predict(X_new1)
                if y_pred1 == 1:
                    st.subheader('**:violet[PREDICTED STATUS:]** :green[WON]')
                else:
                    st.subheader('**:violet[PREDICTED STATUS:]** :red[LOST]')         
        except:
            st.error('**Please enter the details without including any special charaters or space**')