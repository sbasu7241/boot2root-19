
import numpy as np
from numpy.linalg import inv

def input():
  
  plainarray=[]
  keyarray = []
  plaintext = "ACT"
  keytext = "GYBNQKURP"
  
  
 #Encryption


  plainarray= list([(ord(plaintext[i])-65) for i,iterator in enumerate(plaintext)])
  keyarray= list([(ord(keytext[i])-65) for i,iterator in enumerate(keytext)])
  n = len(plainarray)

  mylist = [keyarray[i * n:(i + 1) * n] for i in range((len(keyarray) + n - 1) // n )]

  a = np.array(mylist)
  b = np.vstack(plainarray)

  cipher = a.dot(b)%26

  
  #Decryption given cipher and key find plaintext
  det = np.linalg.det(a)
  print(det)
  inva = inv(a)
  print(inva)



  
  



input()


