# setting up git to use public/private keys
* Set up public/private keys with github, see https://github.com/settings/ssh.
* to verify the fingerprint of a public key, use "ssh-keygen -l"
* Once keys are set up, simply "git clone git@github.com:autoplot/dev.git"

See also https://help.github.com/en/articles/changing-a-remotes-url

# Resetting URL of existing clone
~~~~~
unix> git remote set-url origin git@github.com:autoplot/dev.git
unix> more .git/config
~~~~~
