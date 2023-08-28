import streamlit as st
import streamlit.components.v1 as components


# Set page title
st.set_page_config(
    page_title="Lung Guardian | About Us",
    page_icon=":dna:",
    initial_sidebar_state="expanded",
)
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
img{border-radius: 10px;}
</style> """, unsafe_allow_html=True)
st.write('<style>div.row-widget.stMarkdown { font-size: 24px; }</style>', unsafe_allow_html=True)




# Define page layout
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
            left: 0px;
            position: fixed;
            background: -webkit-linear-gradient(0.25turn,#20D2FE, #5292FE);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        p{
            font-size: 2rem;
        }
    </style>
    <p id="effect">About Us</p>
    """,
  
)

st.image("https://media.sciencephoto.com/image/m2700339/800wm") 


st.write('''
         
The application of deep learning in detecting tuberculosis (TB) and pneumonia through X-ray images has revolutionized medical diagnosis. Leveraging the power of convolutional neural networks (CNNs), this technology has significantly improved the accuracy and efficiency of disease identification. By training on large datasets of annotated X-ray images, these models have learned to identify distinctive patterns associated with TB and pneumonia, enabling them to differentiate between normal and infected cases. The deep learning algorithms can precisely locate and highlight areas of concern in X-ray scans, aiding radiologists in their diagnoses. This innovation holds immense promise for early detection, particularly in regions with limited access to expert medical personnel. However, ethical considerations, ongoing refinement, and validation against diverse populations remain crucial to ensure the reliability and equitable distribution of this technology in the global fight against these respiratory diseases. 
    '''
)

