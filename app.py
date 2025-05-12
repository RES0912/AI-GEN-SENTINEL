import numpy as np
import pandas as pd
import streamlit as st

def predict_disease_from_input(hematocrit, hemoglobin, mch, mchc, mcv, wbc, neutrophils, lymphocytes, monocytes, eosinophils, basophils):
    disease_prediction = np.random.choice(['Disease A', 'Disease B', 'Healthy'])
    return f"Based on the inputs, the possible disease is: {disease_prediction}"

def main():
    
    st.image("dna.png", width=500)

    st.markdown("""
    <style>
        .stButton > button {
            background-color: #FFFFFF;
            color: Blue;
            padding: 10px 24px;
            border: none;
            cursor: pointer;
            border-radius: 12px;
            font-size: 16px;
        }
        .stButton > button:hover {
            background-color: #FFFFFF;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("Enter the screening data to get possible disease predictions.")

    hematocrit = st.number_input("Hematocrit (%)", 0.0, 100.0, 45.0, 0.1)
    hemoglobin = st.number_input("Hemoglobin (g/dL)", 0.0, 100.0, 15.0, 0.1)
    mch = st.number_input("MCH (pg)", 0.0, 100.0, 30.0, 0.1)
    mchc = st.number_input("MCHC (g/dL)", 0.0, 100.0, 35.0, 0.1)
    mcv = st.number_input("MCV (fL)", 0.0, 100.0, 90.0, 0.1)
    wbc = st.number_input("White Cell Count (×10⁹/L)", 0.0, 100.0, 7.0, 0.1)
    neutrophils = st.number_input("Neutrophils (%)", 0.0, 100.0, 60.0, 0.1)
    lymphocytes = st.number_input("Lymphocytes (%)", 0.0, 100.0, 30.0, 0.1)
    monocytes = st.number_input("Monocytes (%)", 0.0, 100.0, 6.0, 0.1)
    eosinophils = st.number_input("Eosinophils (%)", 0.0, 100.0, 2.0, 0.1)
    basophils = st.number_input("Basophils (%)", 0.0, 100.0, 1.0, 0.1)

    if st.button("Predict Disease"):
        result = predict_disease_from_input(
            hematocrit, hemoglobin, mch, mchc, mcv, wbc,
            neutrophils, lymphocytes, monocytes, eosinophils, basophils
        )
        st.subheader("Prediction Result:")
        st.write(result)

        st.markdown("### Input Data Visualization")
        input_data = {
            'Hematocrit': hematocrit, 'Hemoglobin': hemoglobin, 'MCH': mch, 
            'MCHC': mchc, 'MCV': mcv, 'White Cell Count': wbc, 
            'Neutrophils': neutrophils, 'Lymphocytes': lymphocytes, 
            'Monocytes': monocytes, 'Eosinophils': eosinophils, 'Basophils': basophils
        }
        input_df = pd.DataFrame(input_data, index=[0])
        st.write(input_df)
        st.bar_chart(input_df.T, use_container_width=True)

if __name__ == "__main__":
    main()
