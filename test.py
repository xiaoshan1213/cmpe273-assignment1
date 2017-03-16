 # -*- coding: utf-8 -*-
from flask import Flask, render_template
from github import Github
import base64
import argparse
import re
import yaml, json

app = Flask(__name__)
parser = argparse.ArgumentParser(description = 'config site')
parser.add_argument('site', type = str)
args = parser.parse_args()
p = re.compile(r'\/+')
out = p.split(args.site)
len = len(out)

g = Github("xiaoshan1213", "github901213")
repo = g.get_user().get_repo(out[len-1])

@app.route("/")
def getContents():
    tree = repo.get_git_tree('master')
    out = {}
    for item in tree.tree:
        contents = repo.get_file_contents('/' + item.path)
        content = contents.content
        content = base64.b64decode(content)
        out[item.path] = content
    # out = json.dumps(out)
    return render_template('app.html', contents = out)



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
