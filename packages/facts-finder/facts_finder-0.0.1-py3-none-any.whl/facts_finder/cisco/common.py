
# ------------------------------------------------------------------------------
from nettoolkit import IPv4, IPv6, to_dec_mask

from .statics import CISCO_IFSH_IDENTIFIERS
# ------------------------------------------------------------------------------

# ----------------------------------------------------------
def interface_type(ifname):
	if not ifname: 
		raise ValueError(f"Missing mandatory input ifname")
	for int_type, int_types in  CISCO_IFSH_IDENTIFIERS.items():
		for sub_int_type in int_types:
			if sub_int_type.startswith(ifname):
				return (int_type, sub_int_type)

def standardize_if(ifname, expand=False):
	if not ifname:
		raise ValueError("Missing mandatory input ifname")
	if not isinstance(expand, bool): 
		raise TypeError(f"Invalid value detected for input expand, "
		f"should be bool.")
	if not isinstance(ifname, str): 
		raise TypeError(f"Invalid value detected for input ifname, "
		f"should be str.")
	srcifname = ''
	for i in ifname:
		if not i.isdigit(): srcifname += i
		else: break
	if not srcifname: return None
	try:
		it = interface_type(srcifname)
		if it: 
			int_type, int_pfx = it[0], it[1]
		else:
			return ifname		
	except:
		raise TypeError(f"unable to detect interface type for {srcifname}")
	try:
		shorthand_len = CISCO_IFSH_IDENTIFIERS[int_type][int_pfx]
	except:
		raise KeyError(f"Invalid shorthand Key detected {int_type}, {int_pfx}")
	if expand:  return int_pfx+ifname[len(srcifname):]
	return int_pfx[:shorthand_len]+ifname[len(srcifname):]


def expand_if(ifname):
	return standardize_if(ifname, True)

def expand_if_dict(d):
	return {standardize_if(k, True):v for k, v in d.items()}

def get_interface_cisco(line):
	return standardize_if(line[10:])


# ----------------------------------------------------------
def get_vlans_cisco(line):
	"""returns set of vlan numbers allowed for the interface.
	"""
	vlans = {'trunk': set(), 'access': None, 'voice': None}
	line = line.strip()
	if line.startswith("switchport trunk allowed"):
		vlans['trunk'] = trunk_vlans_cisco(line)
	elif line.startswith("switchport access vlan"):
		vlans['access'] = line.split()[-1]
	elif line.startswith("switchport voice vlan"):
		vlans['voice'] = line.split()[-1]
	else:
		return None
	return vlans

def trunk_vlans_cisco(line):
	for i, s in enumerate(line):
		if s.isdigit(): break
	line = line[i:]
	# vlans_str = line.split()[-1]
	# vlans = vlans_str.split(",")
	line = line.replace(" ", "")
	vlans = line.split(",")
	if not line.find("-")>0:
		return vlans
	else:
		newvllist = []
		for vlan in vlans:
			if vlan.find("-")==-1: 
				newvllist.append(vlan)
				continue
			splvl = vlan.split("-")
			for vl in range(int(splvl[0]), int(splvl[1])+1):
				newvllist.append(vl)
		return set(newvllist)
# ---------------------------------------------------------------

def get_subnet(address):
	return IPv4(address).subnet_zero()
def get_inet_address(line):
	if line.strip().startswith("ip address "):
		spl = line.split()
		ip  = spl[-2]
		mask = to_dec_mask(spl[-1])
		s = ip+"/"+str(mask)
		return s
	return None

def get_v6_subnet(address):
	return IPv6(address).subnet_zero()
def get_inetv6_address(line, link_local):
	v6idx = -2 if link_local else -1
	if line.strip().startswith("ipv6 address "):
		spl = line.split()
		ip  = spl[v6idx]
		return ip
	return None

def get_int_ip(ip): return ip.split("/")[0]
def get_int_mask(ip): return ip.split("/")[-1]


# ---------------------------------------------------------------





