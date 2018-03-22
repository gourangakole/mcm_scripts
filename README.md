# mcm_scripts
Repository holding examples of McM scripts

# get cookies on lxplus

cern-get-sso-cookie -u https://cms-pdmv.cern.ch/mcm/ -o ~/private/prod-cookie.txt —krb

cern-get-sso-cookie -u https://cms-pdmv-dev.cern.ch/mcm/ -o ~/private/dev-cookie.txt —krb

# example to copy 

python clone_example.py 4000