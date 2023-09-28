from data_diff import connect_to_table, diff_tables

# import duckdb

source_conn_info = {
    'driver': 'duckdb',
    'filepath': 'source.duckdb',
}

target_conn_info = {
    'filepath': 'target.duckdb',
    'driver': 'duckdb'
}

source = connect_to_table(db_info=source_conn_info, table_name='development.raw_customers', key_columns='id')
target = connect_to_table(db_info=target_conn_info, table_name='development.raw_orders', key_columns='id')

xdb_data_diffs = list(diff_tables(source, target))

print(xdb_data_diffs)