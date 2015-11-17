import logging
from collections import defaultdict
__author__ = 'jhh283'

logging.basicConfig(filename='loader.log', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class ECG(object):
    def __init__(self):
        self.time = []
        self.signal = []


def load_timed(filename, signal, freq):
    time_step = 1/freq
    with open(filename,  'rb') as f:
        time = 0
        for row in f:
            row = float(row.strip())
            if row:
                time = time
                event_value = row
                signal.time.append(time)
                signal.signal.append(event_value)
            time += time_step
    logging.info("loading: "+filename+'\t')


def load_ECG(filename, freq):
    signal = ECG()
    load_timed(filename, signal, freq)
    return signal

if __name__ == '__main__':
    file = 'data/Data.txt'
    freq_hertz = 100.0
    # want time steps that are milliseconds
    frequency_kHz = freq_hertz / 1000
    signal = load_ECG(file, frequency_kHz)
    print signal.time[1], signal.signal[1]
