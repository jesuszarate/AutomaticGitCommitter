from github import Github
import github_login as gl
import Password

repo_name = 'zarate8/AutomaticGitCommitter'

def get_repo_commit_dates(git_inst, repo_name):
    """
    Get commits of certain repo name
    dates of each commit
    :param repo_name:
    :return: dates of the commits of the specified repo name
    """
    dates = []
    for commit in git_inst.get_repo(repo_name).get_commits():
        dates.append(commit.commit.raw_data["committer"]["date"])

    return dates


def get_dates_of_commits(git_inst):
    """
    Get the commits of the first repo

    :return: dates of the commits
    """

    dates = []
    repos = git_inst.get_user().get_repos()
    for i in range(0, len(repos)):
        for commit in repos[i].get_commits():
            dates.append(commit.commit.raw_data["committer"]["date"])
    return dates


def main():
    git_inst = gl.get_github_instance()

    print "Getting Dates..."
    for date in get_repo_commit_dates(git_inst, repo_name):
        print date

if __name__ == '__main__':
    main()