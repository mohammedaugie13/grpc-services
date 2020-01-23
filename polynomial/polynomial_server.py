import logging
import grpc
import time
from concurrent import futures
import polynomial
import polynomial_pb2
import polynomial_pb2_grpc

class Polynomial(polynomial_pb2_grpc.PolynomialServicer):
    def Solve(self, request, context):
        response=polynomial_pb2.PolynomialOutput()
        response.results.res_x, response.results.res_y=polynomial.f(request.x)
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    polynomial_pb2_grpc.add_PolynomialServicer_to_server(Polynomial(),server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()