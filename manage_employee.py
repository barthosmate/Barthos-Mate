from employee import Employee

class ManageEmployee:
	 
	def _init_( self ):

		self.rowList = []
		self.readFile()
		self.countEmployee()
		self.sumMiskolcSal()
		self.szegedWrite ()
		
	def readFile( self ):
		 
		print( "Első feladat: fájl beolvasás" )
		file = open( "employee.txt", "r" )
		file.readline()
		 
		row = file.readline()
		while( row ):
			
			rowS = row.split( ":" )
			emp = Employee()
			emp.name = rowS[0]
			emp.city = rowS[1]
			emp.address = rowS[2]
			emp.salary = rowS[3]
			emp.bonus = rowS[4]
			emp.borndate = rowS[5]
			emp.hiredate = rowS[6]
			
			rowList.append( emp )
			row = file.readline()
		
		file.close()
		print("Sikeres beolvasás")

	def countEmployee( self ):
		
		print("Második feladat: Dolgozók megszámlálása")
		counter = 0;
		for i in self.rowList:
			counter += 1
			
		print("A dolgozók száma: {:10}".format( counter ))


	def sumMiskolcSal( self ):
		print( "A harmadik feladat: Miskolci fizetések összegzése" )
		sumSalary = 0
		for emp in self.rowList:
			
			
			
			if( employee.city == "Miskolc" ):
				
				sumSalary += int( employee.salary )
			
		print( "Miskolciak fizetése: {:10}".format( sumSalary ))
		
	def szegedWrite( self ):
		
		print( "A harmadik feladat: Szeg edi fizetések fájlbairása" )
		sumSalary = 0
		for emp in self.rowList:
			
			
			
			if( employee.city == "Szeged" ):
				
				sumSalary += int( employee.salary )
			
		
		wFile = open ( "Szegedi.txt", "w" )
		wfile.write( "Stegediek fizetése: " +str( sumSalary ))
		
		wFile.close()
		print( "Sikeres kiirás" )


ManageEmployee()
