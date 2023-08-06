from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
  return "Bot Online"

def run(host='0.0.0.0', port=8080):
  app.run(host=host, port=port)

def aliver(host='0.0.0.0', port=8080):
  server = Thread(target=run(host=host, port=port))
  server.start()

if __name__ == "__main__":
    main()