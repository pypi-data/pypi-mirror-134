"""cisco arp table command output parser """

# ------------------------------------------------------------------------------
from facts_finder.cisco.common import standardize_if
from facts_finder.common import verifid_output
from facts_finder.common import blank_line
from facts_finder.common import standardize_mac
from facts_finder.common import mac_4digit_separated
from facts_finder.common import mac_2digit_separated

# ------------------------------------------------------------------------------

def get_arp_table(cmd_op, *args):
	# cmd_op = command output in list/multiline string.
	cmd_op = verifid_output(cmd_op)
	op_dict = {}
	start = False
	for l in cmd_op:
		if blank_line(l): continue
		if l.strip().startswith("!"): continue
		if l.startswith("Protocol"): continue
		if l.find("Incomplete")>0: continue
		if l.strip().startswith("%") and l.endswith("does not exist."): continue
		spl = l.strip().split()
		try:
			p = standardize_if(spl[-1])
			_mac = standardize_mac(spl[3])
			ip = spl[1]
		except:
			pass
		if not op_dict.get(p): op_dict[p] = {'arps': {}}
		port = op_dict[p]['arps']
		if not port.get(_mac): port[_mac] = set()
		port[_mac].add(ip)
	return op_dict
# ------------------------------------------------------------------------------
