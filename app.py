from flask import *

app=Flask(__name__)

@app.route("/")
@app.route("/<filename>")
@app.route("/<filename>/<st>/<en>")
@app.route("/<filename>/<st>")
def home(filename="file1",st=0,en=-1):
	try:
		startLine = int(st)
		endline = int(en)
		leni= 0
		if filename == "file4.txt":
			if endline == -1:
				endline=74
			with open(filename,"r", encoding="utf8", errors='ignore') as myfile:
				d = [next(myfile) for x in range(endline)]
			return render_template('index.html', data=d[startLine:endline+1])
		else:
			with open(filename + ".txt", "r", encoding="cp437") as f1:
				d = f1.readlines()
			if endline == -1:
				endline = len(d)
			return render_template("index.html", data=d[startLine:endline + 1])
	except (FileNotFoundError):
		return "File Not Found "



# last lines
if __name__ =="__main__":
	app.run(debug=True)


