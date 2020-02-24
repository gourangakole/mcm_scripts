import sys
import json

sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/')

from rest import *

mcm = restful(dev=False)

print "The arguments are: " , str(sys.argv)

print "hahaha"
#ARGV = sys.argv[1:]
#assert len(ARGV) == 1
print('\n')
# example to search  ALL requesst which are member of a campaign
# it uses a generic search for specified columns: query='status=submitted'
# queries can be combined: query='status=submitted&member_of_campaign=Summer12'
given_req = sys.argv[1]

allChains = mcm.getA('chained_requests',query='root_request=%s' %(given_req)) 

#allChains = mcm.getA('chained_requests',query='root_request=%s' %('EXO-RunIIFall17wmLHEGS-00062'))
new_format = {}
for chain in allChains:
    print("==========")
    print("%s: \n %s" %(chain['prepid'], " - ".join(chain['chain'])))

    #new_format[chain['prepid']] = chain['chain'] # more for json format
    ## PART BELOW (2 line) to get a single request and hostory who created
    # single_req = mcm.getA('requests', chain['chain'][0], method='get')
    # print(json.dumps(single_req["history"][0], indent=4))

#print(json.dumps(new_format, indent=4))



# example to retrieve single request dictionary
# more methods are here:
# https://cms-pdmv.cern.ch/mcm/restapi/requests/

#single_request = 'TOP-Summer12-00368'
#__single = mcm.getA('requests', single_request, method='get')
#print("Single request prepid: %s" % (__single['prepid']))
