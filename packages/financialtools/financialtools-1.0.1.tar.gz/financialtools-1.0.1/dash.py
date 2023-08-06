import streamlit as st
import yfinance as yf
import sys

PAGE_LAYOUT = dict(layout= "wide")

ticker = sys.argv[1]

st.set_page_config(**PAGE_LAYOUT)

st.title(f'FinTools Dashboard - {ticker.upper()}')

sb = st.sidebar
sb.image("fintoolslogo.png",width=300)
sb.title("FinTools v.1.0.0")
pages = ["Financial Data","Ratio Analysis"]
PAGE_SELECT = sb.selectbox("Select Page",pages)
about = sb.beta_expander("About")
about.write("Python Package for financial analysis")
license = sb.beta_expander("License")
license.write("FinTools open source under the MIT License")
author = sb.beta_expander("Author")
author.write("FinTools was authored and developed by Ryan Gilmore")

st.markdown(f"### Last Years Stock Data for {ticker.upper()}")
data = yf.Ticker(ticker)

@st.cache(allow_output_mutation=True)
def get_data(ticker):
    data = yf.Ticker(ticker)
    return data

@st.cache
def get_history(data):
    return data.history(period="1y")

data = get_data(ticker)
data_copy = data
history = get_history(data_copy)
history_copy = history.copy().astype(float)

if PAGE_SELECT == pages[0]:

    st.dataframe(history_copy)

    STATEMENTS = ['Income Statement','Balance Sheet']
    stmnt = st.selectbox("Select Statement",STATEMENTS)

    financials = data_copy.financials.astype(float)
    financials = financials.style.highlight_max(color = 'lightgreen', axis = 1)
    balancesheet = data_copy.balancesheet
    balancesheet = balancesheet.style.highlight_max(color = 'lightgreen', axis = 1)

    if stmnt == STATEMENTS[0]:
        st.table(financials)
    else:
        st.table(balancesheet)

else:
    st.subheader(pages[1])
