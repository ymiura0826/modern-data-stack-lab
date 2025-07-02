from prefect import flow
import subprocess

@flow(log_prints=True)
def test_dbt_exists():
    result = subprocess.run(["which", "dbt"], capture_output=True, text=True)
    print("DBT path:", result.stdout or "dbt NOT FOUND")

if __name__ == "__main__":
    test_dbt_exists()
