#!/usr/bin/env python3
# coding: utf-8

from prefect import flow
from prefect_dbt.cli.credentials import DbtCliProfile
from prefect_dbt.cli.commands import DbtCoreOperation

@flow(name="run-dbt-on-bigquery", log_prints=True)
def run_dbt_flow():
    dbt_profile: DbtCliProfile = DbtCliProfile.load("dbt-cli-profile")
    dbt_op: DbtCoreOperation = DbtCoreOperation.load("run-dbt-core")
    result = dbt_op.run(
        dbt_cli_profile=dbt_profile,
        overwrite_profiles=True
    )

    print("dbt run result:", result)

if __name__ == "__main__":
    run_dbt_flow()
