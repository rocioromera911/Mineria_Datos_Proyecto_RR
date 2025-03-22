import streamlit as st

# ------------------ CONFIG ------------------
st.set_page_config(
    page_title="Portafolio de Rocío Romera",
    page_icon="🧠",
    layout="centered"
)

# ------------------ HEADER ------------------
st.title("👩‍💻 Rocío Romera")
st.subheader("RPA Developer | Data Scientist | AI & Automation")

st.markdown("""
Especialista en automatización de procesos, análisis de datos y estrategias comerciales para Retail y e-Commerce.

📍 *Argentina*  
📧 **rocio.romera828@gmail.com**  
[🔗 LinkedIn](https://linkedin.com/in/rocio-belen-romera-sily-a0942821b/) | [💻 GitHub](https://github.com/rocioromera911)  
[📄 Descargar CV](https://github.com/rocioromera911/Portafolio_RR/raw/main/CV_Rocio_Romera_RPA_DS_Retail_MercadoLibre.pdf)
""")

# ------------------ PROYECTOS ------------------
st.markdown("## 🚀 Proyectos Destacados")

with st.expander("🛒 Comparador de Precios en Supermercados"):
    st.write("""
    Scraping automatizado y visualización interactiva para detectar las mejores ofertas entre supermercados.
    
    🔧 Tecnologías: Python, Selenium/Playwright, Pandas, Streamlit
    """)
    st.link_button("Ver Código en GitHub", "https://github.com/rocioromera911/scraping-precios-supermercado")

with st.expander("🤖 SAP Notifier: Automatización de Firmas"):
    st.write("""
    Notifica automáticamente al siguiente aprobador cuando una orden de compra es firmada en SAP. Automatización 100% integrada con Outlook.

    🔧 Tecnologías: Python, SAP GUI Scripting, Outlook
    """)
    st.link_button("Ver Código en GitHub", "https://github.com/rocioromera911/sap-notifier-rpa")

with st.expander("🧠 Clasificación de Mensajes con NLP (Mercado Libre)"):
    st.write("""
    Modelo de IA que clasifica automáticamente preguntas de clientes según intención de compra y urgencia. Ideal para e-Commerce.

    🔧 Tecnologías: Python, TensorFlow, NLP, Pandas
    """)
    st.link_button("Ver Código en GitHub", "https://github.com/rocioromera911/nlp-mercado-libre")

# ------------------ PIE DE PÁGINA ------------------
st.markdown("""
---
📫 ¿Querés trabajar conmigo? ¡Estoy abierta a nuevas oportunidades!  
© 2025 Rocío Romera
""")
