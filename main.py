# Import Libraries
import streamlit as st
from st_aggrid import AgGrid
import os
os.environ["MODIN_ENGINE"] = "ray"
import modin.pandas as pd


from PIL import Image



# Set title of our Front web app
image = Image.open('image.png')
st.image(image, use_column_width=True)
st.title('Nilkamal MHE  Manual')


# Set Slide bar to chose between EDA and Visualization
def main():


    data_diesel1 = pd.read_excel('HangchaDiesel1_v2.xlsx')
    data_diesel2 = pd.read_excel('HangchaDiesel2_v2.xlsx')
    diesel= [data_diesel1,data_diesel2]
    data_diesel = pd.concat(diesel)
    #st.dataframe(data_electric.head(20))

    #OEM checkBox
    OEM = ['Hangcha']
    option=st.selectbox('Select OEM to work on:',OEM)

    #OEM subtype
    type = ['Electric', 'Diesel']
    option2 = st.selectbox('Select the Type of Machine:', type)
    if option2 == 'Electric':
        st.success('Success, Please wait...')
        data_electric = pd.read_excel("HangchaElectric_v2.xlsx")

        AgGrid(data_electric)





    elif option2=='Diesel':
        data_diesel1 = pd.read_excel('HangchaDiesel1_v2.xlsx')
        data_diesel2 = pd.read_excel('HangchaDiesel2_v2.xlsx')
        data_diesel3 = pd.read_excel('HangchaDiesel3_v2.xlsx')
        #diesel = [data_diesel1, data_diesel2]
        #data_diesel = pd.concat(diesel)

        AgGrid(data_diesel1)

        if st.checkbox('If the specific Data Was not fount try, Diesel File No 2'):
            AgGrid(data_diesel2)
        if st.checkbox('If the specific Data Was not fount try, Diesel File No 3'):
            AgGrid(data_diesel3)















if __name__ == '__main__':
    main()