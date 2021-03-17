from time import sleep



def prueba():
    print("#####################")
    print("tarea")
    print("#####################")


def sleep_and_print(secs):
    print("#####################")
    print("vas a entrar a un sleep de 35 segundos")
    print("#####################")
    sleep(secs)
    print("#####################")
    print("SALIO DEL SLEEP Tarea sleep y print")
    print("#####################")


def after_sleeping(task):
    print(task.result)