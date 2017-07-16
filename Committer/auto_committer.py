from github import Github
import Password

# First create a Github instance:
g = Github("zarate8", Password.getPassword())

repos = g.get_user().get_repos()

for commit in repos[0].get_commits():
    print (commit.commit.raw_data["committer"]["date"])