"""cisco interface description command output parser """

# ------------------------------------------------------------------------------
from facts_finder.cisco.common import standardize_if
from facts_finder.common import verifid_output
from facts_finder.common import blank_line
from facts_finder.common import get_string_part
from facts_finder.common import get_string_trailing
# ------------------------------------------------------------------------------

def get_interface_description(cmd_op, *args):
	# cmd_op = command output in list/multiline string.
	cmd_op = verifid_output(cmd_op)
	int_desc_dict = {}
	start = False
	for l in cmd_op:
		if blank_line(l): continue
		if l.strip().startswith("!"): continue
		if l.startswith("Interface"): 
			desc_begin_at = l.find("Description")
			continue
		spl = l.strip().split()
		p = standardize_if(spl[0])
		if not int_desc_dict.get(p): 
			int_desc_dict[p] = {}
		port = int_desc_dict[p]
		port['description'] = get_string_trailing(l, desc_begin_at)
	return int_desc_dict
# ------------------------------------------------------------------------------
