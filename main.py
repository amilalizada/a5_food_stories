import time
import threading
import multiprocessing
import requests
import random


def download_image():
    img = requests.get('https://picsum.photos/200')
    with open(f'images/image{random.randint(0, 1000)}.jpg', 'wb') as f:
        f.write(img.content)
# def do_something():
   
#     print("before sleep")
#     time.sleep(1)
#     print("after sleep")

if __name__ == "__main__":
    t1 = time.time()

    processes = []
    for _ in range(100):
        process = multiprocessing.Process(target=download_image)
        process.start()
        processes.append(process)
    
    for pr in processes:
        pr.join()
    t2 = time.time()
    print("time taken: ", t2 - t1)



# t1 = time.time()

# download_image()
# t2 = time.time()
# print("time taken: ", t2 - t1)

# threads = []

# for _ in range(100):
#     thread = threading.Thread(target=download_image)
#     thread.start()
#     threads.append(thread)

# for thread in threads:
#     thread.join()











