import streamlit as st
from PIL import Image

# Configurações da página
st.set_page_config(page_title="Meu Currículo", layout="wide")

# ----- FOTO -----
imagem = Image.open("perfil.jpg")
st.image(imagem, width=150)

# ----- SOBRE MIM -----
st.title("Nayara Ventura Cândido")
st.subheader("Desenvolvedora em Formação")
st.write("""
Sou uma profissional dedicada, apaixonada por tecnologia, buscando oportunidades para aplicar meus conhecimentos em desenvolvimento web e análise de dados. Tenho facilidade com aprendizado rápido, trabalho em equipe e estou em constante evolução.
""")

st.markdown("📱 **Telefone:** (31) 99143-4003")
st.markdown("📧 **E-mail:** nayaravti.380@gmail.com")
st.markdown("🔗 **GitHub:** [github.com/nayvti380](https://github.com/nayvti380)")
st.markdown("🔗 **LinkedIn:** [linkedin.com/in/nayara-ventura-24986532b](https://www.linkedin.com/in/nayara-ventura-24986532b/)")

# ----- HABILIDADES -----
st.header("💡 Habilidades")
st.markdown("""
- Python
- HTML, CSS e JavaScript
- Streamlit
- Banco de Dados (MySQL, SQLite)
- Lógica de Programação
- Git e GitHub
""")

# ----- EXPERIÊNCIA PROFISSIONAL -----
st.header("🧰 Experiência Profissional")

st.subheader("Assistente Administrativo - Empresa F5 Informática")
st.markdown("""
- Atendimento ao cliente
- Emissão de relatórios
- Organização de documentos
""")

st.subheader("Estagiária em TI - F5 Informática")
st.markdown("""
- Suporte técnico
- Criação de planilhas automatizadas
- Manutenção de computadores
""")

# ----- EDUCAÇÃO -----
st.header("🎓 Educação")
st.markdown("""
- Graduação em Engenharia de Software – Universidade Anhanguera (5º Período, em andamento)
- Curso de Full Stack – Infinity School (em andamento)
- Curso de Data Science – Infinity School (em andamento)
- Curso de Inglês – EAD (em andamento)
- Curso de Manutenção de Computadores – F5 Informática (concluído)
- Curso de Transfer Learning – Infinity School (concluído)
- Curso de Sensores, Microcontroladores e Programação em Internet das Coisas – Anhanguera (concluído)
- Curso de Novos Desenvolvimentos em IoT – Anhanguera (concluído)
- Análise em Python – Anhanguera (concluído)
""")

# ----- IDIOMAS -----
st.header("🌐 Idiomas")
st.markdown("""
- Português (Nativo)
- Inglês (Intermediário)
""")
