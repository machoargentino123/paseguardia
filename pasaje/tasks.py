from time import sleep



def prueba():
    print("#####################")
    print("tarea")
    print("#####################")


def sleep_and_print(secs):
    sleep(secs)
    print("Tarea sleep y print")


def hook_after_sleeping(task):
    print(task.result)