# Windchill Metric Config

Configuration parser for windchill prometheus metrics. Parses json and yaml configuration files into a Python object.


## yaml
```yaml
system:
  process_real_memory_total_bytes: true                                         # system total memory in bytes
  process_real_memory_used_bytes: false                                         # system used memory in bytes
  process_cpu_usage_percent: false                                              # cpu utilisation in percent
  process_disc_total_bytes: false                                               # total disc space in bytes
  process_disc_used_bytes: false                                                # used disc space in bytes
  process_users_total_count: false                                              # count of logged in users on os
  system_boot_timestamp: false                                                  # boot timestamp as label
  system_stats_info: false                                                      # various information about the host system, like os version or processor info
  network:
    process_network_bytes_sent: false                                           # bytes sent over all network addresses
    process_network_packets_recv: false                                         # bytes received over all network addresses
    process_network_err_in: false                                               # total number of errors while receiving
    process_network_err_out: false                                              # total number of errors while sending
    process_network_drop_in: true                                               # total number of incoming packets which were dropped
    process_network_drop_out: false                                             # total number of outgoing packets which were dropped (always 0 on macOS and BSD)
windchill:
  windchill_apache_status: false                                                # windchill apache status (0=not running, >1=http code)
  windchill_windchill_status: false                                             # windchill app status (0=not running, >1=http code)
  windchill_api_response_time_seconds: false                                    # windchill api (/Windchill/api/v1/publishmonitor/getworkerinfo.jsp) response time
  windchill_active_users_total: false                                           # windchill total active users count
  windchill_version_info: false                                                 # windchill version and release info
  method_server:
    windchill_server_status_runtime_start_time: false                           # windchill apache status (0=not running, >1=http code)
    windchill_server_status_runtime_uptime: false                               # windchill apache status (0=not running, >1=http code)
  queue_worker:
    windchill_worker_status: false                                              # windchill worker status (0=not running, 1=ok, 2=fails to start)
    windchill_queue_jobs_failed: false                                          # windchill failed jobs queue count
    windchill_queue_jobs_total: false                                           # windchill total jobs queue count
  garbage_collector:
    windchill_server_status_gc_time_spent_in_threshold_percent: false           # Garbage collection time spent in threshold percent
    windchill_server_status_gc_recent_time_spent_percent: false                 # Garbage collection time spent recent percent
    windchill_server_status_gc_overall_time_spent_percent: false                # Garbage collection time spent overall percent
  memory:
    windchill_server_status_memory_heap_usage_threshold_percent: false          # Heap memory usage threshold in percent
    windchill_server_status_memory_heap_usage_percent: false                    # Heap memory usage in percent
    windchill_server_status_memory_perm_gen_usage_threshold_percent: false      # Perm gen memory usage threshold in percent
    windchill_server_status_memory_perm_gen_usage_percent: false                # Perm gen memory usage in percent
  method_context:
    windchill_server_status_mc_active_contexts_average: false                   # active context average
    windchill_server_status_mc_active_contexts_end: false
    windchill_server_status_mc_active_contexts_max: false
    windchill_server_status_mc_active_contexts_start: false
```
## upload to pypi.org
```bash
py -m build
py -m twine upload --repository pypi dist/*
```