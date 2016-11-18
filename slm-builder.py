import os
import subprocess
slm_loc="C:\\svn_repo\\Build\\GrammarBuilds\\SLMBuilds"
cmu_loc="C:\\svn_repo\\Build\\GrammarBuilds\\SLMBuilds\\ToolKits\\CMU-Cam_Toolkit_v2\\bin"
tmp_loc="C:\\PycharmProjects\\sandbox\\test"
nua_loc="C:\\Program Files\\Nuance\\Recognizer\\bin"
target="Artists"
cult="en-us"
# subprocess.call(["ls","{}".format(tmp_loc) ])



music_loc="{}\\Music".format(slm_loc)
# echo "### Copying source file"
# subprocess.call(["cp", "-vf", "{}\\{}.txt".format(music_loc, target),
#                  "{}\\{}.txt".format(tmp_loc, target)])
#
# print "### Normalizing the data"
# # ### Normalize the data
# # # Song titles
# f = open("{}\\tmpx.txt".format(tmp_loc), "w")
# subprocess.call(["perl", "{}\\some_scripts_needed\\uc.pl".format(slm_loc), "{}\\{}.txt".format(tmp_loc, target)], shell=True, stdout=f)
# f.close()
#
# subprocess.call([ "perl", "{}\\some_scripts_needed\\conv_num.pl".format(slm_loc), "-i",
#                   "{}\\tmpx.txt".format(tmp_loc), "-o", "{}\\{}_uc.txt".format(tmp_loc,target)])
#
# print "### Getting the vocab"
# ### Get the vocab
# # Song titles
# os = ""
# r = open("{}\\{}_uc.txt".format(tmp_loc, target), "r")
# os = str(r.read())
# f = open("{}\\{}.wfreq".format(tmp_loc, target), "w")
# subprocess.call(["{}\\text2wfreq".format(cmu_loc)], shell=True, stdin=open("{}\\{}_uc.txt".format(tmp_loc, target), "r"), stdout=f)
# f.close()
# os = ""
#
# subprocess.call(["gawk", "{print $2,$1}"], shell=True,stdin=open("{}\\{}.wfreq".format(tmp_loc, target), "r"), stdout=open("{}\\tmp_gawk.txt".format(tmp_loc, target), "w"))
# f = open("{}\\v0".format(tmp_loc), "w")
# # sort -nr > v0
# subprocess.call(["C:\\cygwin\\bin\\sort", "-nr"], shell=True, stdin=open("{}\\tmp_gawk.txt".format(tmp_loc, target), "r"), stdout=f)
# f.close()
os = ""
subprocess.call(["cat" ,"{}\\{}.wfreq".format(tmp_loc, target)],shell=True, stdout=open("{}\\c1".format(tmp_loc),"w"))
f = open("{}\\v1".format(tmp_loc), "w")
subprocess.call(["{}\\wfreq2vocab".format(cmu_loc), "-gt", "40"],shell=True, stdin=open("{}\\c1".format(tmp_loc),"r"), stdout=f)
f.close()
# ##############################
# # CLEAN UP NOT NEEDED - Assumed data is clean
# #cat "$targetstate".wfreq | CMU-Cam_Toolkit_v2/bin/wfreq2vocab -gt "$N" | grep "^[^(]" > v1
# #grep "[^a-zA-Z 0-9'./#<>"\$")%_-]" v1 > v2
# subprocess.call([ "rm", "-rf", "{}\\v2".format(tmp_loc)])
# subprocess.call(["touch", "{}\\v2".format(tmp_loc)])
# # ##############################
# # #grep "^[ ]*[^#a-zA-Z0-9]\+[ ]*"\$ v1 >> v2
# f = open("{}\\v3".format(tmp_loc), "w")
# subprocess.call(["sort", "{}\\v1".format(tmp_loc)], shell=True, stdout=f)
# f.close()
# os = ""
# subprocess.call(["sort", "{}\\v2".format(tmp_loc)],shell=True, stdout=open("{}\\c1".format(tmp_loc),"w"))
# f = open("{}\\v4".format(tmp_loc), "w")
# subprocess.call(["uniq"], shell=True, stdin=open("{}\\c1".format(tmp_loc),"r"), stdout=f)
# f.close()
# os=""
# os1=""
# subprocess.call(["diff", "{}\\v3".format(tmp_loc),  "{}\\v4".format(tmp_loc)], shell=True, stdout=open("{}\\c1".format(tmp_loc),"w"))
# subprocess.call(["grep", "<"], shell=True, stdin=open("{}\\c1".format(tmp_loc),"r"), stdout=open("{}\\c2".format(tmp_loc),"w"))
# f = open("{}\\{}_vbttest.vocab".format(tmp_loc,target), "w")
# subprocess.call(["cut", "-d ", "-f2-"], shell=True, stdin=open("{}\\c2".format(tmp_loc),"r"), stdout=f)
# f.close()
# os=""
# os1=""
# f = open("{}\\{}.vocab".format(tmp_loc, target), "w")
# subprocess.call(["grep", "\"^[^#(]\"", "{}\\{}_vbttest.vocab".format(tmp_loc, target)], shell=True, stdout=open("{}\\c1".format(tmp_loc),"w"))
# subprocess.call(["grep", "\"^[^<]\""], shell=True, stdin=open("{}\\c1".format(tmp_loc),"r"), stdout=f)
# f.close()
f = open("{}\\{}.vocab".format(tmp_loc,target),"w")
subprocess.call(["uniq","{}\\v1".format(tmp_loc)], shell=True,
                # stdin=open("{}\\v0".format(tmp_loc),"r"),
                stdout=f)
