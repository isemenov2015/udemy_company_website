import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

st.title('Best Company')
content = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

Mi quis hendrerit dolor magna eget est lorem ipsum dolor. 
Adipiscing at in tellus integer feugiat scelerisque. 

Velit scelerisque in dictum non consectetur a erat nam. 
Lacus vel facilisis volutpat est velit egestas dui id. Elit ut aliquam purus sit amet luctus venenatis lectus magna. 
Iaculis eu non diam phasellus vestibulum lorem sed. Malesuada proin libero nunc consequat interdum. 

Ut consequat semper viverra nam libero. Tristique senectus et netus et malesuada fames ac turpis. 
Sit amet nisl suscipit adipiscing bibendum est ultricies. Lectus arcu bibendum at varius vel pharetra. 

Auctor augue mauris augue neque gravida. Ultrices gravida dictum fusce ut. Et ligula ullamcorper malesuada proin libero nunc consequat.
Lobortis mattis aliquam faucibus purus. Porttitor massa id neque aliquam vestibulum.
"""
st.write(content)
st.subheader('Our team')

col1, col2, col3 = st.columns(3)

df = pd.read_csv('data.csv')

with col1:
    for index, row in df[:(len(df) // 3)].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image('images/' + row['image'])

with col2:
    for index, row in df[(len(df) // 3):(2*(len(df) // 3))].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image('images/' + row['image'])

with col3:
    for index, row in df[2*(len(df) // 3):].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image('images/' + row['image'])
