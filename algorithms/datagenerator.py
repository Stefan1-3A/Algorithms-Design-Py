import random
import time

def generate_data(base_filename, count):
    if not base_filename.endswith('.txt'):
        filename = f"{base_filename}.txt"
    else:
        filename = base_filename

    print(f"Creating file: {filename}")

    try:
        with open(filename, "w") as file:
            random.seed(int(time.time()))
            
            chunk_size = 1000000
            written = 0
            while written < count:
                limit = min(count - written, chunk_size)
                buffer = [random.randint(1, 1000) for _ in range(limit)]
                
                for num in buffer:
                    file.write(f"{num} ")
                
                written += limit

    except IOError as e:
        print(f"ERROR: There has been a problem when trying to open this file! {e}")
        return
    
    print(f"Data generated and stored in {filename}")
