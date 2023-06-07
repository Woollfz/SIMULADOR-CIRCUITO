import streamlit as st

def main():
    V = st.text_input('Ingrese el voltaje de la fuente (V)', placeholder="12")
    R1 = st.text_input('Ingrese el valor de la resistencia 1 (ohmios)', placeholder='100')
    R2 = st.text_input('Ingrese el valor de la resistencia 2 (ohmios)', placeholder='200')

    if st.button('Calcular'):
        V = int(V)
        R1 = int(R1)
        R2 = int(R2)

        R_total = R1+R2
        I_total = V / R_total
        V1 = I_total * R1
        V2 = I_total * R2

        st.title("Resultados")
        st.subheader(f"Voltaje total en el circuito: {V} V")
        st.subheader(f"Corriente total del circuito: {I_total} A")
        st.subheader(f"Voltaje en la resistencia 1: {V1} V")
        st.subheader(f"Voltaje en la resistencia 2: {V2} V")

if _name_ == "_main_":
    main()
