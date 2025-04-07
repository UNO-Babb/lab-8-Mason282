#ProcessData.py
#Name: Mason Rodgers
#Date: 4/6/25
#Assignment: Lab 8

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
 
  #line = inFile.readline()

  outFile.write("Last Name, First Name, User ID, Major-Year\n")

  for line in inFile:
    data = line.split()
    first = data[0]
    last = data[1]
    idNum = data[3]
    year = data[5]
    major = data[6]

    student_id = makeID(first, last, idNum)
    major_year = makeMajorYear(major, year)
    output = last + "," + first + "," + student_id + "," + major_year + "\n"
    outFile.write(output)
    #print(student_id)

  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

def makeID(first, last, idNum):
  #print(first, last, idNum)
  idLen = len(idNum)

  while len(last) < 5:
    last = last + "x"

  id = first[0] + last+ idNum[idLen - 3: ]

  #print(id)
  return id


def makeMajorYear(major, year):
  maj = major[ :3]
  if year == "Freshman":
    yr = "FR"
  elif year == "Sophomore":
    yr = "SO"
  elif year == "Junior":
    yr = "JR"
  elif year == "Senior":
    yr = "SR"
  else:
    yr = "UN"

  return maj + "-" +yr


if __name__ == '__main__':
  main()
