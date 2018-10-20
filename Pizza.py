
import random
import math
import sys

class Pizza:
	
	def findIntersectionXValueBetweenFunc_iAndFunc_j(m1, m2, x1, x2, y1, y2):
		return ((y1 - y2) + (m2 * x2) - (m1 * x1)) / (m2 - m1)

	def findYValueFromXValueAndEquation(x, m, x1, y1):
		return m * (x - x1) + y1

	def checkIfInUnitCircle(t):
		return (t[0] * t[0] + t[1] * t[1]) < 1
	def GiveCurrentIntersectionsSet(x, IntersectionXs):
		for i in IntersectionXs:
			if (abs(i - x) < 0.000001):
				return IntersectionXs
		IntersectionXs.add(x)
		return IntersectionXs
	def giveListOfLines(n):
		arrayOfLines = []
		for i in range(0, n):
		
			theta1 = random.random()*2*math.pi
			x1 = math.cos(theta1)
			y1 = math.sin(theta1)

			theta2 = random.random()*2*math.pi			
			x2 = math.cos(theta2)
			y2 = math.sin(theta2)

			arrayOfLines += [((x1, y1),(x2, y2))]
		return arrayOfLines
	def GiveListOfSlopes(arrayOfLines):
		arrayOfSlopes = []
		for i in range(len(arrayOfLines)):
			dx = arrayOfLines[i][0][0] - arrayOfLines[i][1][0]
			dy = arrayOfLines[i][0][1] - arrayOfLines[i][1][1]
			m = dy / dx 
			arrayOfSlopes += [m]
		return arrayOfSlopes
	def giveIntersectionPointBetweenLines_i_and_j(i, j, arrayOfSlopes, arrayOfLines):
		m1 = arrayOfSlopes[i]
		m2 = arrayOfSlopes[j]

		x1 = arrayOfLines[i][0][0]
		x2 = arrayOfLines[j][0][0]

		y1 = arrayOfLines[i][0][1]
		y2 = arrayOfLines[j][0][1]

		x = Pizza.findIntersectionXValueBetweenFunc_iAndFunc_j(m1, m2, x1, x2, y1, y2)
		y = Pizza.findYValueFromXValueAndEquation(x, m1, x1, y1)

		return (x, y)
				
	def main():
		n = 3

		IntersectionXs = set()
		arrayOfLines = []	
		arrayOfSlopes = []

		vertices = 0
		edges = 0

		
		arrayOfLines = Pizza.giveListOfLines(n)		
		arrayOfSlopes = Pizza.GiveListOfSlopes(arrayOfLines)

		for i in range(0, len(arrayOfLines)):
			for j in range(i, len(arrayOfLines)):
				if (arrayOfLines[i] == arrayOfLines[j]):
					continue
				else:
					p = Pizza.giveIntersectionPointBetweenLines_i_and_j(i, j, arrayOfSlopes, arrayOfLines)
					if (Pizza.checkIfInUnitCircle(p)):
						pX = p[0]
						IntersectionXs = Pizza.GiveCurrentIntersectionsSet(pX, IntersectionXs)
						edges += 2

				
		Vertices = len(IntersectionXs)+6
		Edges = edges + 9
		Faces = 1 - Vertices + Edges
		sys.stdout.write("Vertices: " + str(Vertices))
		sys.stdout.write("\n")
		sys.stdout.write("Edges: " + str(Edges) + "\n")
		sys.stdout.write("Faces: " + str(Faces) + "\n")
if __name__ == '__main__':
	Pizza.main()					
	


