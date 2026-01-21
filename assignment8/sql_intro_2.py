import sqlite3
import pandas as pd

try:
    with sqlite3.connect("../db/lesson.db") as conn:
        print("Connected to lesson.db")

        sql="""
        SELECT
            li.line_item_id,
            li.quantity,
            li.product_id,
            p.product_name,
            p.price
        FROM line_items li
        JOIN products p
        ON li.product_id = p.product_id;
        """
        df = pd.read_sql_query(sql, conn)
        print(df.head(5))

        df["total"] = df["quantity"] * df["price"]

        summary = (
            df.groupby("product_id")
                .agg({
                    "line_item_id" : "count",
                    "total" : "sum",
                    "product_name" : "first"
                })
                .reset_index()
        )
        print(summary.head(5))

        summary = summary.sort_values("product_name")
        print(summary.head(5))

        summary.to_csv("order_summary.csv", index=False)
        print("Saved order_summary.csv")

except sqlite3.Error as e:
    print("Database error:", e)