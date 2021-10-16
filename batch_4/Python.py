import os


def overwrite():
    path = str(os.getcwd()) + "\\Python.py"
    with open(path, 'r') as file_handle:
        lines = file_handle.readlines()
    fun_list = ["BROWAR"]
    new_line = '[' + '"BROWAR",' * len(fun_list) + '"BROWAR"]'
    print(fun_list)
    with open(path, "w") as file_handle:
        for i in range(len(lines)):
            if i == 7:
                file_handle.write("    fun_list = " + new_line + "\n")
            else:
                file_handle.write(lines[i])

if __name__ == "__main__":
    overwrite()
