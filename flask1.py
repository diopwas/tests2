from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "bonjour la famille Devops"

@app.route('/tables')
def tables():
	return algo_tabl()
	
def algo_tabl():
    res = []
    for i in range(1,11):
        #print("la table de multiplication de {} \n {} * {} = {}".format(i)
              for j in range(1,11):
                  a = i *j
                  res.append("{} * {} = {}".format(i,j,a))	  
    resultat = ",".join(res)
    return resultat
if __name__ == '__main__':
    app.run(debug=True)
