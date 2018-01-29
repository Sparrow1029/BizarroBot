# To use this script to activate virtualenv, you must source it:
# . setenv.sh
# Feel free to export shell environment variables, etc. via this script as well.
echo "Setting virtualenv..."
CWD=$(pwd)
source $CWD/venv/bin/activate
echo "Done."
