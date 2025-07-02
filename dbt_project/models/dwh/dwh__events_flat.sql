-- models/staging/ga4/dwh__events_flat.sql

{{ config(
    materialized='table',
    alias='events_flat',
    partition_by={"field": "event_date", "data_type": "date"}
) }}

{% set target_date = var('target_date', '20250629') %}

SELECT
  PARSE_DATE('%Y%m%d', _TABLE_SUFFIX) AS event_date,
  event_timestamp,
  event_name,
  user_pseudo_id,

  (SELECT value.string_value FROM UNNEST(event_params) WHERE key = "page_location") AS page_location,
  (SELECT value.string_value FROM UNNEST(event_params) WHERE key = "page_title") AS page_title,
  (SELECT value.int_value FROM UNNEST(event_params) WHERE key = "ga_session_id") AS ga_session_id,
  (SELECT value.int_value FROM UNNEST(event_params) WHERE key = "ga_session_number") AS ga_session_number

FROM
  `seraphic-elixir-462005-c6.analytics_492032347.events_*`
WHERE
  _TABLE_SUFFIX = '{{ target_date }}'
