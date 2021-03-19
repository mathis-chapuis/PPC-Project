#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#
import sys
import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#  Do 10 requests, waiting each time for a response

requests = [
    b"1;74;0",
    b"2;15;45",
    b"2;42;15",
    b"2;65;30",
    b"3;8;90",
    b"3;6;60",
    b"1;68;0",
    b"2;24;54",
]

for request in requests:
    print("Sending request %s …" % request)
    socket.send(request)

    #  Get the reply.
    message = socket.recv()
    print("Received reply %s [ %s ]" % (request, message))

sys.exit()
