import os
from pathlib import Path
import pandas as pd
import streamlit as st
import plotly.express as px


st.set_page_config(page_title="Minh Tran's Portfolio", layout="wide", page_icon=":sparkles:")

def show_home():
    st.title("Minh Tran's Portfolio")
    st.markdown("Use the sidebar to navigate sections (Projects, Resume, Visualizations, About, Contact).")


def show_projects():
    st.header("Projects & Code")
    base_dir = Path(__file__).resolve().parents[1]  # goes up from streamlit_sample to python_projects
    if not base_dir.exists():
        st.error(f"Projects directory not found: {base_dir}")
        return

    files = sorted([p for p in base_dir.rglob("*.*") if p.suffix in (".py", ".md")])
    if not files:
        st.info("No `.py` files found under the projects folder.")
        return

    for f in files:
        with st.expander(f.name):
            try:
                if f.suffix == ".py":
                    text = f.read_text(encoding="utf-8")
                    st.code(text, language="python")
                elif f.suffix == ".md":
                    text = f.read_text(encoding="utf-8")
                    st.markdown(text)
            except Exception as e:
                st.write("Could not read file:", e)


def show_visualizations():
    st.header("CDC Covid Public Health Data Visualizations")
    csv_path = "CDC_public_health_data/VDH-COVID-19-PublicUseDataset-EventDate.csv"
    if csv_path:
        try:
            df = pd.read_csv(csv_path)
            if 'Event Date' in df.columns:
                df['Event Date'] = pd.to_datetime(df['Event Date'], errors='coerce')
                grouped = df.groupby(df['Event Date'].dt.date).sum(numeric_only=True)
                st.dataframe(grouped.tail(10))
                if 'Number of Cases' in grouped.columns:
                    st.plotly_chart(px.line(grouped, y='Number of Cases', title='Event Date vs. Number of Cases'))
                if 'Number of Deaths' in grouped.columns:
                    st.plotly_chart(px.line(grouped, y='Number of Deaths', title='Event Date vs. Number of Deaths'))
            else:
                st.dataframe(df.head())
        except Exception as e:
            st.error(f"Failed to load CSV: {e}")
    else:
        st.info("Sample CSV not found. Upload a CSV with an `Event Date` column to visualize.")
        uploaded = st.file_uploader("Upload CSV", type=["csv"])
        if uploaded is not None:
            df = pd.read_csv(uploaded)
            st.dataframe(df.head())

def show_resume():
    st.pdf("resume/MinhTran_Resume.pdf", height=800)

def show_contact():
    st.header("Contact")
    st.markdown("- Email: `minhtraann@yahoo.com`")
    st.markdown("- Phone Number: `703-626-8840`")
    st.markdown("- GitHub: https://github.com/Minhereno")
    st.markdown("- LinkedIn: https://www.linkedin.com/in/minh-tran-a5206616a/")

def main():
    menu = st.sidebar.selectbox("Section", ["Home", "Resume", "Projects", "CDC Covid Public Health Data Visualizations", "Contact"])
    if menu == "Home":
        show_home()
    elif menu == "Resume":
        show_resume()
    elif menu == "Projects":
        show_projects()
    elif menu == "CDC Covid Public Health Data Visualizations":
        show_visualizations()
    elif menu == "Contact":
        show_contact()


if __name__ == "__main__":
    main()
