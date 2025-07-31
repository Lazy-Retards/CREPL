import subprocess, tempfile, os

def run_code(buffer):
    if not buffer:
        print("Buffer empty!")
        return
    with tempfile.NamedTemporaryFile(delete=False, suffix=".c", mode="w") as tmp:
        tmp.write("\n".join(buffer) + "\n")
        tmp_path = tmp.name

    exe_path = tmp_path[:-2]
    compile_result = subprocess.run(["gcc", tmp_path, "-o", exe_path],
                                    capture_output=True, text=True)
    if compile_result.returncode != 0:
        print("Compile Error:\n", compile_result.stderr)
        os.remove(tmp_path)
        return

    run_result = subprocess.run([exe_path], capture_output=True, text=True)
    print(run_result.stdout, end="")
    os.remove(tmp_path)
    os.remove(exe_path)
