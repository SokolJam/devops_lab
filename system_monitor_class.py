from datetime import datetime
import json
import settings
import sys
import time


import psutil


class Monitoring(object):
    def __init__(self, ):
        self.dict_choose = {'txt': self.write_file, 'json': self.write_json}
        self.c_time = datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
        self.file = settings.FILE_DIR + '/' + self.c_time + '-output.' \
            + settings.OUTPUT
        self.data = []
        self.cpu = 0
        self.swap_mem = 0
        self.v_mem = 0
        self.io_read = 0
        self.io_write = 0
        self.net_sent = 0
        self.net_receive = 0

    def write_json(self, counter):
        self.data.append({'SNAPSHOT': counter, 'TIMESTAMP': self.c_time,
                          'Overall CPU load (%)': self.cpu,
                          'Free SWAP memory (M)': self.swap_mem,
                          'Used virtual memory (%)': self.v_mem,
                          'IO information': {'read': self.io_read,
                                             'write': self.io_write},
                          'Network info': {'packet_sent': self.net_sent,
                                           'packet_receive': self.net_receive}
                          })

        with open(self.file, 'w') as js:
            json.dump(self.data, js)

    def write_file(self, counter):
        text = '\nSNAPSHOT {i}: TIMESTAMP {time}: ' \
               'Overall CPU load = {cp} % : ' \
               'Free SWAP memory = {swap} M: ' \
               'Used virtual memory = {virtual} % : ' \
               'IO read = {r_io} : IO write = {w_io} : ' \
               'Network sent = {net1} ' \
               'receive = {net2}'.format(i=counter, cp=self.cpu,
                                         time=self.c_time,
                                         swap=self.swap_mem,
                                         virtual=self.v_mem,
                                         r_io=self.io_read,
                                         w_io=self.io_write,
                                         net1=self.net_sent,
                                         net2=self.net_receive)

        with open(self.file, 'a') as file:
            if counter == 1:
                file.write('{t} ---Monitoring is started---'
                           ''.format(t=self.c_time, file=self.file))
            file.write(text)

    def info(self, iteration):
        self.c_time = datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
        self.cpu = psutil.cpu_percent(interval=1)
        self.swap_mem = int(psutil.swap_memory()[2] / (2 ** 20))
        self.v_mem = psutil.virtual_memory()[2]
        self.io_read = psutil.disk_io_counters().read_count
        self.io_write = psutil.disk_io_counters().write_count
        self.net_sent = psutil.net_io_counters().packets_sent
        self.net_receive = psutil.net_io_counters().packets_recv

        self.dict_choose[settings.OUTPUT](iteration)

    def start(self):
        print(self.c_time, '---Monitoring is started!---\nOutput file:',
              self.file)
        index = 1
        while True:
            self.info(index)
            time.sleep(settings.INTERVAL)
            index += 1

    def stop(self):
        print(self.c_time, ' ---Monitoring is stopped!---\nOutput file:',
              self.file)
        sys.exit()


if __name__ == '__main__':
    monitoring = Monitoring()
    try:
        monitoring.start()
    except KeyboardInterrupt:
        monitoring.stop()
