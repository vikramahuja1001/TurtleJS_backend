
from app import app
from flask import Flask, render_template
from flask import request
import os

from dulwich import porcelain as p
from dulwich.repo import Repo as DulwichRepo
from dulwich import repo 
import time


import subprocess


"""Porcelain is a simple wrapper that provides porcelain-like functions on top of Dulwich.

Currently implemented functions in porcelain: 
 * archive
 * add
 * branch{_create,_delete,_list}
 * clone
 * commit
 * commit-tree
 * daemon
 * diff-tree
 * fetch
 * init
 * ls-remote
 * pull
 * push
 * rm
 * receive-pack
 * reset
 * rev-list
 * tag{_create,_delete,_list}
 * upload-pack
 * update-server-info
 * status
 * symbolic-ref

These functions are meant to behave similarly to the git subcommands.
Differences in behaviour are considered bugs.
"""


class backend():
	def __init__(self):
		self.username = ""
		self.email = ""
		self.activity = ""
		self.repo_path = ""
		self.repo_name = ""
		self.isaclone = 0
		self.cloned_from = ""
		self.current_file_name = ""


	def set_authorinfo(self, username, email):
		self.username = username
		self.email = email


	def local_init(self, repo_name, activity):
		self.activity = activity
		self.repo_name = repo_name
		try:
			self.repo = p.init(repo_name)
			self.current_dir = os.getcwd()
			self.repo_path = self.current_dir + '/' + self.repo_name
			print self.repo_path
			print "Local Repo Created"
		except:
			print "Repo already exist, delete it first"

	def load_repo(self, repo_name):
		self.repo_name = repo_name
		self.repo = DulwichRepo(self.repo_name)
		self.current_dir = os.getcwd()
		self.repo_path = self.current_dir + '/' + self.repo_name


	def create_file(self, name, content):
		try:
			file = open(os.path.join(self.repo_path,name), 'w')
			file.write(content)
			file.close()
		except:
			print 'Unable to create README, does it already exist?'


	def edit_file(self, name, content):
		file = open(os.path.join(self.repo_path,name), 'w')
		file.write(content)
		file.close()


	def add(self, a):
		#a can be list of files or a single file
		print self.repo_name
		print self.repo
		if type(a) == list:
			for i in a:
				p.add(self.repo, i)
		else:
			p.add(self.repo, a)


	def get_status(self):
		if os.path.exists(self.repo_path):
			print self.repo_path
			return p.status(self.repo_path)
		else:
			print "Repo does not exist"


	def commit(self, message):
		p.commit(self.repo, message)


	def get_commit_history(self, f):
		print self.repo_path
		r = self.repo
		w = r.get_walker(paths=[f], max_entries=None)
		count = 0
		a = []
		for i in iter(w):
			count += 1
			a.append(i.commit)
			a.append('\n')
		return a


	def clone_local(self,clone_repo_name):
		#Creating a clone of a given repo. The repo should be local.
		p.clone(self.repo_path,clone_repo_name)


	def clone_remote(remote_repo_name, clone_repo_name):
		#Creating a clone of remote repo.
		p.clone(remote_repo_name, clone_repo_name)


	def commit_logs(self):
		try:
			if os.path.exists(self.repo_path):
				a = p.log(self.repo)
				return a
			else:
				return "Repo does not exist"
		except:
			return "No commits yet"

	def set_current_file_name(self, f):
		self.current_file_name = f


	"""
	#Some issues - have to be rectified asap

	def revert_to_commit(self):
		print self.repo_path
		r = self.repo
		f = "README"
		w = r.get_walker(paths=[], max_entries=None)
		count = 0
		for i in iter(w):
			count += 1
			print count,
			print type(i)
			print i
			print i.commit.id
			a = i.commit.id
			#a = a[0:8]
			#print i.commit.get_sha_for()
		print a
		p.reset(self.repo, "hard", a)
	"""


	def get_diff(self):
		#p.diff_tree(self.repo,)
		f = self.current_file_name
		tree_list = []
		w = self.repo.get_walker(paths=[f], max_entries=None)
		a = []
		for i in iter(w):
			tree_list.append(i.commit.tree)
			print i.commit.tree
			a.append(i.commit.tree)
		print len(tree_list)
		for i in range(len(tree_list) - 1):
			print "Diff between commits"
			a.append(p.diff_tree(self.repo, tree_list[i], tree_list[i+1]))
			print 
		return a


	def update_local(self):
		if self.isaclone == 1:
			try:
				p.pull(self.repo, self.cloned_from)
			except:
				print "Error"

		else:
			print "Can not update"




