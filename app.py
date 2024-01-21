import json
import pandas as pd
import streamlit as st

with open('player_stats.json', 'r', encoding='utf-8') as f:
    stats = json.loads(f.read())

pd.set_option('display.max_colwidth', 500)
df = pd.DataFrame.from_dict(stats)

stats = df.drop(columns='Avatar', axis=1)

st.set_page_config(layout='wide')

st.title('CS Shit List')

# Overall Table
with st.container():
    st.dataframe(
        data=stats,
        use_container_width=True,
        hide_index=True,
        column_config={
            'KpD': 'K/D Ratio',
            'Win_Rate': 'Win Rate (%)'
        }
    )

# Top Player
top_col, bot_col, rq_col, a_col, z_col = st.columns(5)

with top_col:
    st.header('Top Player')
    top = df.nlargest(1, 'Rating')
    st.subheader(top['Name'].to_string(index=False))
    st.image(top['Avatar'].to_string(index=False))
    st.subheader(f"Rating: {top['Rating'].to_string(index=False)}")

with bot_col:
    st.header('Shit Player')
    bot = df.drop(df[df.Games == 0].index).nsmallest(1, 'Rating')
    st.subheader(bot['Name'].to_string(index=False))
    st.image(bot['Avatar'].to_string(index=False))
    st.subheader(f"Rating: {bot['Rating'].to_string(index=False)}")

with rq_col:
    st.header('Rage Quit')
    rqs = df.drop(df[df.Games > 0].index).filter(['Name'])
    st.dataframe(
        data=rqs,
        use_container_width=True,
        hide_index=True
    )

with a_col:
    st.header('A Team')
    a_team = df.nlargest(5, 'Rating')
    st.dataframe(
        data=a_team.filter(['Name', 'Rating']),
        use_container_width=True,
        hide_index=True
    )

with z_col:
    st.header('Z Team')
    z_team = df.drop(df[df.Games == 0].index).nsmallest(5, 'Rating')
    st.dataframe(
        data=z_team.filter(['Name', 'Rating']),
        use_container_width=True,
        hide_index=True
    )
