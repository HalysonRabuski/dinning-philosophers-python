import threading
import sys
import time
from random import randrange

# comida = 10

class Philosopher (threading.Thread):

    def __init__(self, numero, GarfoEsquerdo, GarfoDireito, vizinhoEsquerda):
        threading.Thread.__init__(self)
        self.numero = numero            # philosopher numero
        self.GarfoEsquerdo = GarfoEsquerdo
        self.GarfoDireito = GarfoDireito
        self.estado = 1  # 0-faminto 1-pensando
        self.vizEsq = vizinhoEsquerda


    def run(self):
        n = 5
        # global comida
        # self.semaforo.acquire()
        for i in range(n):
            self.estado = 1
            time.sleep(randrange(3)+1) #pensa durante 1 a 4 segundos
            print("Filósofo %s com fome" %self.numero, flush=True)
            # time.sleep(0.2)
            if(self.numero%2==0):
                self.GarfoEsquerdo.pegar(self.numero, 'esquerdo', self.GarfoDireito)
                self.GarfoDireito.pegar(self.numero, 'direito', self.GarfoEsquerdo)
            else:
        # time.sleep(0.5)
                self.GarfoDireito.pegar(self.numero, 'direito', self.GarfoEsquerdo)
                self.GarfoEsquerdo.pegar(self.numero, 'esquerdo', self.GarfoDireito)
            # time.sleep(0.4)
            sys.stdout.write("Filósofo %s comendo" %self.numero+"\n")
            sys.stdout.flush()
            time.sleep(randrange(2)+1) #demora entre 1 a 3 segundos para comer
            # comida -= 1
            # time.sleep(0.1)
            self.GarfoEsquerdo.soltar(self.numero, 'esquerda')
            # print("Filósofo %s soltando garfo esquerdo" %self.numero)
            self.GarfoDireito.soltar(self.numero, 'direita')
            sys.stdout.write("Filósofo "+ str(self.numero) + "voltou a pensar"+"\n")
            sys.stdout.flush()
            self.estado = 1

        sys.stdout.write("Filósofo "+ str(self.numero) +" comeu "+str(n)+" vezes e está satisfeito! \n")
        sys.stdout.flush()

class Garfo (object):

    def __init__(self, nFilo):
        # threading.Thread.__init__(self)
        self.filosofo = -2
        self.ocupado = 0
        # self.gEsquerda = gEsquerda
        self.sem = threading.Semaphore()
        # self.timer = 0

    def pegar(self, filosofo, lado, outroGarfo):
        self.sem.acquire()
        self.ocupado = 1
        sys.stdout.write("Filósofo "+ str(filosofo) +" pegando garfo " + lado+" \n")
        sys.stdout.flush()
        self.filosofo = filosofo


    def soltar(self, filosofo, lado):
        sys.stdout.write("Filósofo "+ str(filosofo) +" soltando garfo " + lado+" \n")
        sys.stdout.flush()
        time.sleep(0.1)
        self.filosofo = -2
        self.ocupado = 0
        self.sem.release()

def main():

    g = [Garfo(i) for i in range(5)]
        
    f = [Philosopher(i+1, g[i], g[(i+1)%5], 0) for i in range(5)]

    # filo = [Philosopher(i, g[i], g[(i+1)%5], f[(i-1)%5]) for i in range(5)]
    
    for i in range(5):
        f[i].start()


if __name__ == "__main__":
    main()