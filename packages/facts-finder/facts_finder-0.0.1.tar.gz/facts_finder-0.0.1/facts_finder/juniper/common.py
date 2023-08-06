# ------------------------------------------------------------------------------
from nettoolkit import IPv4, IPv6, to_dec_mask

# ------------------------------------------------------------------------------

def get_subnet(address):
	return IPv4(address).subnet_zero()
def get_v6_subnet(address):
	return IPv6(address).subnet_zero()

def get_vlans_juniper(spl):
	memberlist_identifiers = ('vlan-id-list', 'members')
	is_any_members = False
	for memid in memberlist_identifiers:
		is_any_members = memid in spl
		if is_any_members: break
	if not is_any_members: return None
	int_vl_list = [int(vl) for vl in spl[spl.index(memid)+1:] if vl.isdigit()]
	return int_vl_list


# ------------------------------------------------------------------------------
