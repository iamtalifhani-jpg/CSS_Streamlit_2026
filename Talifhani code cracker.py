import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Researcher Profile")

# Collect basic information
name = "Rerani Talifhani"
field = "Pharmacology"
institution = "Sefako Makgatho Health Sciences University"

# DISPLAY
st.subheader("Where research meets excellence")
st.subheader("Pharmacology And Therapeutics")



     # open an image
     # from a local file
    
image="My AI IMAGE.png"
st.image("My AI IMAGE.png")
    
   
st.title("Talifhani Rerani")
st.subheader("Research Scientist | MSc Pharmacology")

st.write("""
 I am a researcher specializing in medicinal plants, zoological research,
 and bioactive natural compounds. My work focuses on improving our health care sectors as far as diabetes is concerned. Synthetic medication is toxic and hence exploring natural remedies and herbs is a key area of interest to find natural alternatives.
 and sustainable agriculture through molecular and biochemical approaches.
 """)

st.markdown("**Research Interests:**")
st.markdown("""
 - Plant secondary metabolites  
 - Antidiabetic phytochemicals  
 - Enzyme assays  
 - Medicinal pants
 - Sustainable agriculture 
 - Molecular biology
 - Zoological research 
 """)
 # make tabs for each section
tab1, tab2, tab3, = st.tabs(["🔬 Research",  "📊 Projects", "📬 Contact"])

# Add a section for Research projects
st.header("Research projects")
st.subheader("Determination of effective herbal dosage against type 2 diabetes mellitus using herbal plants")
st.write("I have engaged in an antidiabetic study focusing on finding  herbal alternatives towards the current battle with diabetes.This study aimed at finding a dose that had desired effect in inhibitibg key digestive enzymes known as salivary amylase and alpha glucosidase enzyme. The plants of interest used in the study were: Aloe spp, Hemero spp and Drimia spp. Currently, the research is till undergoing with satisfying results that could be a breakthrough for diabetic patients.I believe that the success of this research would make a huge impact in our country South Africa our land."  )
st.subheader("Molecular surveillance of tick-borne Rickettsia and Erhlichia in domestic animals in the rural areas of Elim, Limpopo")
st.write("This research was aimed at investigating major pathogones  carried by ticks in domisticated animals. Screening involved the use of PCR and gel electrophoresis in order to visualise DNA bands. The study was concluded and none of the pathogens being screened were present. Although none of the pathogens of interest were found, this does not entail that tick-borne pathogens do not exist but were not inclusive to the study")


st.set_page_config (layout="centered")
st.markdown("""
<style>
.stApp {
    background-color: #0b1f3a;  /* deep academic dark blue */
    color: white;
}

/* Keep content nicely centered */
.block-container {
    max-width: 900px;
    padding-top: 2rem;
}

/* Optional: make headers a biotech blue */
h1, h2, h3 {
    color: #66d9ff;
}
</style>
""", unsafe_allow_html=True)


import streamlit as st

st.set_page_config(layout="centered")

# ---- DARK BLUE BACKGROUND ----
st.markdown("""
<style>
.stApp {
    background-color: #0b1f3a;
    color: white;
}

.block-container {
    max-width: 900px;
    padding-top: 2rem;
}

/* Card look */
.card-header {
    background-color: #102a4d;
    padding: 15px 20px;
    border-radius: 12px;
    margin-bottom: 8px;
    font-weight: bold;
    font-size: 18px;
    color: #66d9ff;
    border: 1px solid rgba(255,255,255,0.08);
}
</style>
""", unsafe_allow_html=True)

st.title("🔬 Research Focus Areas")

# import streamlit as st

# ---- PAGE STYLE (NORMAL WIDTH) ----
st.set_page_config(layout="centered")

# ---- DARK BIOTECH BACKGROUND ----
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #040a14, #0b2342);
    color: white;
}

/* Center content and control width */
.block-container {
    max-width: 900px;
    padding-top: 2rem;
}

/* Card styling */
.card {
    background-color: #0f2b4c;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.4);
    transition: transform 0.2s ease-in-out;
    margin-bottom: 20px;
}

.card:hover {
    transform: scale(1.03);
}

.card-title {
    font-size: 20px;
    font-weight: bold;
    color: #66d9ff;
    margin-bottom: 10px;
}

.card-text {
    font-size: 14px;
    color: #e8f6ff;
}
</style>
""", unsafe_allow_html=True)

st.title("🔬 Research Focus Areas")

# ---- FUNCTION TO CREATE A CARD ----
def research_card(title, description):
    st.markdown(f"""
    <div class="card">
        <div class="card-title">{title}</div>
        <div class="card-text">{description}</div>
    </div>
    """, unsafe_allow_html=True)

# ---- CARDS (STACKED FOR CENTERED LAYOUT) ----
research_card("Plant Secondary Metabolites",
              "Study of bioactive compounds produced by plants and their pharmaceutical potential.")

research_card("Antidiabetic Phytochemicals",
              "Isolation and screening of plant compounds with blood-glucose-lowering properties.")

research_card("Enzyme Assays",
              "Biochemical evaluation of enzyme inhibition and metabolic pathways.")

research_card("Medicinal Plants",
              "Ethnobotanical and pharmacological investigation of traditional medicinal species.")

research_card("Sustainable Agriculture",
              "Eco-friendly crop production and soil health improvement strategies.")

research_card("Molecular Biology",
              "Genetic and cellular analysis techniques applied to plant and animal systems.")

research_card("Zoological Research",
              "Biological and ecological studies of animal species and biodiversity.")



# Add a contact section
st.header("Contact Information")
email = "iamtalifhani@gmail.com"
st.write(f"You can reach {name} at {email}.")