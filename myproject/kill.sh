
django_pid=$(ps -ef | grep [r]unserver | awk '{print $2}' | head -1)
#echo $django_pid
if [[ "$django_pid" = '' ]]; then
	echo "not running"
	exit 0
fi

kill $django_pid
echo "killed $django_pid"
/bin/rm django_pid.txt 2> /dev/null
