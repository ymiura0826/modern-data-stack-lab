#!/usr/bin/env python3
# coding: utf-8

from prefect import flow
from prefect_gcp.credentials import GcpCredentials
from prefect_dbt.cli.configs.bigquery import BigQueryTargetConfigs
from prefect_dbt.cli.credentials import DbtCliProfile
from prefect_dbt.cli.commands import DbtCoreOperation

@flow(name="run-dbt-on-bigquery", log_prints=True)
def run_dbt_flow():
    """
    1. GCP 認証情報ブロックをロード
    2. BigQuery 向けターゲット設定ブロックをロード
    3. DBT CLI プロファイルブロックをロード
    4. DBT Core Operation ブロックをロード
    5. DBT run を実行
    """

    # 1. GCP 認証情報
    gcp_creds: GcpCredentials = GcpCredentials.load("data-pipeline-sa-key")
    print("✔ Loaded GCP credentials block: data-pipeline-sa-key")

    # 2. BigQuery ターゲット設定
    bq_target: BigQueryTargetConfigs = BigQueryTargetConfigs.load("bq-target-configs")
    print("✔ Loaded BigQuery target configs block: bq-target-configs")

    # 3. DBT CLI プロファイル設定
    dbt_profile: DbtCliProfile = DbtCliProfile.load("dbt-cli-profile")
    print("✔ Loaded DBT CLI profile block: dbt-cli-profile")

    # 4. DBT Core Operation
    dbt_op: DbtCoreOperation = DbtCoreOperation.load("run-dbt-core")
    print("✔ Loaded DBT Core operation block: run-dbt-core")

    # 5. DBT run を実行（profiles.yml を上書きして実行）
    result = dbt_op.run(
        dbt_cli_profile=dbt_profile,
        overwrite_profiles=True
    )

    print("dbt run result:", result)

if __name__ == "__main__":
    run_dbt_flow()
