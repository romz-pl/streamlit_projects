import streamlit as st
import time
import numpy as np
import matplotlib.pyplot as plt




def main():
    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()
    fig = plt.figure(figsize=(8, 4))
    ax = plt.subplot(aspect='auto')
    x = list()
    y = list()
    for i in range(1, 101):
        x.append(i)
        y.append( np.random.randn() )
        status_text.text("%i%% Complete" % i)
        progress_bar.progress(i)
        time.sleep(0.02)

    ax.plot(x, np.cumsum(y))
    st.pyplot(fig)
    plt.close()
    progress_bar.empty()
    # # Streamlit widgets automatically run the script from top to bottom. Since
    # # this button is not connected to any other logic, it just causes a plain
    # # rerun.
    st.button("Re-run")


main()
