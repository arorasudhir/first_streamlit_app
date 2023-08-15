import streamlit
import snowflake.connector
import pandas as pd

streamlit.set_page_config(layout="wide")

def init_connection():
    return snowflake.connector.connect(**streamlit.secrets["snowflake"])

conn = init_connection()
cur = conn.cursor()

def get_run_results():
    with conn.cursor() as cur:
        query = "SELECT * from DBT_RESULTS t;"
        cur.execute(query)
        return cur.fetchall()
        df = pd.DataFrame(cur.fetchall())
        return df

streamlit.title('DBT RUN RESULTS')
run_results = get_run_results()
streamlit.dataframe(run_results)
#df = pd.dataframe(run_results)

streamlit.metric(label="Models", value=run_results[2].count())

#streamlit.dataframe(df)


