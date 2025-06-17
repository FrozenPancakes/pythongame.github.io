import subprocess 
 
python_output = subprocess.check_output(['python', 'main.py']) 
html = f"<pre>{python_output.decode().strip()}</pre>" 