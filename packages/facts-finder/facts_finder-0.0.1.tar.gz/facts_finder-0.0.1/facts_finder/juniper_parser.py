
# ------------------------------------------------------------------------------
from collections import OrderedDict

from facts_finder.juniper import get_lldp_neighbour
from facts_finder.juniper import get_int_description
from facts_finder.juniper import get_chassis_hardware
from facts_finder.juniper import get_arp_table
from facts_finder.juniper import get_interfaces_running
from facts_finder.juniper import get_version
from facts_finder.common import get_op
from facts_finder.device import DevicePapa
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# // Cisco //
# ------------------------------------------------------------------------------
# COMMANDS LIST DICTIONARY, DEFINE **kwargs as dictionary in command value     #
# ------------------------------------------------------------------------------
juniper_cmds_list = OrderedDict([
	('show lldp neighbors', {'dsr': True}),		# dsr = domain suffix removal
	('show configuration', {}),
	('show version', {}),
	('show interfaces descriptions', {}),
	('show chassis hardware', {}),
	('show arp', {}),
	## ADD More as grow ##
])
# ------------------------------------------------------------------------------
# COMMAND OUTPUT HIERARCHY LEVEL
# ------------------------------------------------------------------------------
juniper_cmds_op_hierachy_level = {
	'show lldp neighbors': 'Interfaces',
	'show configuration': 'Interfaces',
	'show version': 'system',
	'show interfaces descriptions': 'Interfaces',
	'show chassis hardware': 'Interfaces',
	'show arp': 'arp',
	## ADD More as grow ##
}
# ------------------------------------------------------------------------------
# Dict of Juniper commands, %trunked commands mapped with parser func.
# ------------------------------------------------------------------------------
juniper_commands_parser_map = {
	'show lldp neighbors': get_lldp_neighbour,
	'show configuration': get_interfaces_running,
	'show version': get_version,
	'show interfaces descriptions': get_int_description,
	'show interfaces terse': None,
	'show chassis hardware': get_chassis_hardware,
	'show arp': get_arp_table,
	'show bgp summary': None,
}
# ------------------------------------------------------------------------------

def absolute_command(cmd, cmd_parser_map, op_filter=False):
	"""returns absolute full command for shorteened cmd
	if founds an entry in cmd_parser_map keys.
	"""
	if op_filter:
		abs_cmd = cmd.split("|")[0].strip()
	else:
		abs_cmd = cmd.replace("| no-more", "").strip()
	for c_cmd in cmd_parser_map:
		word_match = abs_cmd == c_cmd
		if word_match: break
	if word_match:  return abs_cmd
	return cmd

# ------------------------------------------------------------------------------
class Juniper(DevicePapa):
	
	def __init__(self, file):
		super().__init__(file)

	def parse(self, cmd, *arg, **kwarg):
		abs_cmd = absolute_command(cmd, juniper_commands_parser_map)
		parse_func = juniper_commands_parser_map[abs_cmd]
		if isinstance(parse_func, tuple):
			parsed_op = [self.run_parser(pf, abs_cmd, *arg, **kwarg) for pf in parse_func]
		else:
			parsed_op = self.run_parser(parse_func, abs_cmd, *arg, **kwarg)
		return parsed_op

	def run_parser(self, parse_func, abs_cmd, *arg, **kwarg):
		op_list = get_op(self.file, abs_cmd)		
		if not parse_func: return None
		po = parse_func(op_list, *arg, **kwarg)
		return po

# ------------------------------------------------------------------------------
