import time

input("Press Enter to start...")
start_time = time.time()

input("Press Enter to stop...")
elapsed_time = time.time() - start_time

print(f"Elapsed time: {elapsed_time:.2f} seconds")