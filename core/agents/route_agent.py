import psycopg2
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_connection():
    """Establish PostgreSQL connection"""
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        database=os.getenv("DB_NAME", "opsbrain_db"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD")
    )

def explain_routes(results):
    """
    Format SQL results into structured text for LLM reasoning.
    SQL = facts, LLM = interpretation.
    """
    explanation = "=== ROUTE OPTIMIZATION ANALYSIS ===\n\n"

    explanation += "## Delay Rate by Route Pattern (Region + Mode + Vehicle):\n"
    for row in results["route_delay"]:
        explanation += (
            f"- Region: {row[0]}, Mode: {row[1]}, Vehicle: {row[2]} | "
            f"Delay Rate: {row[5]}% ({row[4]}/{row[3]} delayed)\n"
        )

    explanation += "\n## Cost Inefficiency on Delayed Routes:\n"
    for row in results["cost_efficiency"]:
        explanation += (
            f"- Region: {row[0]}, Mode: {row[1]}, Vehicle: {row[2]} | "
            f"Avg Cost: ₹{row[3]}, Avg Distance: {row[4]} km, Cost/km: ₹{row[5]}\n"
        )

    explanation += "\n## Delay Sensitivity by Distance Bucket:\n"
    for row in results["distance_bucket"]:
        explanation += (
            f"- Distance: {row[0]} | Delay Rate: {row[2]}% ({row[1]} deliveries)\n"
        )

    return explanation

def llm_explain_routes(raw_analysis):
    """
    Send formatted route data to Ollama for reasoning.
    """
    system_prompt = """You are OpsBrain AI, a logistics operations analyst.

You are analyzing route efficiency using:
- delay probability
- cost per km
- distance patterns

Your task:
1. Identify inefficient route patterns
2. Explain likely operational causes
3. Recommend corrective actions

Rules:
- Do NOT invent timing or speed metrics
- Use ONLY the provided data
- Be operational and actionable

Respond in this format:
## Key Inefficient Routes
## Root Cause Analysis
## Recommended Actions
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.2",
                "prompt": f"{system_prompt}\n\nAnalyze this route data:\n\n{raw_analysis}",
                "stream": False,
                "options": {
                    "temperature": 0.3,
                    "num_predict": 800
                }
            },
            timeout=60
        )

        if response.status_code == 200:
            return response.json()["response"]
        else:
            return f"Ollama API error: {response.status_code} - {response.text}"

    except requests.exceptions.ConnectionError:
        return "Error: Cannot connect to Ollama. Make sure Ollama is running."
    except Exception as e:
        return f"Error calling Ollama: {str(e)}"

def run_route_analysis():
    """
    Pain Module 3: Route Optimization
    """
    try:
        conn = get_connection()
        cursor = conn.cursor()

        queries = {
            "route_delay": """
                SELECT
                    region,
                    delivery_mode,
                    vehicle_type,
                    COUNT(*) AS total,
                    SUM(CASE WHEN delayed = 'yes' THEN 1 ELSE 0 END) AS delayed,
                    ROUND(
                        SUM(CASE WHEN delayed = 'yes' THEN 1 ELSE 0 END)::NUMERIC
                        / COUNT(*) * 100,
                        2
                    ) AS delay_rate_percent
                FROM deliveries
                GROUP BY region, delivery_mode, vehicle_type
                HAVING COUNT(*) > 30
                ORDER BY delay_rate_percent DESC;
            """,

            "cost_efficiency": """
                SELECT
                    region,
                    delivery_mode,
                    vehicle_type,
                    ROUND(AVG(delivery_cost), 2) AS avg_cost,
                    ROUND(AVG(distance_km), 2) AS avg_distance,
                    ROUND(
                        AVG(delivery_cost / NULLIF(distance_km, 0)),
                        2
                    ) AS cost_per_km
                FROM deliveries
                WHERE delayed = 'yes'
                GROUP BY region, delivery_mode, vehicle_type
                ORDER BY cost_per_km DESC;
            """,

            "distance_bucket": """
                SELECT
                    CASE
                        WHEN distance_km < 5 THEN 'Short'
                        WHEN distance_km BETWEEN 5 AND 20 THEN 'Medium'
                        ELSE 'Long'
                    END AS distance_bucket,
                    COUNT(*) AS total,
                    ROUND(
                        SUM(CASE WHEN delayed = 'yes' THEN 1 ELSE 0 END)::NUMERIC
                        / COUNT(*) * 100,
                        2
                    ) AS delay_rate_percent
                FROM deliveries
                GROUP BY distance_bucket
                ORDER BY delay_rate_percent DESC;
            """
        }

        results = {}
        for k, q in queries.items():
            cursor.execute(q)
            results[k] = cursor.fetchall()

        raw_analysis = explain_routes(results)

        print("Raw Analysis:")
        print(raw_analysis)
        print("\n" + "=" * 50 + "\n")
        print("Generating AI Insights...\n")

        final_answer = llm_explain_routes(raw_analysis)

        cursor.close()
        conn.close()

        return final_answer

    except psycopg2.Error as e:
        return f"Database error: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"

if __name__ == "__main__":
    print(run_route_analysis())
