canSendPy
====================

CAN-bus simulation command line tool
--------------------

Python3.5+ cmd tool for Linux to simulate specific can-bus behaviori.
Project is setup to work on Raspberry Pi but it's possible to run it on any Linux PC with SocketCAN interface 

Requirement
- Working Socket can interface on Linux
- HW to communicate on can-bus (or virtual can interface)
- python-can module (sudo python3.5 -m pip3 install python-can)


*Functionality*

Note: This is old functionality and will be revisited soon

- Read one can message (timeout)
- Read multiple can messages (timeout)
- Send one can message
- Send one message multiple times
- Send messages from text file
- Wait for Address Claim request - no collision
- Wait for Address Claim request - multiple collision
- Wait for new device Address Claim - multiple collision
- Wait for VIN code request - VIN code single frame response
- Wait for VIN code request - VIN code multiple frame response
- Simulate Engine RPM shift from one value to another value

