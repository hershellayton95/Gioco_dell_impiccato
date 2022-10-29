from modulo_prova_calc import Calc
from sys import argv

def main():
    if not len(argv) == 4:
        print ("esempio devi inserire a + b")
    else:
        mycalc = Calc()
        mycalc.setOperando1(int(argv[1]))
        mycalc.setOperazione(argv[2])
        mycalc.setOperando2(int(argv[3]))
        v = mycalc.getResult()
        print (v)
        print(mycalc)


if __name__ == "__main__":
    main()