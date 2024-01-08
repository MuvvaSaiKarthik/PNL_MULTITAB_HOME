import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import time
import datetime

st.set_page_config(layout='wide')

def logout():
    if st.button("Logout"):
        st.markdown(
            """
            <meta http-equiv="refresh" content="0;URL='https://pnlmultitab.streamlit.app/'"/>
            """
            , unsafe_allow_html=True
        )

logout()

selected = option_menu(
        menu_title=None,
        options=['PNL', 'SENTI', 'Scenario'],
        default_index=0,  # default selected navigation
        orientation='horizontal'
    )

def fetch_data():
    try:
        df = pd.read_csv('PNL_Team.csv')
        df[['Mrg', 'Y_PNL', 'E_PNL', 'O_PNL', 'I_PNL', 'T_PNL']] = df[['Mrg', 'Y_PNL', 'E_PNL', 'O_PNL', 'I_PNL', 'T_PNL']].round(2)
        return df
    except Exception as e:
        print(f'Error fetching the data: {str(e)}')
        return None

def style_dataframe(df):
    return df.style.applymap(
        lambda x: 'color: green' if x > 0 else ('color: red' if x < 0 else 'color: black'),
        subset=['Mrg', 'Y_PNL', 'E_PNL', 'O_PNL', 'I_PNL', 'T_PNL', 'PL_D10U5',
       'PL_U5U3', 'PinPout', 'Actual', 'ExpOptVal', 'With_Exch']
    )

if selected == 'PNL':
    st.title('PNL')
    # Create placeholders for dynamic content
    time_display = st.empty()
    total_dataframe_placeholder = st.empty()
    pnl_dataframe_placeholder = st.empty()

    while True:
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Read quantity_fetch_time.csv
        quantity_fetch_time_df = pd.read_csv('quantity_fetch_time.csv')
        quantity_fetch_time = pd.to_datetime(quantity_fetch_time_df['Fetch Time'].iloc[0])

        # Update time_display placeholder
        time_display.write(f'Current Time {current_time}   |   PNL Time {quantity_fetch_time}', format='md')

        # Fetch data
        pnl_df = fetch_data()

        if pnl_df is not None:
            # Calculate and append totals row
            totals_row = pnl_df.select_dtypes(include=['number']).sum()
            totals_df = pd.DataFrame()
            totals_df = totals_df.append(totals_row, ignore_index=True)
            totals_df.reset_index(inplace=True)
            totals_df.rename(columns={'index': 'Name'}, inplace=True)
            totals_df['Name'] = 'Total'

            totals_df[['Mrg', 'Y_PNL', 'E_PNL', 'O_PNL', 'I_PNL', 'T_PNL', 'PL_D10U5', 'PL_U5U3', 'PinPout', 'Actual',
                       'ExpOptVal', 'With_Exch']] = totals_df[
                ['Mrg', 'Y_PNL', 'E_PNL', 'O_PNL', 'I_PNL', 'T_PNL', 'PL_D10U5', 'PL_U5U3', 'PinPout', 'Actual',
                 'ExpOptVal', 'With_Exch']].astype(int)

            pnl_df[['Mrg', 'Y_PNL', 'E_PNL', 'O_PNL', 'I_PNL', 'T_PNL', 'PL_D10U5', 'PL_U5U3', 'PinPout', 'Actual',
                    'ExpOptVal', 'With_Exch']] = pnl_df[
                ['Mrg', 'Y_PNL', 'E_PNL', 'O_PNL', 'I_PNL', 'T_PNL', 'PL_D10U5', 'PL_U5U3', 'PinPout', 'Actual',
                 'ExpOptVal', 'With_Exch']].astype(int)

            # Create styled data frames
            totals_styled_df = style_dataframe(totals_df)
            pnl_styled_df = style_dataframe(pnl_df)

            # update data using place holders
            total_dataframe_placeholder.dataframe(totals_styled_df, width=5000)
            pnl_dataframe_placeholder.dataframe(pnl_styled_df, height=1350, width=5000)

        # Sleep for 3 seconds before the next update
        time.sleep(3)

