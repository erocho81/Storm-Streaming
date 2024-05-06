import storm

from collections import Counter

class BoltCuenta(storm.BasicBolt):
 
    def initialize(self, conf, context):
        self._conf = conf
        self._context = context

        self._counter = Counter()
        storm.logInfo("Iniciando BoltCuenta...")

    def process(self, tup):
    
        palabra = tup.values[0]
        #Incrementa contador
        self._counter[palabra] +=1
        count = self._counter[palabra]
        storm.logInfo("Enviando %s:%s" % (palabra, count))
        # Emite la palabra y cuenta
        storm.emit([palabra, count])

BoltCuenta().run()
