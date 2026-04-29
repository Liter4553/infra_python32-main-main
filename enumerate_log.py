#logs = ["Login Success", "Attack Detected", "Logout"]
#
#for i, msg in enumerate(logs, start=1):
#    if "Attack" in msg:
#        print(f"{i}----{msg}")
#


logs = ["Login Success", "Attack Detected", "Logout"]
attack_msg_list = [for i, msg in enumerate(logs, start=1) if "Attack" in msg attack_msg_list.append(f"{i}----{msg}")]
#for i, msg in enumerate(logs, start=1):
#    i
#        attack_msg_list.append(f"{i}----{msg}")
#
print(attack_msg_list) 