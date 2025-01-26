import os
import subprocess
import time

folder_path = os.path.dirname(os.path.abspath(__file__))
processes = {}

def run_files():
    file_count = 0
    current_script = os.path.basename(__file__)

    for filename in os.listdir(folder_path):
        if file_count >= 2:  
            break
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and filename.endswith(".py") and filename != current_script:
            print(f"porneste scriptu: {filename}")
            try:
                process = subprocess.Popen(['python', file_path])
                processes[filename] = process
                print(f"script {filename} a fost pornit")
                file_count += 1
            except Exception as e:
                print(f"Eroare {filename}: {e}")

    if processes:
        print(f"scripturi pornite: {', '.join(processes.keys())}")
        clear_terminal_event()
    else:
        print("am uitat sa bag scriptu :)))")

    for filename, process in processes.items():
        process.wait()
        print(f"Fișierul {filename} s-a închis")



if __name__ == "__main__":
    run_files()
    print("pa...........")