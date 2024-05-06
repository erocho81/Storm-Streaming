import storm
import random
# Aquí se indican algunas frases
FRASES = """
Aspernatur explicabo voluptatem incidunt. Mollitia vero et tempore ut omnis deleniti qui reiciendis. Deleniti quo vel dicta animi consequatur. Quis voluptas sed voluptates. Eum eum minus dignissimos hic.

Maxime omnis architecto ipsum pariatur natus provident. Rerum nihil cumque accusantium omnis. Ea dolorem fuga aut. Voluptas iure laborum ipsa quod quis. Rerum aliquid natus quae molestiae nesciunt delectus non aspernatur.

Sit excepturi magnam neque dignissimos dolor deserunt. Itaque et aut necessitatibus. Quam facere ratione sunt vero. Quas saepe impedit iusto.

Qui quia vero blanditiis porro animi nemo omnis porro. Molestiae nulla nisi consequatur voluptatibus. Laudantium minus explicabo unde fugit.

Perspiciatis qui temporibus natus deleniti animi in ea sint. Non debitis eum repellat voluptatem voluptas rerum rerum. Atque animi aut sit. Sit sint aut eum officia debitis. Aut deserunt delectus reiciendis quo delectus sint non
""".strip().split('\n')

class SpoutFrase(storm.Spout):
	def initialize(self, conf, context):
		self._conf = conf
		self._context = context

		storm.logInfo("Iniciando SpoutFrase...")

	def nextTuple(self):
        # Envia frases de forma aleatoria
		frase = random.choice(FRASES)
		storm.logInfo("Enviando %s" % frase)
		storm.emit([frase])


SpoutFrase().run()
