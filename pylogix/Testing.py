from pylogix import PLC
with PLC() as comm:
    comm.IPAddress = '192.168.150.9'
    ret = comm.Read('MyTag09')
    print(ret.TagName, ret.Value, ret.Status)