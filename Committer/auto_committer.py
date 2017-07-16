from github import Github
import Password

#file = "Committer/password.txt"

# First create a Github instance:
g = Github("zarate8", Password.getPassword())

repos = g.get_user().get_repos()
#commit = repos[0].get_commits()[0]

for commit in repos[0].get_commits():
    print (commit.commit.raw_data["committer"]["date"])

'''
# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print (repo.commits)
'''