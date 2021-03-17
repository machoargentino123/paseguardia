from time import sleep



def prueba():
    print("#####################")
    print("tarea")
    print("#####################")


def sleep_and_print(secs):
    print("#####################")
     sleep(secs)
     print("Tarea sleep y print")
     print("#####################")


def after_sleeping(task):
    print(task.result)