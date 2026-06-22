import streamlit as st
import pandas as pd
import joblib

from capture import capture_features

model = joblib.load(
    "models/live_model.pkl"
)

st.title(
    "AI Network Intrusion Detection System"
)

st.write(
    "Random Forest + Rule Based Detection"
)

if st.button("Capture & Analyze"):

    with st.spinner(
        "Capturing Live Traffic..."
    ):

        features, alerts = capture_features(
            100
        )

    stats_df = pd.DataFrame(
        [features],
        columns=[
            "packet_count",
            "avg_packet_size",
            "tcp_count",
            "udp_count",
            "unique_ips"
        ]
    )

    st.subheader(
        "Traffic Statistics"
    )

    st.dataframe(stats_df)

    prediction = model.predict(
        stats_df
    )[0]

    st.subheader(
        "Machine Learning Prediction"
    )

    if prediction == 0:

        st.success(
            "✅ Normal Traffic"
        )

    else:

        st.error(
            "🚨 Attack Detected"
        )

    st.subheader(
        "Rule-Based Alerts"
    )

    if alerts:

        for alert in alerts:
            st.warning(alert)

    else:

        st.success(
            "No Rule-Based Alerts"
        )