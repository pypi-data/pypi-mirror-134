# ------------------------------------------------------------------------------

import pandas as pd
# ------------------------------------------------------------------------------

### IDENTIFER OF COMMAND LINE ### >
CMD_LINE_START_WITH = "output for command: "

# ------------------------------------------------------------------------------

def remove_domain(hn):
	return hn.split(".")[0]

def read_file(file):
	with open(file, 'r') as f:
		file_lines = f.readlines()
	return file_lines
# ------------------------------------------------------------------------------

def get_op(file, cmd):
	file_lines = read_file(file)
	toggle, op_lst = False, []
	for l in file_lines:
		if l.find(CMD_LINE_START_WITH)>0:
			toggle = l.find(cmd)>0
			continue
		if toggle:
			op_lst.append(l.strip())
	return op_lst
# ------------------------------------------------------------------------------

def blank_line(line): 
	return not line.strip()

def get_device_manufacturar(file):
	file_lines = read_file(file)
	for l in file_lines:
		if l.startswith("!"): return "Cisco"
		if l.startswith("#"): return "Juniper"
	return "Unidentified"

def verifid_output(cmd_op):
	if isinstance(cmd_op, str):
		cmd_op = cmd_op.split("\n")
	if not isinstance(cmd_op, list):
		raise TypeError("Invalid Command Output Received.\n"
			f"Expected either multiline-string or list, received {type(cmd_op)}.")
	return cmd_op
# ------------------------------------------------------------------------------

def get_string_part(line, begin, end):
	try: return line[begin: end].strip()
	except: raise TypeError("Unrecognized Input")

def get_string_trailing(line, begin_at):
	try: return line[begin_at:].strip()
	except: raise TypeError("Unrecognized Input")
# ------------------------------------------------------------------------------

def standardize_mac(mac):
	return mac.replace(":","").replace(".","")

def mac_2digit_separated(mac):
	mac = standardize_mac(mac)
	for x in range(6):
		if x == 0:  s = mac[:2]
		else: s += ":" + mac[x*2:(x*2)+2]
	return s

def mac_4digit_separated(mac):
	mac = standardize_mac(mac)
	for x in range(3):
		if x == 0:   s  =       mac[:4]
		elif x == 1: s += "." + mac[4:8]
		elif x == 2: s += "." + mac[8:]
	return s

# ------------------------------------------------------------------------------
from collections import MutableMapping
def flatten(d, parent_key='', sep='_'):
	items = []
	if isinstance(d, dict):
		for k, v in d.items():
			new_key = parent_key + sep + k if parent_key else k
			if isinstance(v, MutableMapping):
				items.extend(flatten(v, new_key, sep=sep).items())
			else:
				items.append((new_key, v))
		return dict(items)
	else: return [d]

def dataframe_generate(d):
	new_d = {}
	for k, v in d.items():
		new_d[k] = flatten(v, "")
	return pd.DataFrame(new_d).fillna("").T
# ------------------------------------------------------------------------------
