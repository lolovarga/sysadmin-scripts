WORKSPACE2=~/workspace/LITP2
TMP_FILE=~/.build_all

function success() {
  [ -f $TMP_FILE ] && cat $TMP_FILE | egrep "^\[INFO\] Installing (.+) to (.+)\.rpm$" | awk '{ print $NF }'
}

function failure() {
  cat $TMP_FILE && clean_file
  exit 1
}

function clean_file() {
  [ -f $TMP_FILE ] && rm -f $TMP_FILE
}

function ctrl_c() {
  clean_file
  exit $?
}

clean_file
current_dir=`pwd`
for repo in ERIClitpcore ERIClitpatrunner ERIClitpbootmgr ERIClitpnetwork ERIClibvirt ERIClitpcli; do
  cd $WORKSPACE2/$repo
  mvn clean install > $TMP_FILE 2>&1
  [ $? -eq 0 ] && success || failure
done
cd $current_dir


trap ctrl_c SIGINT

