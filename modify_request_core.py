#========
# this script will update a given request's nThread 
# uses: python clone_example.py original-req number-of-required-events 
# e.g. python clone_example.py HIG-RunIIFall17wmLHEGS-00545 200000
#========          

import sys
sys.path.append('/afs/cern.ch/cms/PPD/PdmV/tools/McM/')
from rest import McM
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('--prepid', type=str, help="check mcm requests using prepids",dest="prepid")
parser.add_argument("--core",type=str, help="number should be 8, 4, 2 or 1",dest="core")

args = parser.parse_args()


print "Number of arguments: ", len(sys.argv)
print "The arguments are: " , str(sys.argv)

mcm = McM(dev=False)

# Example to edit a request parameter(-s) and save it back in McM
# request_prepid_to_update = 'HIG-Summer12-01257' # Doesn't exist
#given_req = sys.argv[1]
request_prepid_to_update = args.prepid # sys.argv[1] #'HIG-RunIIFall18wmLHEGS-03028'
#field_to_update = 'time_event'

field_to_update = 'sequences'
# get a the dictionnary of a request
request = mcm.get('requests', request_prepid_to_update)

if 'prepid' not in request:
    # In case the request doesn't exist, there is nothing to update
    print('Request "%s" doesn\'t exist' % (request_prepid_to_update))
else:
    print('Request\'s "%s" field "%s" BEFORE update: %s' % (request_prepid_to_update,
                                                            field_to_update,
                                                            request[field_to_update]))

    # Modify what we want
    # time_event is a list for each sequence step
    #request[field_to_update] = [4]
    print('check', request["sequences"][0]['nThreads'])
    request[field_to_update][0]['nThreads'] = args.core #sys.argv[2]#'4'
    # Push it back to McM
    update_response = mcm.update('requests', request)
    print('Update response: %s' % (update_response))

    # Fetch the request again, after the update, to check whether value actually changed
    request2 = mcm.get('requests', request_prepid_to_update)
    print('Request\'s "%s" field "%s" AFTER update: %s' % (request_prepid_to_update,
                                                           field_to_update,
                                                           request2[field_to_update]))
