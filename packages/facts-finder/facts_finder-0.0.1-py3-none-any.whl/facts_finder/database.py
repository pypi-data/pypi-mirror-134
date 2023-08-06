# ------------------------------------------------------------------------------
# class, method,  function  defining the excel database write/read operations.
# read_xl = to read file
# append_to_xl = to append to an existing file.
# write_to_xl = to create a new file and write.
# ------------------------------------------------------------------------------
"""database operations"""

# ------------------------------------------------------------------------------
from collections import OrderedDict
import pandas as pd
# ------------------------------------------------------------------------------
__ver__ = "0.0.1"


def read_xl(file):
	"""reads Excel file and return object XL_READ"""
	xlrd = XL_READ(file)
	xlrd.read_sheets()
	return xlrd

def append_to_xl(file, df_dict, overwrite=True):
	"""appends dictionary of dataframes to an Excel file
	overwrite: will append data to existing file, else create a copy and 
	adds data to it
	"""
	try:
		xlrd = read_xl(file)
		prev_dict = xlrd.df_dict
	except:
		prev_dict = {}
	prev_dict.update(df_dict)
	write_to_xl(file, prev_dict, overwrite=overwrite)

def write_to_xl(file, df_dict, index=False, overwrite=False):
	"""Create a new Excel file with provided dictionary of dataframes
	overwrite: removes existing file, else create a copy if file exist.	
	"""
	XL_WRITE(file, df_dict=df_dict, index=index, overwrite=overwrite)
# ------------------------------------------------------------------------------

class XL_READ:
	""" reads an existing Excel file provide absolute path along with filename as xl
	provide sheet_name in order to read only a particular sheet only. otherwise
	all sheets will be read and stored under `df_dict` attribute.
	"""
	def __init__(self, xl, sheet_name=None):
		self.df_dict = OrderedDict()
		self.sheet_name = sheet_name
		self.xl = pd.ExcelFile(xl)
		self.sheet_names = self.xl.sheet_names

	def __len__(self): return len(self.df_dict)
	def __iter__(self):
		for sheet, dataframe in self.df_dict.items(): yield (sheet, dataframe)		
	def __getitem__(self, key): return self.df_dict[key]
	def __setitem__(self, key, value): self.df_dict[key] = value

	def read_sheets(self):
		if self.sheet_name:
			self[self.sheet_name] = self.xl.parse(sheet_name)
		else:
			for sheet_name in self.sheet_names:
				self[sheet_name] = self.xl.parse(sheet_name)

# ------------------------------------------------------------------------------
class XL_WRITE():
	"""write to an Excel file
	name: file name with absolute path and extension
	df_dict: provide the dictionary of dataframes. where keys will be excel 
	         tab names and values will be dataframe
	index: whether to add index column or not
	overwrite: whether to overwrite the file (if exist) or not
	"""
	def __init__(self, name, df_dict, index=False, overwrite=False):
		self.write(name, df_dict, index, overwrite)

	def write(self, name, df_dict, index, overwrite):
		"""write to file"""
		fileName = name if overwrite else self.get_valid_file_name(name)
		with pd.ExcelWriter(fileName) as writer_file:			
			for sht_name, df in df_dict.items():
				df.to_excel(writer_file, sheet_name=sht_name, index=index)

	def copy_of_file(self, file, n):
		"""create a valid available file name"""
		spl_file =  file.split(".")
		name = ".".join(spl_file[:-1])
		extn = spl_file[-1]
		next_num = f'' if n == 1 else f' ({str(n)})'
		return f'{name} - Copy{next_num}.{extn}'

	def get_valid_file_name(self, file):
		"""create a valid available file name"""
		n = 0
		file_name = file
		while True:
			try:
				XL_READ(file)
				n += 1
				file = self.copy_of_file(file_name, n)
			except:
				break
		return file

# ------------------------------------------------------------------------------

__all__ = ['read_xl', 'append_to_xl', 'write_to_xl']
# ------------------------------------------------------------------------------
