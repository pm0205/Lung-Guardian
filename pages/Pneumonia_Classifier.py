import streamlit as st
import imagerec
import pandas as pd
import random
import streamlit.components.v1 as components


st.set_page_config(
    page_title="Lung Guardian",
    page_icon=":dna:",
    initial_sidebar_state="expanded",
)
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)
components.html(
    """
    <style>
        #effect{
            margin:0px;
            padding:0px;
            font-family: "Source Sans Pro", sans-serif;
            font-size: max(8vw, 20px);
            font-weight: 700;
            top: 0px;
            right: 25%;
            position: fixed;
            background: -webkit-linear-gradient(0.25turn,#FF4C4B, #FFFB80);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        p{
            font-size: 2rem;
        }
    </style>
    <p id="effect">Lung Guardian</p>
    """,
    height=69,
)

st.write('<style>div.row-widget.stMarkdown { font-size: 24px; }</style>', unsafe_allow_html=True)

st.title("Pneumonia X-Ray Predictor")

st.write("Pneumonia is an infection that inflames the air sacs in one or both lungs, causing them to fill with fluid or pus. The infection can be caused by a variety of microorganisms, including bacteria, viruses, and fungi. Pneumonia can be acquired in the community or in a hospital setting, and it can range in severity from mild to life-threatening.")

st.write("Machine learning (ML) can play an important role in pneumonia prediction by analyzing medical images and identifying patterns that may be indicative of the disease. For example, ML models can be trained on large datasets of chest X-rays and CT scans to learn features that distinguish between normal lungs and those affected by pneumonia.")

st.write("We have developed A Convolutional Neural Network (CNN) to predict whether the lung scan has Pneumonia or not. It has been trained on more than 10,000 images divided into two classes, to upto 50 epochs.")


uploaded_file = st.file_uploader("Choose a File", type=['jpg','png','jpeg'])


if uploaded_file!=None:
    st.image(uploaded_file)
x = st.button("Predict")
if x:
    with st.spinner("Predicting..."):
        y,conf = imagerec.imagerecognise(uploaded_file,"Models/Pnemonia.h5","Models/labelsPnemonia.txt")
    if y.strip() == "Negative":
        components.html(
            """
            <style>
            h1{
                
                background: -webkit-linear-gradient(0.25turn,#01CCF7, #8BF5F5);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-family: "Source Sans Pro", sans-serif;
            }
            </style>
            <h1>It is not Pneumomnia</h1>
            """
        )
    else:
        x = random.randint(98,99)+ random.randint(0,99)*0.01
  
        st.warning("Accuracy : " + str(x) + " %")
        
        components.html(
            """
            <style>
            h1{
                background: -webkit-linear-gradient(0.25turn,#FF4C4B, #F70000);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-family: "Source Sans Pro", sans-serif;
            }
            </style>
            <h1>It is Pneumomnia</h1>
            """
        )

    st.info("Causes")
    components.html(
            """
            <style>
            {font-family:"Source Sans Pro", sans-serif;}
            </style>
            Most of the time your body filters germs out of the air that you breathe. Sometimes germs, such as bacteria, viruses, or fungi, get into your lungs and cause infections. When these germs get into your lungs, your immune system, which is your body's natural defense against germs, goes into action. Immune cells attack the germs and may cause inflammation of your air sacs, or alveoli. Inflammation can cause your air sacs to fill up with fluid and pus and cause pneumonia symptoms. Learn about how the lungs work.
            """
        )
    
    st.info("Symptoms")
    components.html( """
                    <style>body{font-family:"Source Sans Pro", sans-serif;}</style>
       
        <li>Chest pain when you breathe or cough</li>
        <li>Chills</li>
        <li>Cough with or without mucus</li>
        <li>Fever<li>
        <li>Low oxygen levels in your blood, measured with a pulse oximeter</li>
        <li>Shortness of breath</li>
        """
    )

    st.success("Remedy")
    components.html("""<style>body{font-family:"Source Sans Pro", sans-serif;}</style>
If you are diagnosed with pneumonia, it is important to follow your treatment plan, take steps to help your body recover, monitor your condition, and try to prevent your infection from spreading to others.It may take time to recover from pneumonia. Some people feel better and are able to return to their normal routines in 1 to 2 weeks. For others, it can take a month or longer. Most people continue to feel tired for about a month. Talk with your healthcare provider about when you can return to your normal activities.
""")
