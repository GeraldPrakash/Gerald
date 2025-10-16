# Code to take a voice input and output an answer 
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import speech_recognition as sr

def A():
  with open('Electric Field.txt', 'r') as x:
    A = x.read()
    print(A)
  return A
def B():
  with open('Magnetic Field.txt', 'r') as x:
    B = x.read()
    print(B)
  return B
def C():
  with open('Electromagnetism.txt', 'r') as x:
    C = x.read()
    print(C)
  return C
def D():
  with open('Electric and Magnetic Fields.txt', 'r') as x:
    D = x.read()
    print(D)
  return D
def E():
  with open('Electric Charge.txt', 'r') as x:
    E = x.read()
    print(E)
  return E
def F():
  with open('Electromagnetic Spectrum.txt', 'r') as x:
    F = x.read()
    print(F)
  return F
def G():
  with open('Electromagnetic Induction.txt', 'r') as x:
    G = x.read()
    print(G)
  return G
def H():
  with open('Applications of Electromagnetism.txt', 'r') as x:
    H = x.read()
    print(H)
  return H
def I():
  with open('Maxwells Equation.txt', 'r') as x:
    I = x.read()
    print(I)
  return I
def J():
  with open('Electromagnetic Spectrum.txt', 'r') as x:
    J = x.read()
    print(J)
  return J

# Z = input("Type your question:")
# Initialize the recognizer
recognizer = sr.Recognizer()

# Use the microphone as the audio source
with sr.Microphone() as source:
    print("Adjusting for background noise... Please wait.")
    recognizer.adjust_for_ambient_noise(source, duration=2)
    print("Listening... Speak something!")
    audio = recognizer.listen(source)

# Convert speech to text using Google Speech Recognition

print("Recognizing...")
text = recognizer.recognize_google(audio)
print("You said:", text)
Z = text
Y = Z.lower()

T = ['what', 'is', 'show','the','a','list','details','give','report','detail','register']

X = Y.split()

filter = [word for word in X if word.lower() not in T]

key = " ".join(filter)

print("-------------------------------------------------------------")
print (key)
print("-------------------------------------------------------------")

if key =='electric field':
  A()
elif key == 'magnetic field':
  B()
elif key == 'electromagnetism':
  C()
elif key == 'electric and magnetic field' :
  D()
elif key == 'charge':
  E()
elif key == 'induction' :
  F()
elif key == 'application':
  G()
elif key == 'equation':
  H()
elif key == 'spectrum':
  I()
elif key == 'applications of electromagnetism':
    H()
else:
    Z = key

    Z1 = "electric field"
    Z2 = "magnetic field"
    Z3 = "electromagnetism"
    Z4 = "electric and magnetic field"
    Z5 = "charge"
    Z6 = "induction"
    Z7 = "application"
    Z8 = "equation"
    Z9 = "spectrum"
    Z10 = "applications of electromagnetism"

    Y1=fuzz.WRatio(Z, Z1)
    print(Y1)
    Y2=fuzz.WRatio(Z, Z2)
    print(Y2)
    Y3=fuzz.WRatio(Z, Z3)
    print(Y3)
    Y4=fuzz.WRatio(Z, Z4)
    print(Y4)
    Y5=fuzz.WRatio(Z, Z5)
    print(Y5)
    Y6=fuzz.WRatio(Z, Z6)
    print(Y6)
    Y7=fuzz.WRatio(Z, Z7)
    print(Y7)
    Y8=fuzz.WRatio(Z, Z8)
    print(Y8)
    Y9=fuzz.WRatio(Z, Z9)
    print(Y9)
    Y10=fuzz.WRatio(Z, Z10)
    print(Y10)


    if Y1 > 80 :
      M = A()
    elif Y2 > 80 :
      Z= B()
    elif Y3 > 80 :
      Y = C()
    elif Y4 > 80 :
      X = D()
    elif Y5 > 80 :
      W = E()
    elif Y6 > 80 :
      V = F()
    elif Y7 > 80 :
      T = G()
    elif Y8 > 80 :
      T = H()
    elif Y9 > 80 :
      T = I()
    elif Y10 > 80 :
      T = J()
    else:
      print("Invalid input")