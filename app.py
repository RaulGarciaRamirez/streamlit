import streamlit as st

def main():
    st.title("Convertidor de Texto a Mayúsculas")
    
    # Texto de entrada
    input_text = st.text_area("Ingrese su texto aquí:")
    
    # Botón para convertir a mayúsculas
    if st.button("Convertir a Mayúsculas"):
        output_text = input_text.upper()
        st.write("Texto convertido a mayúsculas:")
        st.write(output_text)

if __name__ == "__main__":
    main()
