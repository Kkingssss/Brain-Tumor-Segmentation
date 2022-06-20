import streamlit as st 
from PIL import Image, ImageOps 
import time
from unittest import result
import numpy as np

st.sidebar.image("logo-image.png")
st.sidebar.header("AI BUILDERS")
def load_image(image_file):
    img = Image.open(image_file)
    return img

activities = ["About this project", "Start Segmentation"]
choice = st.sidebar.selectbox("Select Activty",activities)

if choice =='About this project' :
    st.subheader("About my project")
    st.title("Brain tumor segmentation")
    st.write("Artificial intelligence (AI) นั้นเริ่มมีบทบาทสำคัญต่อหลากหลายสาขาอาชีพ ซึ่งหนึ่งในนั้นก็คือหน่วยงานด้านการแพทย์ โดยได้มีการเปิดรับเอาเทคโนโลยี AI และ Robotics มาใช้ประโยชน์มากขึ้นเรื่อย ๆ เพื่อประหยัดเวลาและอำนวยความสะดวกให้กับบุคลากรทางการแพทย์มากยิ่งขึ้น")
    st.write("brain tumor segmentation ในโปรเจคนี้จะทำการแบ่งเป็น 3 ส่วน ซึ่งประกอบด้วย ")
    st.image("seg_picture.png")
    st.subheader("1.peritumoral edematous/invaded tissue")#1
    st.write("จากภาพแสดงด้วยสีเหลือง")
    st.subheader("2.necrotic tumor core")#2
    st.write("จากภาพแสดงด้วยสีฟ้า")
    st.subheader("3.GD-enhancing tumor")#3
    st.write("จากภาพแสดงด้วยสีเขียว")
    st.write("")
    st.write("โปรเจคชิ้นนี้จะไม่สามารถเกิดขึ้นได้หากปราศจากการสนับสนุนจากผู้สนับสนุนของโครงการ AI BUILDERS รวมถึงพี่ ๆ ทุกคนที่คอยดูแลเป็นอย่างดี ขอขอบคุณค่ะ")
    st.image("sponser.png")  
elif choice == "Start Segmentation": 
    st.subheader("please put your email ")
    title = st.text_input('Your email : ', '')
   
    st.subheader("please upload ")
    image_file = st.file_uploader("Upload Images", type=[".nrrd",".nii",".vti",".mhd"])
    if image_file is not None:
        # To See details 
       
        image_file.seek(0)
        file_details = {"filename":image_file.name, "filetype":image_file.type,"filesize":image_file.size}
        st.write('file details : ')
        st.write(file_details)
        st.write('โปรดรอสักพัก จะมีการตอบกลับไปทาง : ', title)
        st.write('ขอบคุณค่ะ')
    
        
checkpoint_path = ""           
st.sidebar.write('If you have encounter issues, please contact at nattawadee.lee@gmail.com')
    








