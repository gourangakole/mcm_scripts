# mcm_scripts
Repository holding examples of McM scripts

# get cookies on lxplus

cern-get-sso-cookie -u https://cms-pdmv.cern.ch/mcm/ -o ~/private/prod-cookie.txt —krb

# example to make clone
# uses: python clone_example.py original-req number-of-required-events                                                                                       <br /> 
# e.g. python clone_example.py HIG-RunIIFall17wmLHEGS-00545 200000      


# to get all chain and their prep-ids given a root request 

python get_chains.py <root_request> <br />
e.g <br />
python get_chains.py HIG-RunIIFall17wmLHEGS-00532 <br />

# to make ticket
python makeTicket.py -i FirstRequestPrepId-LastRequestPrepId
e.g <br />