b = backend()
	#def push():

	#def pull():

	#def clone():
@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/ginit', methods=['GET', 'POST'])
def ginit():
	print "Initializing the repo"
	#b = backend()
	b.local_init("turtle", "TurtleJS")
	print b.repo_name
	a = "turtle_vikram.tb"
	b.set_current_file_name(a)
	b.create_file(a,"Code will be here")
	b.set_current_file_name(a)

	print "File Created"
	img = "<img src=\"{{ url_for('static', filename='header-icons/delete.svg') }}\"  onclick=\"hide()\"/>"
	a = "<h2>Local  repo " + b.repo_name + " created</h2>"
	return img+a


@app.route('/add', methods=['GET', 'POST'])
def add():
	#b.load_repo("turtle")
	b.add(b.current_file_name)
	img = "<img src=\"{{ url_for('static', filename='header-icons/delete.svg') }}\"  onclick=\"hide()\"/>"
	a = "<h2>File Added: " + b.current_file_name + "</h2>"
	return img + a

@app.route('/status', methods=['GET', 'POST'])
def status():
	#b.load_repo("turtle")
	print b.current_file_name
	img = "<img src=\"{{ url_for('static', filename='header-icons/delete.svg') }}\"  onclick=\"hide()\"/>"
	a = "<h2>" + str(b.get_status()) + "</h2>"
	return img+a


@app.route('/commit', methods=['GET', 'POST'])
def commit():
	#b.load_repo("turtle")
	a = "First Commit"
	b.commit(a)
	img = "<img src=\"{{ url_for('static', filename='header-icons/delete.svg') }}\"  onclick=\"hide()\"/>"
	c = "<h2>Commited with Commit message:" + a + "</h2>"
	return img+c


@app.route('/commithistory', methods=['GET', 'POST'])
def commithistory():
	#b.load_repo("turtle")
	print b.current_file_name
	a = b.get_commit_history(b.current_file_name)
	c = ""
	for i in a:
		c += str(i)
	print c 
	print type(a)
	print len(a)
	img = "<img src=\"{{ url_for('static', filename='header-icons/delete.svg') }}\"  onclick=\"hide()\"/>"
	c = "<h2>" + c + "</h2>"
	
	return img+c


@app.route('/commitlogs', methods=['GET', 'POST'])
def commitlogs():
	#b.load_repo("turtle")
	a = b.commit_logs()
	#print type(a)
	return a



@app.route('/difftree', methods=['GET', 'POST'])
def difftree():
	#b.load_repo("turtle")
	a = b.get_diff()
	print a
	import commands
	cmd = '> temp'
	output = commands.getoutput(cmd)
	print output
	proc=subprocess.Popen('> temp', shell=True, stdout=subprocess.PIPE, )
	output=proc.communicate()[0]
	print output
	#print b.get_diff()
	#print type(a)
	a = "Hello"
	return a


@app.route('/loadrepo', methods=['GET', 'POST'])
def loadrepo():
	b.load_repo("turtle")
	b.set_current_file_name("turtle_vikram.tb")
	print b.current_file_name
	img = "<img src=\"{{ url_for('static', filename='header-icons/delete.svg') }}\"  onclick=\"hide()\"/>"
	a = "<h2>Repo loaded: " + b.repo_name + "</h2>"
	return img+a

@app.route('/save', methods=['GET', 'POST'])
def save():
	a = request.form['data']
	print a
	print type(a)
	a = str(a)
	b.edit_file(b.current_file_name,a)
	print b.current_file_name
	a = "<h2> File Saved: " + b.current_file_name + "</h2>" 
	img = "<img src=\"{{ url_for('static', filename='header-icons/delete.svg') }}\"  onclick=\"hide()\"/>"
	return img+a

