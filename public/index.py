import os
import sys
from http.server import HTTPServer

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from server import iniciar_servidor

if __name__ == "__main__":
    iniciar_servidor()
