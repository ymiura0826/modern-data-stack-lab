-- models/mart/mart__web_site_metrics.sql

{{ config(
    materialized='table',
    alias='web_site_metrics'
) }}

{% set target_date = var('target_date', '20250629') %}

SELECT 
  event_date
  ,COUNT(DISTINCT user_pseudo_id) AS user_num
  ,SUM(CASE WHEN event_name = 'page_view' THEN 1 ELSE 0 END) AS pv_num
FROM {{ ref('dwh__events_flat') }}
WHERE 
  event_date = PARSE_DATE('%Y%m%d', '{{ target_date }}')
GROUP BY
  event_date
