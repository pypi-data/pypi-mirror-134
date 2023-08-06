"""juniper interface from config command output parser """

# ------------------------------------------------------------------------------
from collections import OrderedDict
from nettoolkit import DIC, JSet

from facts_finder.common import verifid_output
from facts_finder.common import blank_line
from facts_finder.common import get_string_trailing
from facts_finder.juniper.statics import JUNIPER_IFS_IDENTIFIERS
from facts_finder.juniper.common import get_subnet
from facts_finder.juniper.common import get_v6_subnet
from facts_finder.juniper.common import get_vlans_juniper

merge_dict = DIC.merge_dict
# ------------------------------------------------------------------------------

class RunningInterfaces():

	def __init__(self, cmd_op):
		self.cmd_op = cmd_op
		JS = JSet(input_list=cmd_op)
		JS.to_set
		self.set_cmd_op = verifid_output(JS.output)
		self.interface_dict = OrderedDict()

	def interface_read(self, func):
		ports_dict = OrderedDict()
		for l in self.set_cmd_op:
			if blank_line(l): continue
			if l.strip().startswith("#"): continue
			if l.startswith("set interfaces interface-range"): continue
			if not l.startswith("set interfaces"): continue
			spl = l.split()
			int_type = None
			for k, v in JUNIPER_IFS_IDENTIFIERS.items():
				if spl[2].startswith(v):
					int_type = k
					break
			if not int_type: 
				print(f"UndefinedInterface(Type)-{spl[2]}")
				continue
			p = juniper_port(int_type, spl)
			if not p: continue
			if not ports_dict.get(p): ports_dict[p] = {}
			port_dict = ports_dict[p]
			func(port_dict, l, spl)
		return ports_dict


	def interface_ips(self):
		func = self.get_ip_details
		merge_dict(self.interface_dict, self.interface_read(func))

	@staticmethod
	def get_ip_details(port_dict, l, spl):
		subnet = get_v4_subnet(spl, l)
		if not subnet: return		
		port_dict['v4'] = {}
		port_dict['v4']['address'] = get_v4_address(spl, l)
		port_dict['v4']['ip'] = get_v4_ip(spl, l)
		port_dict['v4']['mask'] = get_v4_mask(spl, l)
		port_dict['v4']['subnet'] = subnet

	def interface_v6_ips(self):
		func = self.get_ipv6_details
		merge_dict(self.interface_dict, self.interface_read(func))

	@staticmethod
	def get_ipv6_details(port_dict, l, spl):
		address = get_v6_address(spl, l)
		if not address: return
		link_local = is_link_local(address)
		if not port_dict.get('v6'): port_dict['v6'] = {}
		v6_port_dic = port_dict['v6']
		if link_local :
			if v6_port_dic.get("link-local"): return None
			v6_port_dic['link-local'] = {}
			v6_pd = v6_port_dic['link-local']
		else:
			if v6_port_dic.get("address"): return None
			v6_pd = v6_port_dic
		v6_pd['address'] = address
		v6_pd['ip'] = get_v6_ip(address)
		v6_pd['mask'] = get_v6_mask(address)
		v6_pd['subnet'] = get_v6_subnet(address)


	def interface_vlans(self):
		func = self.get_int_vlan_details
		merge_dict(self.interface_dict, self.interface_read(func))

	@staticmethod
	def get_int_vlan_details(port_dict, l, spl):
		vlans = get_vlans_juniper(spl)
		if not vlans: return None
		if not port_dict.get('vlan'): port_dict['vlan'] = []
		port_dict['vlan'].extend(vlans)


	def interface_mode(self):
		func = self.get_interface_mode
		merge_dict(self.interface_dict, self.interface_read(func))

	@staticmethod
	def get_interface_mode(port_dict, l, spl):
		mode = 'interface-mode' in spl
		if not mode: return None
		if not port_dict.get('port_mode'): port_dict['port_mode'] = spl[-1]




	# # Add more interface related methods as needed.


# ------------------------------------------------------------------------------


def get_interfaces_running(cmd_op, *args):
	""" define set of methods executions. to get interface parameters.
	"""
	R  = RunningInterfaces(cmd_op)
	R.interface_ips()
	R.interface_v6_ips()
	R.interface_vlans()
	R.interface_mode()
	# # update more interface related methods as needed.

	return R.interface_dict



# ------------------------------------------------------------------------------

def juniper_port(int_type, spl):
	if spl[3] == 'unit':
		if spl[2] in ('irb', 'vlan'):
			return spl[4]
		return spl[2]+"."+spl[4]
	else:
		return spl[2]

def get_v4_subnet(spl, line):
	if not is_v4_addressline(line): return None
	return get_subnet(spl[spl.index("address") + 1])

def get_v4_ip(spl, line):
	if not is_v4_addressline(line): return None
	return spl[spl.index("address") + 1].split("/")[0]

def get_v4_address(spl, line):
	if not is_v4_addressline(line): return None
	return spl[spl.index("address") + 1]

def get_v4_mask(spl, line):
	if not is_v4_addressline(line): return None
	return spl[spl.index("address") + 1].split("/")[1]

def is_v4_addressline(line):	
	if line.find("family inet") == -1: return None
	if line.find("address") == -1: return None
	return True
# ------------------------------------------------------------------------------


def get_v6_address(spl, line):
	v6ip = is_v6_addressline(spl, line)
	if not v6ip : return None
	return v6ip

def get_v6_ip(v6ip):
	return v6ip.split("/")[0]

def get_v6_mask(v6ip):
	return v6ip.split("/")[1]

# def get_v6_subnet(v6ip):
# 	return get_v6_subnet(v6ip)

def is_v6_addressline(spl, line):
	if line.find("family inet6") == -1: return None
	try:
		if spl[spl.index('inet6')+1] != 'address': return None
	except: return None
	return spl[spl.index('inet6')+2]

def is_link_local(v6_ip):
	return v6_ip.lower().startswith("fe80:")

# ------------------------------------------------------------------------------
