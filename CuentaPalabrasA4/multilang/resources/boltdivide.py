import storm

class BoltDivide(storm.BasicBolt):

    def initialize(self, conf, context):
        self._conf = conf
        self._context = context
        storm.logInfo("Iniciando BoltDivide...")

    def process(self, tup):
        # Divide las frases por espacios
        palabras = tup.values[0].split()
        # Emite las palabras
        for palabra in palabras:
            storm.logInfo("Enviando %s" % palabra)
            storm.emit([palabra])

BoltDivide().run()
