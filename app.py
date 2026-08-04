import streamlit as st
from src.predictor import get_suggestions

st.set_page_config(
    page_title="Word Prediction",
    page_icon="🔍",
    layout="wide"
)

st.markdown("""
<style>

.stApp{
    background: linear-gradient(to right,#eef5ff,#dbeafe);
}

/* Hide Streamlit Menu */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Title */
.title{
    text-align:center;
    font-size:55px;
    font-weight:700;
    color:#1565C0;
    margin-top:20px;
}

.subtitle{
    text-align:center;
    color:#444;
    font-size:20px;
    margin-bottom:40px;
}

/* Search Box */
div[data-baseweb="input"]{
    border-radius:50px !important;
    border:2px solid #1E88E5 !important;
    box-shadow:0px 5px 20px rgba(30,136,229,.25);
}

div[data-baseweb="input"] input{
    font-size:20px !important;
    padding:16px !important;
}

/* Suggestions Heading */
.heading{
    font-size:28px;
    color:#1565C0;
    font-weight:600;
    margin-top:20px;
    margin-bottom:15px;
}

/* Horizontal Chip */
.chip{
    display:inline-block;
    background:#1E88E5;
    color:white;
    padding:10px 20px;
    margin:8px;
    border-radius:30px;
    font-size:18px;
    font-weight:500;
    box-shadow:0px 4px 12px rgba(0,0,0,.15);
    transition:.3s;
}

.chip:hover{
    background:#1565C0;
    transform:scale(1.05);
    cursor:pointer;
}

.footer{
    text-align:center;
    margin-top:60px;
    color:#777;
    font-size:15px;
}

</style>
""", unsafe_allow_html=True)


st.markdown(
    "<div class='title'>🔍 Word Prediction</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Fast English Autocomplete using Streamlit</div>",
    unsafe_allow_html=True
)

# Search of Word Start Here

query = st.text_input(
    "",
    placeholder="Type something like cric..."
)

# Suggestion of Word Start Here
if query:

    suggestions = get_suggestions(query)

    if suggestions:

        st.markdown(
            "<div class='heading'>Suggestions</div>",
            unsafe_allow_html=True
        )

        chips = ""

        for word in suggestions:
            chips += f"<span class='chip'>{word}</span>"

        st.markdown(chips, unsafe_allow_html=True)

    else:
    
        st.markdown("""
    <div style="
        background:white;
        border:2px solid #1E88E5;
        border-radius:15px;
        padding:18px;
        margin-top:20px;
        text-align:center;
        color:#1565C0;
        font-size:20px;
        font-weight:600;
        box-shadow:0px 4px 15px rgba(0,0,0,0.08);
    ">
        ❌ No suggestions found
    </div>
    """, unsafe_allow_html=True)


