import streamlit as st

import yfinance as yf

st.title("Depot status and ETF stats")

#st.title("yf vanguard all world ")


@st.cache

def get_ticker(shortname):
    vanguard = yf.Ticker(shortname)#"#VGWL.DE")

    df=(vanguard.history(period='1y', interval='1d', start=None, end=None, prepost=False, actions=True, auto_adjust=True, back_adjust=False, proxy=None, rounding=False, tz=None,).iloc[:,0:5])
    return df


shares=444.2184
submit = st.button('refresh')
if submit:
    vanguard_last_close= get_ticker("VGWL.DE").iloc[-1,3]
    current_stat=vanguard_last_close * shares #get_ticker("VGWL.DE").iloc[-1,3]#
    #444.2184#64.9556
    invested = 500+5000+5000+27766.4
    st.write("Vanguard FTSE all world close: ", vanguard_last_close, "no. of shares: ", shares)
    st.write("Depot status: ",current_stat, " total invest: ", invested)
    st.write("win / loss: ",current_stat- invested)
    st.write("Performance: ",((current_stat - invested)/invested)*100)
    tname = st.selectbox('Choose ticker name: ',('VWRL.MI','VGWL.DE', 'XDWD.DE','XMAW.DE'))
    st.write(get_ticker(tname).iloc[-1,])

    st.line_chart(get_ticker(tname)["Close"])


#st.write(float(df.iloc[0,3][0])*64.9556)
