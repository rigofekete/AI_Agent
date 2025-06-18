import os
import subprocess

def run_python_file(working_directory, file_path, args=None):

    abs_work_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    
    if not abs_file_path.startswith(abs_work_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'

    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is no a Python file.'

    try:
        commands = ["python3", abs_file_path]

        if args:
            commands.extend(args)

        result = subprocess.run(
                commands,
                capture_output=True, 
                text=True,
                cwd=abs_work_dir,
                timeout=30
        )

        object = []
        
        if result.stdout:
            object.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            object.append(f"STDERR:\n{result.stderr}")
        
        if result.returncode != 0:
            object.append("Process exited with code:\n{result.returncode}")
        if not result.stdout:
            object.append("No output produced.")

        return "\n".join(object)

    except Exception as e:
        return f"Error: executing Python file: {e}"

                                    
