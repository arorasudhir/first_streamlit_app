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
        
streamlit.title('DBT RUN RESULTS')
run_results = get_run_results()
df = pd.DataFrame(run_results)
streamlit.write(df)

#df = pd.dataframe(run_results)

streamlit.metric(label="Models", value=len(df.index))

#streamlit.dataframe(df)


