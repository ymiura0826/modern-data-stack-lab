from prefect import flow
from prefect_dbt.cli.commands import DbtCoreOperation

@flow(log_prints=True)
def run_dbt_flow():
    # 先ほど作成した Block 名（run-dbt-core）を指定
    result = DbtCoreOperation.load("run-dbt-core").run()
    print("dbt run result:", result)

if __name__ == "__main__":
    run_dbt_flow()
