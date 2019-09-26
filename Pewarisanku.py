class BTS(object):
	def __init__(self, l, ja, t):
		self.label = l
		self.jumlahanggota = ja
		self.tahun = t
		
		
	def cetakData(self):
		print("Label\t\t: ", self.label)
		print("Jumlah Anggota\t: ", self.jumlahanggota)
		print("Tahun Debut\t: ", self.tahun)
		
# mendefinisikan kelas turunan (subclass)
class BT21(BTS):
	def __init__(self, l, ja, t, p):
		self.label = l
		self.jumlahanggota = ja
		self.tahun = t
		self.pencipta = p
	def cetakData(self):
		print("Label\t\t: ", self.label)
		print("Jumlah Anggota\t: ", self.jumlahanggota)
		print("Tahun Debut\t: ", self.tahun)
		print("Pencipta\t: ", self.pencipta)
				
def main():
	#membuat objek BTS
	bts1 = BTS('BigHit', 7, 2013)
	bt211 = BT21('LINE', 8, 2017, 'BTS')
	
	#menggunakan objek
	print('BTS')
	bts1.cetakData()
	
	print(' ')
	print('BT21')
	bt211.cetakData()
	
if __name__ == "__main__":
	main()