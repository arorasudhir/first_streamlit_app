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
        query = "SELECT
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
                    DBT_RESULTS t;"
        cur.execute(query)
        return cur.fetchall()
        # df = pd.DataFrame(dat, columns=[col[0] for col in cur.description])
        # return df

streamlit.title('DBT RUN RESULTS')
run_results = get_run_results()
streamlit.dataframe(run_results)


#streamlit.metric(label="Models", value="70 °F", delta="1.2 °F")



