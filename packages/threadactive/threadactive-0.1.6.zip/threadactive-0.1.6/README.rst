threadactive
============

A simple utility help building multithread application through message queue.

Examples
--------

main.py::

    import time
    import threading
    import threadactive
    
    
    class BackWorker(threadactive.Agent):
        def tick(self):
            threadactive.Agent.tick(self)
            print("[%s][%d] front" % (threading.current_thread().getName(), time.clock()) )
            self.print_in_back()
            time.sleep(1)

        @threadactive.backend
        def print_in_back(self, *args, **kwargs):
            print("[%s][%d] back" % (threading.current_thread().getName(), time.clock()) )
            if time.clock() > 3:
                self.back_to_front()

        @threadactive.frontend
        def back_to_front(self, *args, **kwargs):
            print("[%s][%d] back to front" % (threading.current_thread().getName(), time.clock()) )


    bw = BackWorker()
    while True:
        bw.tick()
    
output::

    [MainThread][0] front
    [Thread-1][0] back
    [MainThread][1] front
    [Thread-1][1] back
    [MainThread][2] front
    [Thread-1][2] back
    [MainThread][3] front
    [Thread-1][3] back
    [MainThread][4] back to front
    [MainThread][4] front
    [Thread-1][4] back
    [MainThread][5] back to front
    [MainThread][5] front
    [Thread-1][5] back
    ...