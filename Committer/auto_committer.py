from github import Github
import Password

# First create a Github instance:
g = Github("zarate8", Password.getPassword())

repos = g.get_user().get_repos()

repo_name = 'bkimmig/data-mining-project'
repo_name = 'zarate8/AutomaticGitCommitter'

rep = g.get_repo(repo_name)

#coms = rep.get_commits()

# Get commits of certain repo name
for commit in g.get_repo(repo_name).get_commits():
    print (commit.commit.raw_data["committer"]["date"])

'''
Get the commits of the first repo
'''
'''
for commit in repos[0].get_commits():
    print (commit.commit.raw_data["committer"]["date"])
'''
