from __future__ import print_function
import logging
from random import randint
import grpc
import polynomial_pb2
import polynomial_pb2_grpc
import polynomial
import matplotlib.pyplot as plt
import numpy as np
value=[-1.,-0.77777778,-0.55555556, -0.33333333,-0.11111111,0.11111111,0.33333, 0.55555556, 0.77777778 , 1]
answer1=[]
answer2=[]




def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub=polynomial_pb2_grpc.PolynomialStub(channel)
        for i in value:
            request = polynomial_pb2.PolynomialInput(x=i)
            response= polynomial_pb2.PolynomialOutput()
            response= stub.Solve(request)
            answer1.append(response.results.res_x)
            answer2.append(response.results.res_y)
        plt.plot(value,answer1,"g--",label="Polynomial Ordo 5")
        plt.plot(value,answer2,"y--", label="Polynomial Ordo 4")
        plt.grid()
        plt.legend()
        plt.show()




        
        
    




if __name__ == '__main__':
    logging.basicConfig()
    run()