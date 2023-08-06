"""juniper interface description command output parser """

# ------------------------------------------------------------------------------
from collections import OrderedDict

from facts_finder.common import remove_domain
from facts_finder.common import verifid_output
from facts_finder.common import blank_line
from facts_finder.common import get_string_trailing
from facts_finder.cisco.common import standardize_if
# ------------------------------------------------------------------------------

def get_chassis_hardware(cmd_op, *args):
	# cmd_op = command output in list/multiline string.
	# arg = DeviceDB object from merger
	cmd_op = verifid_output(cmd_op)
	op_dict = OrderedDict()
	toggle = False
	JCH = JuniperChassisHardware(cmd_op)
	for arg in args:
		ports = arg['Interfaces']
		break
	for p, port_attr in  ports.items():	
		sfp = JCH.get_sfp(p)
		if not sfp: continue
		op_dict[p] = {}
		op_dict[p]["port_type"] = sfp
	return op_dict


class JuniperChassisHardware():
	"""read the show chassis hardware output from juniper and returns port type(sfp)"""
	def __init__(self, output):
		self.fpc, self.pic = '', ''
		self.port = ''
		self.ports = {}
		self.read(output)

	def read(self, output):
		for l in output:
			if not l.strip(): continue
			self.add(l)

	def add(self, line):
		# if line.upper().find("BUILTIN") > 0: return         # Some of juniper output are incosistent so removed.
		spl = line.strip().split()
		if not spl[0].upper() in ("FPC", "PIC", "XCVR"): return
		if spl[0].upper() in ("FPC"):
			self.fpc = spl[1]
			self.pic = ''
		elif spl[0].upper() in ("PIC"):
			self.pic = self.fpc + "/" + spl[1]
		elif spl[0].upper() in ('XCVR',):
			self.port = self.pic + "/" + spl[1]
			self.ports[self.port] = spl[-1]
			self.port=''

	def get_sfp(self, port):
		"""return port type/sfp for given port"""
		for p, sfp in self.ports.items():
			spl_port = port.split("-")
			if spl_port[-1] == p:
				return sfp
		return ""

