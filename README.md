# mcm_scripts
Repository holding examples of McM scripts

# get cookies on lxplus

cern-get-sso-cookie -u https://cms-pdmv.cern.ch/mcm/ -o ~/private/prod-cookie.txt —krb

# example to copy 

python clone_example.py 4000

# to get all chain and their prep-ids given a root request 

python get_chains.py <root_request> <br />
e.g <br />
python get_chains.py HIG-RunIIFall17wmLHEGS-00532 <br />