from service.collect import Collector

if __name__ == '__main__':
    room_id = 21693526
    collector = Collector(room_id, 1)
    collector.run()