f.close()
# rm -rf v0 v1 v2 v3 v4
#
print "### Checking dictionary coverage"
# ### Check dictionary coverage
# # Song titles
# subprocess.call(["{}\\dicttest".format(nua_loc), "-language", "en-us", "-input", "{}\\{}.vocab".format(tmp_loc,target),
#                  "-output", "{}\\{}.dic".format(tmp_loc,target),  "-user_dict", "{}\\Music\\music_all_lex.xml".format(slm_loc)])
# subprocess.call(["grep","'Error: Dictionary lookup failed'", "{}\\{}.dic".format(tmp_loc,target)],shell=True, stdout=os)
# f = open("{}\\notfound".format(tmp_loc), "w")
# subprocess.call(["cut", "-d'|'", "-f1"], shell=True, stdin=os, stdout=f)
# f.close()
# os = ""
# subprocess.call(["perl", "{}\\some_scripts_needed\\DynamicCleanup.pl".format(slm_loc), "{}\\notfound".format(tmp_loc), "{}\\notfound2".format(tmp_loc)])
# subprocess.call(["{}\\dicttest".format(nua_loc), "-language", "en-us", "-max_pron", "4", "-input", "{}\\notfound2".format(tmp_loc), "-output",
#                  "{}\\notfound.dic".format(tmp_loc)])
# f = open("{}\\al".format(tmp_loc), "w")
# subprocess.call([ "cut", "-d'|'", "-f2-", "{}\\notfound.dic".format(tmp_loc)], shell=True, stdout=f)
# f.close()
# subprocess.call(["paste", "{}\\notfound".format(tmp_loc), "{}\\a1".format(tmp_loc)],shell=True, stdout=open("{}\\c1".format(tmp_loc),"w"))
# f = open("{}\\{}_notfound.dic".format(tmp_loc,target), "w")
# subprocess.call(["sed", "s/","\"\t\"","/\"|\"/g"],shell=True, stdin=open("{}\\c1".format(tmp_loc),"r"), stdout=f)#todo: unsure of this
# f.close()
# os = ""
# f = open("{}\\{}_lex.xml".format(tmp_loc,target), "w")
# subprocess.call(["perl", "{}\\some_scripts_needed\\build_dict_n9.pl", "{}\\{}_notfound.dic".format(tmp_loc,target)],shell=True, stdout=f)
# f.close()

