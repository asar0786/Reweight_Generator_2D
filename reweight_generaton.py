import os
import sys

aQGC_Pars = {
#    "FS0":[1,  [-0.4, -0.2, 0.0, 0.2, 0.4]],
    "FS0":[1,  [-50, -45, -40, -35, -30, -20, -10, -8, -6, -5, -4, -3.0, -2.5, -2.0, -1.5, -1.2, -1.0, -0.8, -0.6, -0.4, -0.2, 0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.5, 2.0, 2.5, 3.0, 4, 5, 6, 8, 10, 20, 30, 35, 40, 45, 50]],
#    "FS1":[2,  [-1.0, -0.5, 0.0, 0.5, 1.0]],
    "FS1":[2,  [-35, -33, -30, -25, -20, -15, -10, -7.5, -5.0, -4.0, -3.0, -2.5, -2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 7.5, 10, 15, 20, 25, 30, 33, 35]],

#    "FM0":[3,  [-0.2, -0.1, 0, 0.1, 0.2]],    
    "FM0":[3,  [-10, -9, -8, -7, -6, -5, -4, -3, -2.0, -1.5, -1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.5, 2.0, 3, 4, 5, 6, 7, 8, 9, 10]],
#    "FM1":[4,  [-0.6, -0.3, 0, 0.3, 0.6]],
    "FM1":[4,  [-30, -28, -23, -21, -18, -15, -13, -10, -5.0, -3.0, -2.5, -2.1, -1.8, -1.5, -1.2, -0.9, -0.6, -0.3, 0, 0.3, 0.6, 0.9, 1.2, 1.5, 1.8, 2.1, 2.5, 3.0, 5.0, 10, 13, 15, 18, 21, 23.0, 28, 30]],
#    "FM2":[5,  [0, 1, 2, 3, 6, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]],    # not included in 2016
#    "FM3":[6,  [0, 1, 2, 3, 5, 8, 13, 21, 31, 44, 55, 65, 75, 85, 95, 105]],    # not included in 2016
#    "FM4":[7,  [0, 1, 2, 3, 5, 8, 13, 21, 31, 44, 55, 65, 75, 85, 95, 105, 115, 121, 130]],    # not included in 2016
#    "FM5":[8,  [0, 1, 2, 3, 5, 8, 13, 21, 31, 44, 55, 65, 75, 85, 95, 105, 115, 121, 130, 150, 170, 190, 200]],    # not included in 2016
    "FM6":[9,  [-20, -18, -15, -12, -10, -7, -5, -3, -2.0, -1.8, -1.6, -1.4, -1.2, -1.0, -0.5, -0.2, 0, 0.2, 0.5, 0.7, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 3, 5, 7, 10, 12, 15, 18, 20]],
#    "FM6":[9,  [0, 0.2, 0.5]],
    "FM7":[10, [-40, -35, -30, -25, -20, -15, -10, -5.0, -3.5, -3.0, -2.5, -2.0, -1.5, -1.0, -0.5, 0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 5.0, 10, 15, 20, 25, 30, 35, 40]],
#    "FM7":[10, [0, 0.5, 1.0]],
#    
    "FT0":[11, [-2.0, -1.8, -1.4, -1.2, -1.0, -0.7, -0.5, -0.3, -0.2, -0.18, -0.14, -0.12, -0.10, -0.08, -0.06, -0.04, -0.02, 0, 0.02, 0.04, 0.06, 0.08, 0.10, 0.12, 0.14, 0.18, 0.20, 0.30, 0.50, 0.7, 1.0, 1.2, 1.4, 1.8, 2.0]],
#    "FT0":[11, [0, 0.02, 0.04]],
    "FT1":[12, [-2.0, -1.8, -1.4, -1.2, -1.0, -0.7, -0.5, -0.3, -0.2, -0.18, -0.14, -0.12, -0.10, -0.08, -0.06, -0.04, -0.02, 0, 0.02, 0.04, 0.06, 0.08, 0.10, 0.12, 0.14, 0.18, 0.20, 0.30, 0.50, 0.7, 1.0, 1.2, 1.4, 1.8, 2.0]],
#    "FT1":[12, [0, 0.02, 0.04]],
    "FT2":[13, [-4.5, -3.9, -3.4, -2.9, -2.5, -1.7, -1.2, -0.9, -0.7, -0.5, -0.32, -0.26, -0.20, -0.14, -0.08, -0.04, -0.02, 0, 0.02, 0.04, 0.08, 0.14, 0.20, 0.26, 0.32, 0.5, 0.7, 0.9, 1.2, 1.7, 2.5, 2.9, 3.4, 3.9, 4.5]],
#    "FT2":[13, [0, 0.02, 0.04]]
#    "FT5":[16, [0, 0.2, 0.5, 0.7, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 3, 5, 7, 10, 12, 15, 18, 20, 22, 25]],    # not included in 2016
#    "FT6":[17, [0, 0.2, 0.5, 0.7, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 3, 5, 7, 10, 12, 15, 18, 20, 22, 25, 27, 29]],    # not included in 2016
#    "FT7":[18, [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.5, 2.0, 2.5, 3.0, 4, 5, 6, 8, 10, 20, 30, 35, 40, 45, 50, 55, 60, 65, 70]],    # not included in 2016
#    "FT8":[19, [0, 0.02, 0.04, 0.06, 0.08, 0.10, 0.12, 0.14, 0.18, 0.20, 0.30, 0.50, 0.7, 1.0, 1.2, 1.4, 1.8, 2.2, 2.6, 3.0, 3.5, 4.0]],    # not included in 2016
#    "FT9":[20, [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.5, 2.0, 3, 4, 5, 6, 7, 8, 9, 10]]    # not included in 2016
}
twod_par_to_scan = [
		    ["FS0", "FS1"],
		    ["FM0" ,"FM1"],
		    ["FM6","FM7"],
		    ["FT0","FT1"],
		    ["FT1","FT2"],
		   ]
