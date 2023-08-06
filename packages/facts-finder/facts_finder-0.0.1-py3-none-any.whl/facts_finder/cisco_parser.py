
# ------------------------------------------------------------------------------
from collections import OrderedDict

from facts_finder.common import read_file
from facts_finder.device import DevicePapa
from facts_finder.cisco import get_cdp_neighbour
from facts_finder.cisco import get_lldp_neighbour
from facts_finder.cisco import get_interface_status
from facts_finder.cisco import get_interface_description
from facts_finder.cisco import get_mac_address_table
from facts_finder.cisco import get_arp_table
from facts_finder.cisco import get_interfaces_running, get_system_running
# ------------------------------------------------------------------------------

CMD_LINE_START_WITH = "output for command: "
LEN_CMD_LINE = len(CMD_LINE_START_WITH)

# ------------------------------------------------------------------------------
# // Cisco //
# ------------------------------------------------------------------------------
# COMMANDS LIST DICTIONARY, DEFINE **kwargs as dictionary in command value     #
# ------------------------------------------------------------------------------
cisco_cmds_list = OrderedDict([
	('sh lldp nei', {'dsr': True}),			# dsr = domain suffix removal
	('sh cdp nei', {'dsr': True}),			# dsr = domain suffix removal
	('sh int status', {}),
	('sh int desc', {}),
	('show mac address-table', {}),
	('sh ip arp', {}),
	('sh run', {}),
	## ADD More as grow ##
])
# ------------------------------------------------------------------------------
# COMMAND OUTPUT HIERARCHY LEVEL ( key need to match with 'cisco_cmds_list' )
# ------------------------------------------------------------------------------
cisco_cmds_op_hierachy_level = {
	'sh lldp nei': 'Interfaces',
	'sh cdp nei': 'Interfaces',
	'sh int status': 'Interfaces',
	'sh int desc': 'Interfaces',
	'show mac address-table': 'arp',
	'sh ip arp': 'arp',
	'sh run': ('Interfaces', 'system'),
	## ADD More as grow ##
}
# ------------------------------------------------------------------------------
# Dict of cisco commands, %full commands in keys mapped with parser func.
# ------------------------------------------------------------------------------
cisco_commands_parser_map = {
	'show lldp neighbors': get_lldp_neighbour,
	'show cdp neighbors': get_cdp_neighbour,
	'show interfaces status': get_interface_status,
	'show interfaces description': get_interface_description,
	'show mac address-table': get_mac_address_table,
	'show ip arp': get_arp_table,
	'show running-config': (get_interfaces_running, get_system_running),
}

# ------------------------------------------------------------------------------
def absolute_command(cmd, cmd_parser_map):
	"""returns absolute full command for shorteened cmd
	if founds an entry in cmd_parser_map keys.
	"""
	spl_cmd = cmd.split()
	for c_cmd in cmd_parser_map:
		spl_c_cmd = c_cmd.split()
		for i, word in enumerate(spl_cmd):
			try:
				word_match = spl_c_cmd[i].startswith(word)
				if not word_match: break
			except:
				word_match = False
				break
		if word_match: break
	if word_match:  return c_cmd
	return cmd

# get_op_cisco() returns output of a command in list format found from capture file.
# this is differ from general get_op() in a way that it has to get absolute command
# in case if provided trunked while capture. Juniper does auto-complete at terminal
# so it does not require that step.
def get_op_cisco(file, abs_cmd, cmd_parser_map):
	file_lines = read_file(file)
	toggle, op_lst = False, []
	for l in file_lines:
		if l.find(CMD_LINE_START_WITH)>0:
			cmd_line_cmd = absolute_command(l[LEN_CMD_LINE+1:].strip(), cmd_parser_map)
			toggle = abs_cmd == cmd_line_cmd
			continue
		if toggle:
			op_lst.append(l.strip())
	return op_lst

# ------------------------------------------------------------------------------
class Cisco(DevicePapa):
	
	def __init__(self, file):
		super().__init__(file)

	def parse(self, cmd, *arg, **kwarg):
		abs_cmd = absolute_command(cmd, cisco_commands_parser_map)
		parse_func = cisco_commands_parser_map[abs_cmd]
		if isinstance(parse_func, tuple):
			parsed_op = [self.run_parser(pf, abs_cmd, *arg, **kwarg) for pf in parse_func]
		else:
			parsed_op = self.run_parser(parse_func, abs_cmd, *arg, **kwarg)
		return parsed_op

	def run_parser(self, parse_func, abs_cmd, *arg, **kwarg):
		op_list = get_op_cisco(self.file, abs_cmd, cisco_commands_parser_map)
		if not parse_func: return None		
		po = parse_func(op_list,*arg, **kwarg)
		return po
# ------------------------------------------------------------------------------
