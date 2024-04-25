import streamlit as st

def main():
    st.title("Convertidor de Texto con Formato")
    
    # Texto de entrada
    input_text = st.text_area("Ingrese su texto aquí:")
    
    # Opciones de formato
    italic = st.checkbox("Cursiva")
    bold = st.checkbox("Negrita")
    underline = st.checkbox("Subrayado")
    
    # Color del texto
    color = st.color_picker("Color del Texto", "#000000")
    
    # Aplicar formato al texto
    formatted_text = input_text
    if italic:
        formatted_text = f"*{formatted_text}*"
    if bold:
        formatted_text = f"**{formatted_text}**"
    if underline:
        formatted_text = f"__{formatted_text}__"
    
    # Convertir a mayúsculas
    formatted_text = formatted_text.upper()
    
    # Aplicar color al texto
    formatted_text = f'<span style="color:{color}">{formatted_text}</span>'
    
    # Botón para mostrar el texto con formato
    if st.button("Mostrar Texto con Formato"):
        st.markdown(formatted_text, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
