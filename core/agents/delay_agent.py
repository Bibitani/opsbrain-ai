import psycopg2

# -----------------------------
# Database connection
# -----------------------------
conn = psycopg2.connect(
    host="localhost",
    database="opsbrain_db",
    user="postgres",
    password="59205920"  # change this
)

cursor = conn.cursor()

# -----------------------------
# SQL queries (canonical)
# -----------------------------
queries = {
    "weather": """
        SELECT weather_condition, delay_rate_percent
        FROM (
            SELECT
              weather_condition,
              ROUND(
                SUM(CASE WHEN delayed THEN 1 ELSE 0 END)::NUMERIC
                / COUNT(*) * 100, 2
              ) AS delay_rate_percent
            FROM deliveries
            GROUP BY weather_condition
        ) t
        ORDER BY delay_rate_percent DESC;
    """,

    "partner": """
        SELECT delivery_partner, delay_rate_percent
        FROM (
            SELECT
              delivery_partner,
              ROUND(
                SUM(CASE WHEN delayed THEN 1 ELSE 0 END)::NUMERIC
                / COUNT(*) * 100, 2
              ) AS delay_rate_percent
            FROM deliveries
            GROUP BY delivery_partner
        ) t
        ORDER BY delay_rate_percent DESC;
    """,

    "vehicle": """
        SELECT vehicle_type, delay_rate_percent
        FROM (
            SELECT
              vehicle_type,
              ROUND(
                SUM(CASE WHEN delayed THEN 1 ELSE 0 END)::NUMERIC
                / COUNT(*) * 100, 2
              ) AS delay_rate_percent
            FROM deliveries
            GROUP BY vehicle_type
        ) t
        ORDER BY delay_rate_percent DESC;
    """
}

# -----------------------------
# Run queries
# -----------------------------
results = {}

for key, sql in queries.items():
    cursor.execute(sql)
    results[key] = cursor.fetchall()

# -----------------------------
# OpsBrain reasoning
# -----------------------------
def explain_delays(data):
    weather = data["weather"]
    partner = data["partner"]
    vehicle = data["vehicle"]

    explanation = []

    explanation.append("Delivery delays are driven primarily by external and partner-level factors.\n")

    top_weather = weather[0]
    explanation.append(
        f"- Weather impact is strongest: '{top_weather[0]}' conditions show the highest delay rate "
        f"({top_weather[1]}%)."
    )

    top_partner = partner[0]
    explanation.append(
        f"- Partner performance varies: '{top_partner[0]}' has the highest delay rate "
        f"({top_partner[1]}%), indicating execution quality differences."
    )

    vehicle_spread = vehicle[0][1] - vehicle[-1][1]
    explanation.append(
        f"- Vehicle type impact is minimal (spread ≈ {round(vehicle_spread, 2)}%), "
        f"so vehicle choice is not a primary cause."
    )

    explanation.append(
        "\nConclusion: Delays should be addressed through partner performance management "
        "and weather-aware planning, not vehicle changes."
    )

    return "\n".join(explanation)


# -----------------------------
# Run OpsBrain
# -----------------------------
print("\n🧠 OpsBrain Analysis\n")
print(explain_delays(results))

cursor.close()
conn.close()
