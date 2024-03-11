import json
import pandas as pd
import streamlit as st

with open('player_stats.json', 'r', encoding='utf-8') as f:
    stats = json.loads(f.read())

pd.set_option('display.max_colwidth', 500)
df = pd.DataFrame.from_dict(stats)

stats = df.drop(columns=['Avatar', 'Maps'], axis=1)
stats.sort_values(by=['Rating'], ascending=False, inplace=True)

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

df.drop(df[df.Games == 0].index, inplace=True)

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
    th_col, apple_col, kills_col, deaths_col, assists_col = st.columns(5)

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

    with kills_col:
        avg_kills = [
            {
                'Name': k['Name'],
                'Kills': round(int(k['Kills']) / int(k['Games']), 2),
                'Avatar': k['Avatar']
            }
            for _, k in df.iterrows()
        ]
        df_avg_kills = pd.DataFrame.from_records(avg_kills)
        st.header('The Terminator')
        most_kills = df_avg_kills.nlargest(1, 'Kills')
        st.subheader(most_kills['Name'].to_string(index=False))
        st.image(most_kills['Avatar'].to_string(index=False))
        st.subheader(f"Avg Kills per Game: {most_kills['Kills'].to_string(index=False)}")

    with deaths_col:
        st.header('Canon Fodder')
        avg_deaths = [
            {
                'Name': k['Name'],
                'Deaths': round(int(k['Deaths']) / int(k['Games']), 2),
                'Avatar': k['Avatar']
            }
            for _, k in df.iterrows()
        ]
        df_avg_deaths = pd.DataFrame.from_records(avg_deaths)
        most_deaths = df_avg_deaths.nlargest(1, 'Deaths')
        st.subheader(most_deaths['Name'].to_string(index=False))
        st.image(most_deaths['Avatar'].to_string(index=False))
        st.subheader(f"Avg Deaths per Game: {most_deaths['Deaths'].to_string(index=False)}")

    with assists_col:
        st.header('The Assistant')
        avg_assists = [
            {
                'Name': k['Name'],
                'Assists': round(int(k['Assists']) / int(k['Games']), 2),
                'Avatar': k['Avatar']
            }
            for _, k in df.iterrows()
        ]
        df_avg_assists = pd.DataFrame.from_records(avg_assists)
        most_assists = df_avg_assists.nlargest(1, 'Assists')
        st.subheader(most_assists['Name'].to_string(index=False))
        st.image(most_assists['Avatar'].to_string(index=False))
        st.subheader(f"Avg Assists per Game: {most_assists['Assists'].to_string(index=False)}")

with st.container():
    map_table, clutch_col, multik_col, kobe_col = st.columns(4)

    with map_table:
        st.header('Map Statistics')
        map_stats = {}
        for i, r in df.iterrows():
            for k, v in r['Maps'].items():
                try:
                    map_stats[k] = map_stats[k] + v
                except KeyError:
                    map_stats[k] = v

        map_tbl = pd.DataFrame(map_stats.items())
        map_tbl.columns = ['Map', 'Games']
        map_tbl.sort_values(by='Games', inplace=True, ascending=False)

        st.dataframe(
            data=map_tbl,
            use_container_width=True,
            hide_index=True
        )

    with clutch_col:
        st.header('Clutch Minister')
        clutch_pts = {}
        for i, r in df.iterrows():
            clutch_pts.update(
                {f"{r['Name']}": r['1v1'] + (3 * r['1v2']) + (5 * r['1v3']) + (7 * r['1v4']) + (10 * r['1v5'])}
            )

        clutch_minister = max(clutch_pts, key=clutch_pts.get)
        st.subheader(clutch_minister)
        st.image(df[df['Name'] == clutch_minister]['Avatar'].to_string(index=False))
        st.subheader(f'Clutch Points: {clutch_pts[clutch_minister]}')
        st.text(f"""
        1v1: {df[df['Name'] == clutch_minister]['1v1'].to_string(index=False)} x 1pt
        1v2: {df[df['Name'] == clutch_minister]['1v2'].to_string(index=False)} x 3pts
        1v3: {df[df['Name'] == clutch_minister]['1v3'].to_string(index=False)} x 5pts
        1v4: {df[df['Name'] == clutch_minister]['1v4'].to_string(index=False)} x 7pts
        1v5: {df[df['Name'] == clutch_minister]['1v5'].to_string(index=False)} x 10pts
        """)

    with multik_col:
        st.header('Multi-Killa')
        mk_pts = {}
        for i, r in df.iterrows():
            mk_pts.update(
                {f"{r['Name']}": (4 * r['3k']) + (7 * r['4k']) + (10 * r['5k'])}
            )

        multi_killa = max(mk_pts, key=mk_pts.get)
        st.subheader(multi_killa)
        st.image(df[df['Name'] == multi_killa]['Avatar'].to_string(index=False))
        st.subheader(f'Multi Kill Points: {mk_pts[multi_killa]}')
        st.text(f"""
        3k: {df[df['Name'] == multi_killa]['3k'].to_string(index=False)} x 4pts
        4k: {df[df['Name'] == multi_killa]['4k'].to_string(index=False)} x 7pts
        5k: {df[df['Name'] == multi_killa]['5k'].to_string(index=False)} x 10pts
        """)

    with kobe_col:
        st.header('The Kobe')
        avg_ud = [
            {
                'Name': k['Name'],
                'UD': round(int(k['UD']) / int(k['Games']), 2),
                'Avatar': k['Avatar']
            }
            for _, k in df.iterrows()
        ]
        df_avg_ud = pd.DataFrame.from_records(avg_ud)
        most_ud = df_avg_ud.nlargest(1, 'UD')
        st.subheader(most_ud['Name'].to_string(index=False))
        st.image(most_ud['Avatar'].to_string(index=False))
        st.subheader(f"Avg UD per Game: {most_ud['UD'].to_string(index=False)}")
