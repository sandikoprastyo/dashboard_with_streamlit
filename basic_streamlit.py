import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Belajar Analisis Data")

st.header("Pengembangan Dashboard")
st.subheader("Pengembangan Dashboard")
st.write(pd.DataFrame({"c1": [1, 2, 3, 4], "c2": [12, 31, 41, 12]}))

st.markdown(
    """
    # My first app
    Hello, para calon praktisi data masa depan!
    """
)

code = """def hello():
    print("Hello, Streamlit!")"""


st.code(code, language="python")
st.text("Halo, calon praktisi data masa depan.")


st.latex(
    r"""
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
"""
)

df = pd.DataFrame(
    {
        "c1": [1, 2, 3, 4],
        "c2": [10, 20, 30, 40],
    }
)

st.dataframe(data=df, width=500, height=150)

df = pd.DataFrame(
    {
        "c1": [1, 2, 3, 4],
        "c2": [10, 20, 30, 40],
    }
)
st.table(data=df)

# metric
st.metric(label="Temperature", value="28 °C", delta="1.2 °C")

# json
st.json(
    {
        "c1": [1, 2, 3, 4],
        "c2": [10, 20, 30, 40],
    }
)

x = np.random.normal(15, 5, 250)

fig, ax = plt.subplots()
ax.hist(x=x, bins=15)
st.pyplot(fig)


st.caption("Copyright (c) 2023")
