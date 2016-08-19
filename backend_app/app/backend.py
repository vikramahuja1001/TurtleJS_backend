
from dulwich import porcelain as p
from dulwich.repo import Repo as DulwichRepo
from dulwich import repo
import os

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
		self.cloned_from = "ssh://git@github.com/vikramahuja1001/TurtleCodes"
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
			print type(i)
			print type(i.commit)
			a.append('\n')
		return a

	def get_commit_id_and_message(self, f):
		print self.repo_path
		r = self.repo
		w = r.get_walker(paths=[f], max_entries=None)
		count = 0
		a = []
		for i in iter(w):
			count += 1
			lin = ''
			lin = i.commit.id + '_' + i.commit.message 
			a.append(lin)

			print type(i)
			print type(i.commit)
			a.append('\n')
		return a


	def clone_local(self,clone_repo_name):
		#Creating a clone of a given repo. The repo should be local.
		p.clone(self.repo_path,clone_repo_name)


	def clone_remote(self, clone_repo_name):
		#Creating a clone of remote repo.
		self.isaclone = 1
		#Creating a clone of remote repo.
		p.clone(self.cloned_from, clone_repo_name)


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
			#print i.commit.tree
			a.append(i.commit.tree)
		#print len(tree_list)
		for i in range(len(tree_list) - 1):
			#print "Diff between commits"
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


	def push(self):
		try:
			refs_path = b"refs/heads/master"
			new_id = self.repo[b'HEAD'].id
			#self.assertNotEqual(new_id, ZERO_SHA)
			self.repo.refs[refs_path] = new_id
			p.push( self.repo.path,self.cloned_from, b"HEAD:" + refs_path)
		except Exception as e:
			print e
			print "Error"