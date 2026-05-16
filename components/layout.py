import streamlit as st


def apply_css():
    st.markdown(
        """
        <style>
        /* Main app */
        .stApp {
            background: #f4f7fb;
            color: #0f172a;
        }

        /* Main content spacing */
        .block-container {
            padding-top: 3rem;
            padding-bottom: 2rem;
            max-width: 1200px;
        }

        /* Sidebar */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0f172a 0%, #1e3a5f 100%);
            border-right: 1px solid rgba(255, 255, 255, 0.12);
        }

        /* Only make sidebar labels/headings white, NOT inputs/dropdowns */
        [data-testid="stSidebar"] label,
        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] h1,
        [data-testid="stSidebar"] h2,
        [data-testid="stSidebar"] h3 {
            color: #f8fafc !important;
        }

        /* Sidebar input labels */
        [data-testid="stSidebar"] .stTextInput label,
        [data-testid="stSidebar"] .stSelectbox label,
        [data-testid="stSidebar"] .stSlider label {
            color: #f8fafc !important;
            font-weight: 600;
        }

        /* Text input boxes */
        .stTextInput input {
            background-color: #ffffff !important;
            color: #111827 !important;
            border-radius: 10px !important;
            border: 1px solid #cbd5e1 !important;
        }

        .stTextInput input::placeholder {
            color: #6b7280 !important;
        }

        /* Selectbox closed state */
        div[data-baseweb="select"] > div {
            background-color: #ffffff !important;
            color: #111827 !important;
            border-radius: 10px !important;
            border: 1px solid #cbd5e1 !important;
        }

        div[data-baseweb="select"] span,
        div[data-baseweb="select"] input {
            color: #111827 !important;
        }

        div[data-baseweb="select"] svg {
            color: #111827 !important;
            fill: #111827 !important;
        }

        /* Selectbox dropdown menu */
        ul[role="listbox"] {
            background-color: #ffffff !important;
        }

        ul[role="listbox"] li,
        ul[role="listbox"] div,
        ul[role="listbox"] span {
            color: #111827 !important;
            background-color: #ffffff !important;
        }

        ul[role="listbox"] li:hover,
        ul[role="listbox"] div:hover {
            background-color: #e0f2fe !important;
            color: #111827 !important;
        }

        /* Slider */
        .stSlider [data-baseweb="slider"] {
            margin-top: 10px;
        }

        .stSlider [data-baseweb="slider"] div {
            color: #f8fafc !important;
        }

        /* Header */
        .main-title {
            font-size: 44px;
            font-weight: 800;
            color: #0f172a;
            margin-bottom: 6px;
            letter-spacing: -0.03em;
        }

        .subtitle {
            color: #475569;
            font-size: 17px;
            margin-bottom: 28px;
        }

        /* Metric cards */
        div[data-testid="stMetric"] {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            padding: 20px;
            border-radius: 18px;
            box-shadow: 0 10px 30px rgba(15, 23, 42, 0.08);
        }

        div[data-testid="stMetric"] label {
            color: #64748b !important;
            font-weight: 700;
        }

        div[data-testid="stMetricValue"] {
            color: #0f172a !important;
            font-weight: 800;
        }

        /* Headings */
        h1, h2, h3 {
            color: #0f172a;
            font-weight: 800;
        }

        /* Alerts */
        div[data-testid="stAlert"] {
            border-radius: 14px;
            border: none;
        }

        /* Dataframe */
        div[data-testid="stDataFrame"] {
            background: #ffffff;
            border-radius: 16px;
            border: 1px solid #e2e8f0;
            box-shadow: 0 10px 30px rgba(15, 23, 42, 0.08);
            padding: 8px;
        }

        /* Download button */
        .stDownloadButton button {
            background: #2563eb !important;
            color: white !important;
            border-radius: 12px !important;
            border: none !important;
            font-weight: 700 !important;
        }

        .stDownloadButton button:hover {
            background: #1d4ed8 !important;
            color: white !important;
        }

        /* Footer */
        .footer {
            text-align: center;
            color: #64748b;
            padding: 25px;
            font-size: 14px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


def render_header():
    st.markdown(
        """
        <div class="main-title">✈️ Real-Time Flight Tracker & Delay Analytics</div>
        <div class="subtitle">
            Live aviation dashboard for tracking flights, airport activity and delay patterns.
        </div>
        """,
        unsafe_allow_html=True
    )


def render_footer():
    st.markdown("---")
    st.markdown(
        """
        <div class="footer">
            Developed by <b>Avi Panchal</b> · Real-Time Flight Delay Analytics Dashboard
        </div>
        """,
        unsafe_allow_html=True
    )