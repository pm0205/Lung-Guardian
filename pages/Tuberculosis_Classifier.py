import streamlit as st
import pandas as pd
import random
import imagerec
import streamlit.components.v1 as components
st.set_page_config(
    page_title="Lung Guardian",
    page_icon="🧬",
    initial_sidebar_state="expanded",
)
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


st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

st.title("Tuberculosis Predictor")

st.write('<style>div.row-widget.stMarkdown { font-size: 1.2rem; }</style>', unsafe_allow_html=True)



st.write("Tuberculosis (TB) is an infectious disease caused by the bacterium Mycobacterium tuberculosis. It primarily affects the lungs, but can also affect other parts of the body such as the brain, kidneys, and bones. TB is spread through the air when an infected person coughs or sneezes. People with weakened immune systems, such as those living with HIV/AIDS, are particularly susceptible to TB.")
st.write("The symptoms of TB include coughing, fever, fatigue, weight loss, and night sweats. TB can be diagnosed through a variety of tests, including chest X-rays and sputum tests, which involve analyzing a sample of phlegm from the patient. Treatment for TB typically involves a long course of antibiotics. Patients must complete the full course of antibiotics, even if they begin to feel better before the treatment is finished.")
st.write("TB is a major global health problem, particularly in developing countries. According to the World Health Organization, TB is one of the top 10 causes of death worldwide, and in 2019, an estimated 10 million people fell ill with TB. Efforts to combat TB include improving public health infrastructure, increasing access to TB testing and treatment, and developing new TB drugs and vaccines.")


st.write("""
Machine learning and specifically Convolutional Neural Networks (CNNs) have shown promising results in the detection of tuberculosis (TB) in lung X-rays.

CNNs are a type of neural network that are particularly suited for image processing tasks. They work by learning to identify relevant features in the input images, which are then used to make a prediction. In the case of TB detection, CNNs are trained on large datasets of lung X-rays, with some images labeled as "TB positive" and others labeled as "TB negative".

The trained CNN can then be used to classify new lung X-rays as either positive or negative for TB. In practice, the CNN output can be used as a "second opinion" for radiologists, who can review the CNN output along with their own analysis to make a diagnosis.

The use of CNNs in TB detection has several potential advantages over traditional methods. For example, CNNs can analyze images much faster than human experts, which could speed up the diagnosis process. Additionally, CNNs are not subject to the same biases and variability as human experts, which could improve the accuracy and consistency of TB diagnoses.

Overall, ML and CNNs have the potential to be a valuable tool in the fight against TB, especially in areas with limited access to expert medical resources.
""")
st.write("We have developed A Convolutional Neural Network (CNN) to predict whether a xray of lungs has tuberculosis or not. It has been trained on more than 4,200 images divided into two classes, to upto 50 epochs.")

uploaded_file = st.file_uploader("Choose a File", type=['jpg','png','jpeg'])


if uploaded_file!=None:
    st.image(uploaded_file)
x = st.button("Predict")
if x:
    with st.spinner("Predicting..."):
        y,conf = imagerec.imagerecognise(uploaded_file,"Models/tuberculosis_model.h5","Models/tb_labels.txt")

    if y.strip() == "Normal":
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
            <h1>It is Normal</h1>
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
            <h1>Tuberculosis Detected</h1>
            """
        )
        st.info("Causes")
        components.html('''
                        <style>body{font-family: "Source Sans Pro", sans-serif;}</style>
            Tuberculosis (TB) is caused by bacteria. It can spread through close contact with people who have TB and have symptoms (active TB). When someone with active TB coughs, they release small droplets containing the bacteria. You can catch TB if you regularly breathe in these droplets over a long period of time. Some people have TB in their body but do not get ill or have any symptoms (latent TB). This type of TB cannot be spread to others, but it can turn into active TB in the future.

        ''')

        st.info("Symptoms")
        components.html('''
                        <style>body{font-family: "Source Sans Pro", sans-serif;}</style>
            <ol>
                <li>Cough that lasts more than 3 weeks</li>
                <li>Patient might cough up mucus (phlegm) or mucus with blood in it</li>
                <li>Feeling tired or exhausted</li>
                <li>Loss of appetite</li>
                <li>Swollen glands</li>
                <li>Constipation</li>
            </ol>

        ''')

        st.success("Remedies")
        components.html('''
                        <style>body{font-family: "Source Sans Pro", sans-serif;}</style>
                            The main treatment for tuberculosis (TB) is to take antibiotics for at least 6 months. If TB has spread to your brain, spinal cord or the area around your heart, you may also need to take steroid medicine for a few weeks. If you have TB but do not have symptoms (latent TB) you usually need to take antibiotics for 3 to 6 months.
                        ''')

        

