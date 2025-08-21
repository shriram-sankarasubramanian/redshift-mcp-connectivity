# Author: Shriram
# Date: 2025-08-17

import psycopg2
from dotenv import load_dotenv
import os
from query_agent import english_to_sql
from dotenv import load_dotenv
load_dotenv()


def run_sql(sql: str):

    # print(os.getenv("REDSHIFT_HOST"))
    # print(os.getenv("REDSHIFT_PORT"))
    # print(os.getenv("REDSHIFT_DB"))
    # print(os.getenv("REDSHIFT_USER"))


    conn = psycopg2.connect(
        host=os.getenv("REDSHIFT_HOST"),
        port=os.getenv("REDSHIFT_PORT"),
        dbname=os.getenv("REDSHIFT_DB"),
        user=os.getenv("REDSHIFT_USER"),
        password=os.getenv("REDSHIFT_PASSWORD")
    )
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

if __name__ == "__main__":
    prompt = input("Ask your question: ")
    sql = english_to_sql(prompt)
    print(f"\nGenerated SQL:\n{sql}\n")
    run_sql(sql)

