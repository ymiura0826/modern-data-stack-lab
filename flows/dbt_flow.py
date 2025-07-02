from prefect import flow
from prefect_dbt.cli.commands import DbtCoreOperation
from prefect_gcp import GcpCredentials

@flow(log_prints=True)
def run_dbt_flow():
    gcp_credentials = GcpCredentials.load("data-pipeline-sa-key")
    result = DbtCoreOperation.load("run-dbt-core").run()
    print("dbt run result:", result)

if __name__ == "__main__":
    run_dbt_flow()