if selected == 'SENTI':
    st.title('SENTI')

    # Create placeholders for dynamic content
    time_display = st.empty()
    total_dataframe_placeholder = st.empty()
    pnl_dataframe_placeholder = st.empty()

    while True:
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Read quantity_fetch_time.csv
        quantity_fetch_time_df = pd.read_csv('quantity_fetch_time.csv')
        quantity_fetch_time = pd.to_datetime(quantity_fetch_time_df['Fetch Time'].iloc[0])

        # Update time_display placeholder
        time_display.write(f'Current Time {current_time}   |   PNL Time {quantity_fetch_time}', format='md')

        # Fetch data
        pnl_df = fetch_data()

        if pnl_df is not None:
            # Calculate and append totals row
            totals_row = pnl_df.select_dtypes(include=['number']).sum()
            totals_df = pd.DataFrame()
            totals_df = totals_df.append(totals_row, ignore_index=True)
            totals_df.reset_index(inplace=True)
            totals_df.rename(columns={'index': 'Name'}, inplace=True)
            totals_df['Name'] = 'Total'

            totals_df[['Mrg', 'Y_PNL', 'E_PNL', 'O_PNL', 'I_PNL', 'T_PNL', 'PL_D10U5', 'PL_U5U3', 'PinPout', 'Actual',
                       'ExpOptVal', 'With_Exch']] = totals_df[
                ['Mrg', 'Y_PNL', 'E_PNL', 'O_PNL', 'I_PNL', 'T_PNL', 'PL_D10U5', 'PL_U5U3', 'PinPout', 'Actual',
                 'ExpOptVal', 'With_Exch']].astype(int)

            pnl_df[['Mrg', 'Y_PNL', 'E_PNL', 'O_PNL', 'I_PNL', 'T_PNL', 'PL_D10U5', 'PL_U5U3', 'PinPout', 'Actual',
                    'ExpOptVal', 'With_Exch']] = pnl_df[
                ['Mrg', 'Y_PNL', 'E_PNL', 'O_PNL', 'I_PNL', 'T_PNL', 'PL_D10U5', 'PL_U5U3', 'PinPout', 'Actual',
                 'ExpOptVal', 'With_Exch']].astype(int)

            # Create styled data frames
            totals_styled_df = style_dataframe(totals_df)
            pnl_styled_df = style_dataframe(pnl_df)

            # update data using place holders
            total_dataframe_placeholder.dataframe(totals_styled_df, width=5000)
            pnl_dataframe_placeholder.dataframe(pnl_styled_df, height=1350, width=5000)

        # Sleep for 3 seconds before the next update
        time.sleep(3)

if selected == 'Scenario':
    st.title('SCENARIO')
    # Create placeholders for dynamic content
    time_display = st.empty()
    total_dataframe_placeholder = st.empty()
    pnl_dataframe_placeholder = st.empty()

    while True:
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Read quantity_fetch_time.csv
        quantity_fetch_time_df = pd.read_csv('quantity_fetch_time.csv')
        quantity_fetch_time = pd.to_datetime(quantity_fetch_time_df['Fetch Time'].iloc[0])

        # Update time_display placeholder
        time_display.write(f'Current Time {current_time}   |   PNL Time {quantity_fetch_time}', format='md')

        # Fetch data
        pnl_df = fetch_data()

        if pnl_df is not None:
            # Calculate and append totals row
            totals_row = pnl_df.select_dtypes(include=['number']).sum()
            totals_df = pd.DataFrame()
            totals_df = totals_df.append(totals_row, ignore_index=True)
            totals_df.reset_index(inplace=True)
            totals_df.rename(columns={'index': 'Name'}, inplace=True)
            totals_df['Name'] = 'Total'

            totals_df[['Mrg', 'Y_PNL', 'E_PNL', 'O_PNL', 'I_PNL', 'T_PNL', 'PL_D10U5', 'PL_U5U3', 'PinPout', 'Actual',
                       'ExpOptVal', 'With_Exch']] = totals_df[
                ['Mrg', 'Y_PNL', 'E_PNL', 'O_PNL', 'I_PNL', 'T_PNL', 'PL_D10U5', 'PL_U5U3', 'PinPout', 'Actual',
                 'ExpOptVal', 'With_Exch']].astype(int)

            pnl_df[['Mrg', 'Y_PNL', 'E_PNL', 'O_PNL', 'I_PNL', 'T_PNL', 'PL_D10U5', 'PL_U5U3', 'PinPout', 'Actual',
                    'ExpOptVal', 'With_Exch']] = pnl_df[
                ['Mrg', 'Y_PNL', 'E_PNL', 'O_PNL', 'I_PNL', 'T_PNL', 'PL_D10U5', 'PL_U5U3', 'PinPout', 'Actual',
                 'ExpOptVal', 'With_Exch']].astype(int)

            # Create styled data frames
            totals_styled_df = style_dataframe(totals_df)
            pnl_styled_df = style_dataframe(pnl_df)

            # update data using place holders
            total_dataframe_placeholder.dataframe(totals_styled_df, width=5000)
            pnl_dataframe_placeholder.dataframe(pnl_styled_df, height=1350, width=5000)

        # Sleep for 3 seconds before the next update
        time.sleep(3)



