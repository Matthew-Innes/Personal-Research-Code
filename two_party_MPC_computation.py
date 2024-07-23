import crypten
import threading

def multi_party_computation(rank, world_size, value): 
    crypten.init()
    encrypted_value = crypten.cryptensor(value)
    result = encrypted_value.get_plain_text()
    print(f"Party {rank} result: {result.item()}")

def run_simulation_threaded(value_1, value_2): 
    world_size = 2 
    needed_threads = [
        threading.Thread(target=multi_party_computation, args=(0, world_size, value_1)),
        threading.Thread(target=multi_party_computation, args=(1, world_size, value_2))
    ]

    for singular_thread in needed_threads: 
        singular_thread.start()
    for singular_thread in needed_threads:
        singular_thread.join()


if __name__ == "__main__": 
    value_1 = 5
    value_2 = 10 
    run_simulation_threaded(value_1, value_2)
