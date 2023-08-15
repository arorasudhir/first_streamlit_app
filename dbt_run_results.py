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
        # df = pd.DataFrame(dat, columns=[col[0] for col in cur.description])
        # return df

streamlit.title('DBT RUN RESULTS')
run_results = get_run_results()
df = pd.dataframe(run_results)

streamlit.metric(label="Models", value=df['2'].nunique(), delta="1.2 °F")

streamlit.dataframe(df)


