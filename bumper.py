import systemd.daemon
import redis
import time


def execute():
    print('Startup')

    left_input = '6'
    right_input = '7'
    left_channel = 'pfd.input.' + left_input
    right_channel = 'pfd.input.' + right_input
    request_channel = 'bumper'

    left_input_on_msg = 'input.' + left_input + '.on'
    left_input_off_msg = 'input.' + left_input + '.off'
    right_input_on_msg = 'input.' + right_input + '.on'
    right_input_off_msg = 'input.' + right_input + '.off'

    r = redis.Redis(host='192.168.0.1', port=6379,
                    db=0, decode_responses=True)
    p = r.pubsub(ignore_subscribe_messages=True)
    p.subscribe(request_channel, left_channel, right_channel)

    r.publish('services', 'bumper.on')
    systemd.daemon.notify('READY=1')
    print('Startup complete')

    try:
        for message in p.listen():
            if message['channel'] == request_channel:
                r.publish('pfd.inputs', left_input)
                r.publish('pfd.inputs', right_input)

            elif message['channel'] == left_channel:
                if message['data'] == left_input_on_msg:
                    r.publish('bumper.left', 'left.on')
                elif message['data'] == left_input_off_msg:
                    r.publish('bumper.left', 'left.off')

            elif message['channel'] == right_channel:
                if message['data'] == right_input_on_msg:
                    r.publish('bumper.right', 'right.on')
                elif message['data'] == right_input_off_msg:
                    r.publish('bumper.right', 'right.off')
    except:
        r.publish('services', 'bumper.off')
        p.close()
        print('Goodbye')


if __name__ == '__main__':
    execute()
