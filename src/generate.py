import os

from github import Github

def init():
    github = Github()
    return github

def init_workspace(name, wiki_url):
    relpath = "./ws/"+name
    os.makedirs(relpath)
    os.chdir(relpath)
    os.popen("git clone "+wiki_url+" 2>../generator.log")
    os.chdir("../..")


github = init()
reponame = "capstone-generator"
user = github.get_user("moevm")
repo = user.get_repo(reponame)
if repo.has_wiki:
    init_workspace("capstone-generator", "https://github.com/moevm/"+reponame+".wiki.git")
else:
    print "Wiki not found"






#
# g = Github()
# user = g.get_user("kajigor")
# repo = user.get_repo("eltech_compilers")
# pulls = repo.get_pulls()
# path = os.path.abspath("")
# path = path+"\\pulls_info"
# i=0
# for pull in pulls:
#     i = i+1
#     newpath = path+'\\'+str(i)
#     os.makedirs(newpath)
#     filePath = newpath+"\\pull_request.txt"
#     newFile = open(filePath,'w')
#
#     newFile.write("User login:\n")
#     newFile.write(pull.user.login+'\n')
#     newFile.write("title:\n")
#     newFile.write(pull.title.encode('utf-8')+'\n')
#     newFile.write("Body:\n")
#     newFile.write(pull.body.encode('utf-8')+'\n')
#     newFile.write("Comments_URL:\n")
#     newFile.write(pull.comments_url+'\n')
#     newFile.write("Commits_URL:\n")
#     newFile.write(pull.commits_url+'\n')
#     newFile.write("Diff_URL:\n")
#     newFile.write(pull.diff_url+'\n')
#     newFile.write("Review_comments_url:\n")
#     newFile.write(pull.review_comments_url+'\n')
#     newFile.close()
#
#     filePath = newpath+"\\pull_comments.txt"
#     newFile = open(filePath,'w')
#     comments = pull.get_issue_comments()
#     for comment in comments:
#         newFile.write("User:\n")
#         newFile.write(comment.user.login+'\n')
#         newFile.write("Body:\n")
#         newFile.write(comment.body.encode('utf-8')+'\n')
#         newFile.write("---------------------------------------\n")
#     newFile.close()
#
#     filePath = newpath+"\\pull_rewies.txt"
#     newFile = open(filePath,'w')
#     reviews = pull.get_reviews()
#     for review in reviews:
#         newFile.write("Body:\n")
#         newFile.write(comment.body.encode('utf-8')+'\n')
#         newFile.write("---------------------------------------\n")
#     newFile.close()
#
#
#
#
#
#
