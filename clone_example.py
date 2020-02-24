#========
# this script will clone a given example and make changes to extension=1 with required number of events
# uses: python clone_example.py original-req number-of-required-events 
# e.g. python clone_example.py HIG-RunIIFall17wmLHEGS-00545 200000
#========          

import sys
sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/')

#---gkole start
#import argparse
#parser = argparse.ArgumentParser()
#parser.add_argument('--foo', help='foo help')
#args = parser.parse_args()
#----gkole end
print "Number of arguments: ", len(sys.argv)
print "The arguments are: " , str(sys.argv)
from rest import *

mcm = restful(dev=False) #it was True
given_req = sys.argv[1]
# script clones a request to other campaign.
# define list modifications, if member_of_campaign is different
# it will clone to other campaign


modif = {'extension' : 1, 'total_events' : sys.argv[2]}
#__req_prepid = "HIG-RunIIFall17wmLHEGS-01355"
__req_prepid = given_req

# get a request object which we want to clone
a_request = mcm.getA('requests', __req_prepid)

# make predefined modifications
for el in modif:
    a_request[el] = modif[el]

answer = mcm.clone(a_request['prepid'], a_request)
print("new_prepid: %s" % (answer["prepid"]))

single_req = mcm.getA('requests', answer["prepid"], method='get')                                                                                                                                  
print(json.dumps(single_req["history"][0], indent=4))
