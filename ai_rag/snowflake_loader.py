import os
import snowflake.connector

def get_policy_details(policy_id):
    conn = snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA")
    )
    cursor = conn.cursor()
    cursor.execute("""
        SELECT POLICY_ID, CANCEL_REASON_CODE, PAYMENT_SUMMARY
        FROM INSURANCE_ANALYTICS.POLICY_CANCELLATION_SUMMARY
        WHERE POLICY_ID = %s
    """, (policy_id,))
    row = cursor.fetchone()
    return {
        "policy_id": row[0],
        "cancel_code": row[1],
        "payment_summary": row[2]
    } if row else {}
