p = subprocess.Popen("svn info svn://xx.xx.xx.xx/project/trunk | grep \"Revision\" | awk '{print $2}'", stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
print "Revision is", output
