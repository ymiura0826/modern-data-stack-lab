-- macros/generate_schema_name.sql

{% macro generate_schema_name(custom_schema_name, node) -%}

    {%- set fqn = node['fqn'] -%}
    {%- set schema = '_'.join(fqn[1:-1]) -%}

    {{ schema }}

{%- endmacro %}





