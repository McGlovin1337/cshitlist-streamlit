import json
import pandas as pd
import streamlit as st

with open('player_stats.json', 'r', encoding='utf-8') as f:
    stats = json.loads(f.read())

df = pd.DataFrame.from_dict(stats)

st.title('CS Shit List')

st.dataframe(
    data=df,
    use_container_width=True,
    hide_index=True,
    column_config={
        'KpD': 'K/D Ratio',
        'Win_Rate': 'Win Rate (%)'
    }
)