print "Start printing the reweight card..."

OutPutFile = open("reweight_card_2018.dat","w")

OutPutFile.write("change helicity False\n")
print("change helicity False")
OutPutFile.write("change rwgt_dir rwgt\n")
print("change rwgt_dir rwgt\n")

for i in twod_par_to_scan:
#    print(i)
    for key, item in aQGC_Pars.items():
	if i[0]==key:
	    OutPutFile.write("\n\n#"+"*"*11+" "*3+key+" "*3+"*"*11+"\n")
	    print("\n#"+"*"*11+" "*3+key+" "*3+"*"*11+"\n")
#	    print(key,item)
	    for parameters1 in item[1]:
#	        if parameters1 ==0: continue
#		print(item[1])
#		print(parameters1)
		for key2, item2 in aQGC_Pars.items():
		    if key2==key: continue
#		    print("Key2= ",key2,item2)
		    for parameters2 in item2[1]:
			if (key==i[0] and key2==i[1]):
			    if item[0] != 11 and item2[0] != 11:
				if int(parameters1) != 0 and int(parameters2) != 0:
				    print("\nlaunch --rwgt_name="+key+str(parameters1).replace(".","p").replace("-","m")+"_"+key2+str(parameters2).replace(".","p").replace("-","m"))
#            	    					OutPutFile.write("\nlaunch --rwgt_name="+key+"_m"+str(parameters1).replace(".","p")+"_"+key2+"_m"+str(parameters2).replace(".","p"))
#            	    		    print("\nlaunch --rwgt_name="+key2+"_m"+str(parameters2).replace(".","p"))
                		    print("\n\tset anoinputs 11 0.000000e+00")
                		    print("\n\tset anoinputs "+str(item[0])+" -"+str(parameters1)+"e-12\n")
                		    print("\n\tset anoinputs "+str(item2[0])+" -"+str(parameters2)+"e-12\n")
				print("\nlaunch --rwgt_name="+key+"_"+str(parameters1).replace(".","p").replace("-","m")+"_"+key2+"_"+str(parameters2).replace(".","p").replace("-","m"))
				OutPutFile.write("\nlaunch --rwgt_name="+key+"_"+str(parameters1).replace(".","p").replace("-","m")+"_"+key2+"_"+str(parameters2).replace(".","p").replace("-","m"))
				print("\tset anoinputs 11 0.000000e+00")
				OutPutFile.write("\n\tset anoinputs 11 0.000000e+00")
				print("\n\tset anoinputs "+str(item[0])+" "+str(parameters1)+"e-12")
				OutPutFile.write("\n\tset anoinputs "+str(item[0])+" "+str(parameters1)+"e-12")
				print("\tset anoinputs "+str(item2[0])+" "+str(parameters2)+"e-12\n")
				OutPutFile.write("\n\tset anoinputs "+str(item2[0])+" "+str(parameters2)+"e-12\n")
			    else:  
				print("\nlaunch --rwgt_name="+key+"_"+str(parameters1).replace(".","p").replace("-","m")+"_"+key2+"_"+str(parameters2).replace(".","p").replace("-","m"))
				OutPutFile.write("\nlaunch --rwgt_name="+key+"_"+str(parameters1).replace(".","p").replace("-","m")+"_"+key2+"_"+str(parameters2).replace(".","p").replace("-","m"))
				print("\n\tset anoinputs "+str(item[0])+" "+str(parameters1)+"e-12")
				OutPutFile.write("\n\tset anoinputs "+str(item[0])+" "+str(parameters1)+"e-12")
				print("\n\tset anoinputs "+str(item2[0])+" "+str(parameters2)+"e-12")
				print("\n\tset anoinputs "+str(item2[0])+" "+str(parameters2)+"e-12")
				OutPutFile.write("\n\tset anoinputs "+str(item2[0])+" "+str(parameters2)+"e-12")
