def prueba_signals(sender,instance,**kwargs):
    print('=========')
    lista = instance.tkt.id
    print('Se agrego el tkt',lista)
    print('========================')


def prueba_signals2(sender,instance,**kwargs):
    print('=========')
    lista = instance.tkt.id
    print('Se elimino el tkt',lista)
    print('========================')