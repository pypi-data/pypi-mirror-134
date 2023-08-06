from flask import Flask, request, render_template
import csv
import sys
from copy import deepcopy
import os

sourcepath, _ = os.path.split(__file__)

app = Flask(__name__, template_folder=sourcepath)

if len(sys.argv) > 1:
    filepath,fullflname = os.path.split(sys.argv[1])
    fname,ext = os.path.splitext(fullflname)
    with open(sys.argv[1]) as f:
        t = list(csv.reader(f))

    if len(sys.argv) > 2:
        n = int(sys.argv[2])
    else:
        n = 1
else:
    fname = "test"
    n = 5
    with open(os.path.join(sourcepath,"test.csv")) as f:
        t = list(csv.reader(f))
class data():
    def __init__(self, header, content):
        for i, head in enumerate(header):
            setattr(self, head, content[i])

headers = t[0]
headers_set = set(headers)
fmts = t[1]
funcs = []


for fmt in fmts:
    check = fmt.split()
    if len(check) == 1:
        funcs.append(fmt)
    elif len(check) == 2:
        funcs.append("(lambda x: %s(map(%s, x.split())))"%(check[1], check[0]))

t = t[2:]
realt = deepcopy(t)
classt = []
tasks = {}
for i in range(len(t)):
    for j in range(len(t[i])):
        exec("t[i][j] = %s('%s')"%(funcs[j].strip(), t[i][j]))
    if t[i][0] in tasks.keys():
        print("警告！任务名重复")
    tasks[t[i][0]] = i
    classt.append(data(headers, t[i]))
        
def parse_q_to_p(q):
    p = q.split()
    for i, pi in enumerate(p):
        if pi in headers_set:
            p[i] = "self." + pi
    return " ".join(p)

@app.route('/')
def hello_world():
    return render_template("template.html", fname = fname, search = "难度系数 > 0", lists = realt, header = headers, n = n)

searched = False
@app.route('/search/')
def search():
    global searched
    # arguments
    q = request.args.get('q')
    p = parse_q_to_p(q)
    t = []
    for i, self in enumerate(classt):
        searched = eval("%s"%(p))
        if searched == True:
            t.append(realt[i])
    return render_template("template.html", fname = fname, search = q, lists = t, header = headers, n = n)

searched = False
@app.route('/export/')
def export():
    global searched
    # arguments
    q = request.args.get('q')
    p = parse_q_to_p(q)
    t = ",".join(headers) + "\n" + ",".join(fmts) + "\n"
    for i, self in enumerate(classt):
        searched = eval("%s"%(p))
        if searched == True:
            t += ",".join(realt[i]) + "\n"
    return t

@app.route('/detail/')
def detail():
    # arguments
    q = request.args.get('q')
    t = [realt[tasks[q]]]
    return render_template("detail.html", fname = fname, lists = t, header = headers, n = n)


if __name__ == '__main__':
	#开启debug
    app.debug=True
    #在run（）里加入参数 use_reloader=False，就可以解决 * Restarting with stat
    app.run(port=1996,debug=False, use_reloader=False)

