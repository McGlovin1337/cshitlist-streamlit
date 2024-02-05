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
            'Win_Rate': 'Win Rate (%)',
            'Entry_Attempts': 'Entry Attempts (%)',
            'Kill_Shot_Ratio': 'Kill/Shot Ratio (%)',
            'Best_Match': 'Best Match Rating',
            'Worst_Match': 'Worst Match Rating'
        }
    )

with st.container():
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

with st.container():
    fanny_col, bd_col, b_match_col, w_match_col, blanks_col = st.columns(5)

    with fanny_col:
        st.header('Fanny of the Week')
        fanny = df.drop(df[df.Games == 0].index).nsmallest(1, 'Entry_Attempts')
        st.subheader(fanny['Name'].to_string(index=False))
        st.image(fanny['Avatar'].to_string(index=False))
        st.subheader(f"Entry Attempts: {fanny['Entry_Attempts'].to_string(index=False)}%")

    with bd_col:
        st.header('Big Dick of the Week')
        big_dick = df.nlargest(1, 'Entry_Attempts')
        st.subheader(big_dick['Name'].to_string(index=False))
        st.image(big_dick['Avatar'].to_string(index=False))
        st.subheader(f"Entry Attempts: {big_dick['Entry_Attempts'].to_string(index=False)}%")

    with b_match_col:
        st.header("Can't Touch This")
        best_match = df.nlargest(1, 'Best_Match')
        st.subheader(best_match['Name'].to_string(index=False))
        st.image(best_match['Avatar'].to_string(index=False))
        st.subheader(f"Best Match Rating: {best_match['Best_Match'].to_string(index=False)}")

    with w_match_col:
        st.header('Chocolate Teapot')
        worst_match = df.drop(df[df.Games == 0].index).nsmallest(1, 'Worst_Match')
        st.subheader(worst_match['Name'].to_string(index=False))
        st.image(worst_match['Avatar'].to_string(index=False))
        st.subheader(f"Worst Match Rating: {worst_match['Worst_Match'].to_string(index=False)}")

    with blanks_col:
        st.header('Firing Blanks')
        worst_kill_shot_ratio = df.drop(df[df.Games == 0].index).nsmallest(1, 'Kill_Shot_Ratio')
        st.subheader(worst_kill_shot_ratio['Name'].to_string(index=False))
        st.image(worst_kill_shot_ratio['Avatar'].to_string(index=False))
        st.subheader(f"Kill/Shot Ratio: {worst_kill_shot_ratio['Kill_Shot_Ratio'].to_string(index=False)}%")

with st.container():
    th_col, apple_col = st.columns(2)

    with th_col:
        st.header('The Try Hard')
        most_games = df.nlargest(1, 'Games')
        st.subheader(most_games['Name'].to_string(index=False))
        st.image(most_games['Avatar'].to_string(index=False))
        st.subheader(f"Most Number of Games: {most_games['Games'].to_string(index=False)}")

    with apple_col:
        st.header('The Apple')
        least_games = df.drop(df[df.Games == 0].index).nsmallest(1, 'Games')
        st.subheader(least_games['Name'].to_string(index=False))
        st.image(least_games['Avatar'].to_string(index=False))
        st.subheader(f"Least Number of Games: {least_games['Games'].to_string(index=False)}")
