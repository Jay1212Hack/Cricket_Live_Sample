import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv("live_cricket_data.csv")

# Streamlit page configuration
st.set_page_config(page_title="Live Cricket Dashboard", layout="wide")

# Title
st.title("🏏 Live Cricket Match Dashboard")

# Match selection dropdown
selected_match = st.selectbox("Select a Match", df["Match"].unique())
match_data = df[df["Match"] == selected_match].iloc[0]

# Match Summary
st.markdown(f"## **{match_data['Match']} - Status: {match_data['Match_Status']}**")

# Score Comparison
fig = px.bar(
    x=[match_data['Team1'], match_data['Team2']],
    y=[match_data['Team1_Score'], match_data['Team2_Score']],
    labels={'x': 'Teams', 'y': 'Score'},
    title='Score Comparison',
    color=[match_data['Team1'], match_data['Team2']],
    color_discrete_map={match_data['Team1']: 'blue', match_data['Team2']: 'red'}
)
st.plotly_chart(fig, use_container_width=True)

# Player Performance Table
st.subheader("🏆 Top Performers")
player_data = {
    "Top Batsman": [match_data['Top_Batsman']],
    "Runs": [match_data['Top_Batsman_Runs']],
    "Top Bowler": [match_data['Top_Bowler']],
    "Wickets": [match_data['Top_Bowler_Wickets']]
}
st.table(pd.DataFrame(player_data))

# Footer
st.markdown("---")
st.text("Created with ❤️ using Streamlit & Plotly")
