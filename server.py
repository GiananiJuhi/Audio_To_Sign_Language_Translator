from nltk.parse.corenlp import CoreNLPServer
import os

java_path = "Your java bin path"
os.environ['JAVAHOME'] = java_path

STANFORD = os.path.join("models", "stanford-corenlp-full-2018-10-05")

server = CoreNLPServer(
   os.path.join(STANFORD, "stanford-corenlp-3.9.2.jar"),
   os.path.join(STANFORD, "stanford-corenlp-3.9.2-models.jar"),
)

server.start()