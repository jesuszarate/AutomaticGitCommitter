from github import Github
import Password

# First create a Github instance:
g = Github("zarate8", Password.getPassword())

# Test to see if I can get token


repo_name = 'bkimmig/data-mining-project'
repo_name = 'zarate8/AutomaticGitCommitter'


def getDatesOfCommitsOfRepo(repo_name):
    """
    Get commits of certain repo name
    dates of each commit
    :param repo_name:
    :return: dates of the commits of the specified repo name
    """
    dates = []
    for commit in g.get_repo(repo_name).get_commits():
        dates.append(commit.commit.raw_data["committer"]["date"])

    return dates


def getDatesOfCommits():
    """
    Get the commits of the first repo

    :return: dates of the commits
    """

    dates = []
    repos = g.get_user().get_repos()
    for i in range(0, len(repos)):
        for commit in repos[i].get_commits():
            dates.append(commit.commit.raw_data["committer"]["date"])
    return dates

for date in getDatesOfCommitsOfRepo(repo_name):
    print date