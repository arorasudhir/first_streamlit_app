import streamlit
import snowflake.connector
import pandas as pd

streamlit.set_page_config(layout="wide")

def init_connection():
    return snowflake.connector.connect(**streamlit.secrets["snowflake"])

conn = init_connection()
cur = conn.cursor()

def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        dat = cur.fetchall()
        df = pd.DataFrame(dat, columns=[col[0] for col in cur.description])
        return df


df = run_query("""SELECT
    t.RESULT_ID,
    t.INVOCATION_ID,
    t.UNIQUE_ID,
    t.DATABASE_NAME,
    t.SCHEMA_NAME,
    t.NAME,
    t.STATUS,
    t.EXECUTION_TIME,
    t.ROWS_AFFECTED
from
    DBT_RESULTS t;""")

df2 = df

streamlit.title('DBT RUN RESULTS')
 streamlit.text(df2)


#streamlit.metric(label="Models", value="70 °F", delta="1.2 °F")



