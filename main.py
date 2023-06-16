import threading

from service.collect import Collector

if __name__ == '__main__':
    room_id = 21693526
    collector = Collector(room_id, 1)
    workers = list()
    collector_worker = threading.Thread(target=collector.run())
    collector_worker.start()
    workers.append(collector_worker)
    nlp_worker =
