CREATE OR REPLACE VIEW `seraphic-elixir-462005-c6.dataops.sync_status_latest` AS
SELECT
  execution_date,
  pipeline_name,
  status_name,
  triggered_by,
  inserted_at
FROM (
  SELECT
    *,
    ROW_NUMBER() OVER (
      PARTITION BY execution_date, pipeline_name
      ORDER BY inserted_at DESC
    ) AS rn
  FROM
    `seraphic-elixir-462005-c6.dataops.sync_status_logs`
)
WHERE rn = 1;
