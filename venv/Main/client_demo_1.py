import socket
import alarm_pb2
import message_pb2


def pack_data(length,byteorder) -> bytes:
    alarm = alarm_pb2.Alarm()
    alarm.community = '保利花园'
    alarm.building_id = 19
    alarm.building_part = 'A'
    alarm.cell_id = 2
    alarm.room_id = 206
    alarm.alarm_category = '火警'
    alarm.attachment = '其它'

    message_head = message_pb2.MessageBase.Header()
    message_head.type = message_pb2.MessageBase.SERVICE_REQ

    message_body = message_pb2.MessageBase.Body()
    message_body.context.MergeFrom(alarm)

    message = message_pb2.MessageBase()
    message.header.MergeFrom(message_head)
    message.body.MergeFrom(message_body)

    # print readable message
    print(message)

    # create a new request message
    message_str = message.SerializeToString()
    length_bytes = len(message_str).to_bytes(length=length,byteorder=byteorder)

    # send bytes to server
    data = length_bytes + message_str

    # for debug
    print('消息序列化后：')
    print (message_str)
    print('封装消息长度后：')
    print(data)

    return data

def unpack(recv_data,length=4) -> message_pb2.MessageBase:
    bytes_data = recv_data[length:]
    message = message_pb2.MessageBase()
    message.ParseFromString(bytes_data)
    return message


if __name__ == '__main__':

    # create a Tcp/ip socket object
    # socket_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #
    # remote_address = ('192.168.0.100',5000)
    #
    # socket_client.connect_ex(remote_address)
    #
    # # emit the message
    # socket_client.send(pack_data(4,'big'))
    #
    # recv_data = socket_client.recv(1024)
    #
    # message = unpack(recv_data,length=4)
    # print('接收返回的' + message.body.context.building_part)


    # socket_client.close()

    send_data = pack_data(4,'big')
    #
    # print(len(send_data))

    abytes = b'\n\x02\x12*'
    bbytes = b'"('

    print(len(abytes))
    print(abytes[3])
    print(bbytes[0])












































#message.Clear()
#print(message.IsInitialized())
#print(message.__str__())



#print(type(message.header.type))
#print(message.body.context.room_id)