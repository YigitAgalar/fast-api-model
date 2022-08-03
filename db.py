from sqlalchemy import create_engine
import io
import pandas as pd

engine = create_engine(
    )


def postgre_insert(engine, table_name, df):
    conn = engine.raw_connection()
    cur = conn.cursor()
    dummy_file = io.StringIO()
    df.to_csv(dummy_file, sep=",", index=False, header=False)
    dummy_file.seek(1)
    content = dummy_file.getvalue()
    cur.copy_from(dummy_file, table_name, sep=",", null="",)
    conn.commit()


table = "loglar"
query = """CREATE TABLE IF NOT EXISTS {0} (
        timestamp TIMESTAMP WITHOUT TIME ZONE,
        "customerID" TEXT,
        churn_prediction TEXT
)
""".format(table)


engine.execute(f"DROP TABLE IF EXISTS {table}")
print("table dropped if exist")
engine.execute(query)
print("Table created")
# postgre_insert(engine,table,df)
