cpu_log = [50,43,98,42,30]

warning_cpu = [str(cpu_usage)+"%" for cpu_usage in cpu_log if cpu_usage >= 80]
print(warning_cpu)