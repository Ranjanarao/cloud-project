
import streamlit as st

st.set_page_config(
    page_title="AI Career Assistant",
    page_icon="🎓",
    layout="wide"
)

st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: #f5f7fb;
    color: #172554;
}

.block-container {
    padding-top: 2rem;
}

/* General text */
.stApp p,
.stApp h1,
.stApp h2,
.stApp h3 {
    color: #172554;
}

/* Header */
.header {
    background: #172554;
    padding: 25px;
    border-radius: 12px;
    color: white;
    text-align: center;
}

.header h1 {
    color: white !important;
    margin-bottom: 5px;
}

.header p {
    color: #dbeafe !important;
}

/* Module cards */
.card {
    background: white;
    padding: 18px 12px;
    border-radius: 12px;
    border: 1px solid #dce3ed;
    min-height: 175px;
    text-align: center;
    margin-bottom: 12px;
}

.card h3 {
    color: #172554 !important;
    font-size: 17px;
}

.card p {
    color: #475569 !important;
    font-size: 13px;
}

/* Bottom sections */
.section {
    background: white;
    padding: 18px;
    border: 1px solid #dce3ed;
    border-radius: 12px;
}

.section h3 {
    color: #172554 !important;
}

.section p {
    color: #475569 !important;
}

/* Footer */
.footer {
    text-align: center;
    color: #64748b;
    padding: 10px;
}

</style>
""", unsafe_allow_html=True)


# Header
st.markdown("""
<div class="header">
<h1>AI CAREER ASSISTANT</h1>
<p>Your Smart Partner for Career Growth and Placement Preparation</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# Welcome section
st.subheader("Welcome to AI Career Assistant 👋")

st.write(
    "An AI-powered platform designed to help students "
    "with career planning, placement preparation and resume improvement."
)

# Dashboard metrics
c1, c2, c3 = st.columns(3)

c1.metric("Available Modules", "5")
c2.metric("AI Technology", "Llama 3.1")
c3.metric("Platform", "Streamlit")

st.divider()

# Available modules
st.subheader("Explore Our Modules")

modules = [
    ("💬", "Career Chat",
     "Get AI-powered answers to your career-related questions."),

    ("🗺️", "Career Roadmap",
     "Generate a learning roadmap based on your career goals."),

    ("📊", "Placement Predictor",
     "Get placement guidance based on CGPA and technical skills."),

    ("🎯", "Interview Generator",
     "Generate technical interview questions and answers."),

    ("📄", "Resume Analyzer",
     "Analyze your resume and identify missing skills and keywords.")
]

# Module navigation
if "selected_module" not in st.session_state:
    st.session_state.selected_module = None

cols = st.columns(5)

for col, module in zip(cols, modules):
    icon, title, description = module

    with col:
        st.markdown(f"""
        <div class="card">
            <div style="font-size:32px">{icon}</div>
            <h3>{title}</h3>
            <p>{description}</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Open Module", key=f"open_{title}",
                     use_container_width=True):
            st.session_state.selected_module = title
            st.rerun()

# Display selected module
if st.session_state.selected_module:
    st.divider()
    st.subheader(st.session_state.selected_module)

    st.info(
        f"You have opened the {st.session_state.selected_module} module."
    )

    if st.button("Back to Home"):
        st.session_state.selected_module = None
        st.rerun()

st.divider()

# Bottom sections
left, right = st.columns(2)

with left:
    st.markdown("""
    <div class="section">
    <h3>🚀 How It Works</h3>
    <p>1. Select your required module.</p>
    <p>2. Enter your information.</p>
    <p>3. AI processes your request.</p>
    <p>4. Get personalized guidance and results.</p>
    </div>
    """, unsafe_allow_html=True)

with right:
    st.markdown("""
    <div class="section">
    <h3>💻 Technology Stack</h3>
    <p>• Python Programming</p>
    <p>• Streamlit Framework</p>
    <p>• Hugging Face API</p>
    <p>• Llama 3.1 8B Instruct</p>
    <p>• PyPDF and Python-dotenv</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# Footer
st.markdown("""
<div class="footer">
AI Career Assistant | Developed by Ranjana Rao
<br>
Computer Science & Engineering
</div>
""", unsafe_allow_html=True)

