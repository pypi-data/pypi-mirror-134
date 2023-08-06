"""juniper show version command output parser """

# ------------------------------------------------------------------------------
from collections import OrderedDict

from facts_finder.common import remove_domain
from facts_finder.common import verifid_output
from facts_finder.common import blank_line
from facts_finder.common import get_string_trailing
from facts_finder.cisco.common import standardize_if
# ------------------------------------------------------------------------------

def get_version(cmd_op, *args):
	# cmd_op = command output in list/multiline string.
	cmd_op = verifid_output(cmd_op)
	op_dict = OrderedDict()
	version, model = "", ""
	for l in cmd_op:
		if blank_line(l): continue
		if l.strip().startswith("#"): continue
		if l.startswith("Junos: "):  version = l.split()[-1]
		if l.startswith("Model: "): model = l.split()[-1]

	if not op_dict.get('version'): op_dict['version'] = version
	if not op_dict.get('model'): op_dict['model'] = model
	return op_dict
# ------------------------------------------------------------------------------
