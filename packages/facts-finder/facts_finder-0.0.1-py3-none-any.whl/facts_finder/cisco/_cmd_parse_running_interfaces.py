"""cisco running-config command output parser """

# ------------------------------------------------------------------------------
from collections import OrderedDict
from nettoolkit import DIC

from facts_finder.cisco.common import standardize_if
from facts_finder.common import verifid_output
from facts_finder.common import blank_line
from facts_finder.cisco.common import get_interface_cisco
from facts_finder.cisco.common import get_inet_address
from facts_finder.cisco.common import get_subnet
from facts_finder.cisco.common import get_int_ip
from facts_finder.cisco.common import get_int_mask
from facts_finder.cisco.common import get_vlans_cisco
from facts_finder.cisco.common import get_v6_subnet
from facts_finder.cisco.common import get_inetv6_address

merge_dict = DIC.merge_dict
# ------------------------------------------------------------------------------

class RunningInterfaces():

	def __init__(self, cmd_op):
		self.cmd_op = verifid_output(cmd_op)
		self.interface_dict = OrderedDict()

	def interface_read(self, func):
		int_toggle = False
		ports_dict = OrderedDict()
		for l in self.cmd_op:
			if blank_line(l): continue
			if l.strip().startswith("!"): 
				int_toggle = False
				continue
			if l.startswith("interface "):
				p = get_interface_cisco(l)
				if not p: continue
				if not ports_dict.get(p): ports_dict[p] = {}
				port_dict = ports_dict[p]
				int_toggle = True
				continue
			if int_toggle:
				func(port_dict, l)
		return ports_dict

	def interface_ips(self):
		func = self.get_ip_details
		merge_dict(self.interface_dict, self.interface_read(func))

	@staticmethod
	def get_ip_details(port_dict, l):
		address = get_inet_address(l)
		# print(address)
		if not address: return None
		port_dict['v4'] = {}
		port_dict['v4']['address'] = address
		port_dict['v4']['ip'] = get_int_ip(address)
		port_dict['v4']['mask'] = get_int_mask(address)
		port_dict['v4']['subnet'] = get_subnet(address)


	def interface_v6_ips(self):
		func = self.get_ipv6_details
		merge_dict(self.interface_dict, self.interface_read(func))

	@staticmethod
	def get_ipv6_details(port_dict, l):
		link_local = l.find("link-local") > -1
		address = get_inetv6_address(l, link_local)
		if not address: return None
		if not port_dict.get('v6'): port_dict['v6'] = {}
		if link_local:
			port_dict['v6']['link-local'] = {}
			pd = port_dict['v6']['link-local']
			pd['address'] = address
			return None
		pd = port_dict['v6']
		pd['address'] = address
		pd['ip'] = get_int_ip(address)
		pd['mask'] = get_int_mask(address)
		pd['subnet'] = get_v6_subnet(address)


	def interface_vlans(self):
		func = self.get_int_vlan_details
		merge_dict(self.interface_dict, self.interface_read(func))

	@staticmethod
	def get_int_vlan_details(port_dict, l):
		vlans = get_vlans_cisco(l)
		if not vlans: return None
		port_dict['vlan'] = vlans

	# # Add more interface related methods as needed.


# ------------------------------------------------------------------------------


def get_interfaces_running(cmd_op, *args):
	""" define set of methods executions. to get interface parameters.
	"""
	R  = RunningInterfaces(cmd_op)
	R.interface_ips()
	R.interface_v6_ips()
	R.interface_vlans()
	# # update more interface related methods as needed.

	return R.interface_dict

