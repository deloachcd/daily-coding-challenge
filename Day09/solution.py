from time import sleep
import threading


def scheduler(f, args, n):
    def worker(f, args, n):
        seconds = n / 1000
        sleep(seconds)
        f(*args)

    t = threading.Thread(target=worker, args=(f, args, n))
    t.start()
    return t


if __name__ == "__main__":
    jobs = []
    jobs.append(scheduler(print, ('''
  ____   ___    _    ____    ____   ___  _     _        _      ____    _    _
 |  _ \ / _ \  / \  |  _ \  |  _ \ / _ \| |   | |      / \    |  _ \  / \  | |
 | |_) | | | |/ _ \ | | | | | |_) | | | | |   | |     / _ \   | | | |/ _ \ | |
 |  _ <| |_| / ___ \| |_| | |  _ <| |_| | |___| |___ / ___ \  | |_| / ___ \|_|
 |_| \_\\\___/_/   \_\____/  |_| \_\\\___/|_____|_____/_/   \_\ |____/_/   \_(_)

    ''',), 9000))
    jobs.append(scheduler(print, ("One second has passed.",), 1000))
    jobs.append(scheduler(print, ("Two seconds have passed.",), 2000))
    jobs.append(scheduler(print, ("Three seconds have passed.",), 3000))
    jobs.append(scheduler(print, ("Four seconds have passed.",), 4000))
    jobs.append(scheduler(print, ("Five seconds have passed.",), 5000))
    jobs.append(scheduler(print, ("Six seconds have passed.",), 6000))
    jobs.append(scheduler(print, ("Seven seconds have passed.",), 7000))
    jobs.append(scheduler(print, ("Eight seconds have passed.",), 8000))
    for job in jobs:
        job.join()
