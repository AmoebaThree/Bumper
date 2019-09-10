if __name__ == '__main__':
    import systemd.daemon, pifacedigitalio, redis, time

    print('Startup')
    pfd = pifacedigitalio.PiFaceDigital()
    listener = pifacedigitalio.InputEventListener(chip=pfd)
    r = redis.Redis(host='192.168.0.1', port=6379, db=0)
    print('Startup complete')
    systemd.daemon.notify('READY=1')

    try:
        def left_on(e):
            r.publish("bumper-left", "left-on")
        def left_off(e):
            r.publish("bumper-left", "left-off")
        def right_on(e):
            r.publish("bumper-right", "right-on")
        def right_off(e):
            r.publish("bumper-right", "right-off")

        listener.register(6, pifacedigitalio.IODIR_FALLING_EDGE, left_on)
        listener.register(6, pifacedigitalio.IODIR_RISING_EDGE, left_off)
        listener.register(7, pifacedigitalio.IODIR_FALLING_EDGE, right_on)
        listener.register(7, pifacedigitalio.IODIR_RISING_EDGE, right_off)
        listener.activate()

        while True:
            time.sleep(1)
    except:
        listener.deactivate()
        pfd.deinit_board()
        print("Goodbye")