# subprocess.call(["rm", "-rf", "{}\\a1".format(tmp_loc), "{}\\notfound".format(tmp_loc), "{}\\notfound2".format(tmp_loc)])
#
# ### Format vocab
print "### Formatting vocab"
subprocess.call(["echo","-e", "'<s>\n</s>'"], shell=True, stdout=open("{}\\c1".format(tmp_loc),"w"))
f = open("{}\\tmpx.txt".format(tmp_loc), "w")
subprocess.call(["cat", "-", "{}\\{}.vocab".format(tmp_loc,target)], shell=True, stdin=open("{}\\c1".format(tmp_loc),"r"), stdout=f)
f.close()
os = ""
print "### Moving temp to vocab"
subprocess.call(["mv", "{}\\tmpx.txt".format(tmp_loc), "{}\\{}.vocab".format(tmp_loc,target)])
print "### Formatting vocab end"
#
# ### Format training data
print "### Formatting training data"
# echo "<s>"  >  train_lm.ccs
f = open("{}\\train_lm.ccs".format(tmp_loc), "w")
f.write("<s>")
f.close()
print "### Formatting training data 2"
# # Song titles
f = open("{}\\{}_train.txt".format(tmp_loc, target), "w")
subprocess.call(["gawk", "'{print \"<s> \"$0\" </s>\"}'", "{}\\{}_uc.txt".format(tmp_loc,target)],shell=True, stdout=f)
print "### Formatting training data end"
#
print "### Training ARPA"
# ### Train ARPA
# # Song titles
subprocess.call(["cat", "{}\\{}_train.txt".format(tmp_loc, target)], shell=True, stdout=open("{}\\c1".format(tmp_loc),"w"))
f = open("{}\\tmp.bin".format(tmp_loc), "w")
subprocess.call(["{}\\text2idngram".format(cmu_loc),  "-vocab", "{}\\{}.vocab".format(tmp_loc, target), "-n", "5", "-temp", "{}".format(tmp_loc)],
                shell=True, stdin=open("{}\\c1".format(tmp_loc),"r"), stdout=f)
subprocess.call(["{}\\idngram2lm".format(cmu_loc), "-vocab", "{}\\{}.vocab".format(tmp_loc,target), "-idngram",
                 "{}\\tmp.bin".format(tmp_loc), "-arpa", "{}\\{}.arpa".format(tmp_loc,target), "-n", "5", "-vocab_type",
                 "0", "-witten_bell", "-context", "{}\\train_lm.ccs".format(tmp_loc), "-cutoffs 40 40 50 60", "-four_byte_counts"]) #todo: this is the moneymaker
subprocess.call(["rm", "-rf", "{}\\tmp.bin".format(tmp_loc)])
#
print "### Modifying headers"
# ### Modify header
# # Song titles
r = open("{}\\{}.arpa".format(tmp_loc,target), "r")
lines = r.readlines()
f = open("{}\\{}.arpa".format(tmp_loc,target), "w")
# for lines in range(lines[45:]):
f.writelines(lines[45:])
f.close()
r.close()
# l=`cat "$targetstate".arpa | wc -l`
# l=`expr "$l" - 46`
# tail -n "$l" "$targetstate".arpa > tmpx.txt
# mv tmpx.txt "$targetstate".arpa
#
print "### Compiling binary models"
# ### Compile binary model
subprocess.call(["{}\\sgc".format(nua_loc), "-language", "{}".format(cult), "-load_arpa", "{}\\{}.arpa".format(tmp_loc,target),
                 "-fsm_out", "{}\\{}.fsm".format(tmp_loc,target), "-wordlist_out" "{}\\{}.wordlist".format(tmp_loc,target),
                 "-no_gram"])
# todo: swtich the .grxml location
subprocess.call(["{}\\sgc".format(nua_loc), "-language", "{}".format(cult), "-optimize", "12", "{}\\{}_wrapper.grxml".format(slm_loc, target)])
#
subprocess.call(["{}\\sgc".format(nua_loc), "-language","{}".format(cult), "-optimize", "12", "{}\\{}.grxml".format(slm_loc, target)])
#
# echo "### Copying files to dest dir"
# cp -f -v *.arpa "$destdir"
# cp -f -v *.fsm "$destdir"
# cp -f -v *.gram "$destdir"
# cp -f -v *.vocab "$destdir"
# cp -f -v *.wordlist "$destdir"
#
# echo "### End"
