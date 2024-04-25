import streamlit as st

def main():
    st.title("Convertidor de Texto con Formato")
    
    # Texto de entrada
    input_text = st.text_area("Ingrese su texto aquí:")
    
    # Opciones de formato
    italic = st.checkbox("Cursiva")
    bold = st.checkbox("Negrita")
    underline = st.checkbox("Subrayado")
    
    # Aplicar formato al texto
    formatted_text = input_text
    if italic:
        formatted_text = f"*{formatted_text}*"
    if bold:
        formatted_text = f"**{formatted_text}**"
    if underline:
        formatted_text = f"__{formatted_text}__"
    
    # Botón para convertir a mayúsculas
    if st.button("Aplicar Formato"):
        st.write("Texto con formato aplicado:")
        st.write(formatted_text)

if __name__ == "__main__":
    main()
