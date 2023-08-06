import time

from tqdm import trange


def determine_answer():
    for _ in trange(10, desc='Thinking...', leave=False):
        time.sleep(0.2)
    return 42
