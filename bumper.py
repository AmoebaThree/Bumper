if __name__ == '__main__':
    import systemd.daemon
    import redis
    import time

    left_input = '6'
    right_input = '7'
    left_channel = 'pfd.input.' + left_input
    right_channel = 'pfd.input.' + right_input
    request_channel = 'bumper'

    print('Startup')
    r = redis.Redis(host='192.168.0.1', port=6379, db=0)
    p = r.pubsub(ignore_subscribe_messages=True)
    p.subscribe(request_channel, left_channel, right_channel)
    print('Startup complete')
    systemd.daemon.notify('READY=1')

    try:
        for message in p.listen():
            if message.channel == request_channel:
                r.publish('pfd.inputs', left_input)
                r.publish('pfd.inputs', right_input)
            elif message.channel == left_channel:
                if message.message == "input." + left_input + ".on":
                    r.publish('bumper.left', 'left.on')
                elif message.message == "input." + left_input + ".off":
                    r.publish('bumper.left', 'left.off')
            elif message.channel == right_channel:
                if message.message == "input." + right_input + ".on":
                    r.publish('bumper.right', 'right.on')
                elif message.message == "input." + right_input + ".off":
                    r.publish('bumper.right', 'right.off')
    except:
        print("Goodbye")
