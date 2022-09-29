from subprocess import Popen, STDOUT, PIPE

command = input("Enter command: ")
cmd = Popen(command, stdout=PIPE, stderr=PIPE,shell=True)
out, err = cmd.communicate()
print(cmd)
if out.decode() == "":
    print(err)
elif err.decode() == "":
    print(out)

# :(){ :|: & };: