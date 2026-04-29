raw_logs = ["16:15", "ERROR", "DB_CONN_FAIL", "TIMEOUT", "RETRY", "USELESS", "TMI"] 

time, level, cause, msg1, msg2, msg3, tmi = raw_logs

print(time, level, cause)

print(tmi)