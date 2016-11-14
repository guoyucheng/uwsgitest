#!/bin/bash
export PATH=/usr/local/python/bin:$PATH
function enter_current_dir() {
	THIS="$0"
	THIS=`dirname "$THIS"`
	cd $THIS
	THIS="`pwd`"
	echo "enter : `pwd`" 1>&2
}

OLD_DIR="`pwd`"
enter_current_dir

function get_status() {
	if [ -f 'uwsgi.pid' ]; then
		pid=`cat uwsgi.pid`
		proc=`ps -ef|grep -v grep|grep ' '$pid' ' |wc -l`
		if [ $proc -gt 0 ]; then
			STATUS=running
		else
			STATUS=stoped
		fi
	else
		STATUS=stoped
	fi
	echo uwsgi is $STATUS
}
get_status

function wait_stop() {
	while [ "$STATUS" = "running" ]
	do
		echo 'sleep 2 seconds to wait the stop operation finished...'
		sleep 2
		get_status
	done
}


function get_operation_action() {
	echo "start"
	echo "stop"
	echo "update"
	echo "restart"
}

function update() {
	if [ "$STATUS" = "running" ]; then
		echo c > uwsgi.ff
	else
		do_start
	fi
}

function do_stop() {
	if [ "$STATUS" = "running" ]; then
		uwsgi --stop uwsgi.pid
		wait_stop
	fi
}

function do_start() {
	if [ "$STATUS" = "stoped" ]; then
		uwsgi --ini uwsgi.ini
	fi
}

function do_restart() {
	do_stop
	do_start
}


CMD=$1
shift

if [ "$CMD" = "status" ]; then
	get_status
elif [ "$CMD" = "actions" ]; then
	get_operation_action
elif [ "$CMD" = "update" ]; then
	update
elif [ "$CMD" = "stop" ]; then
	do_stop
elif [ "$CMD" = "start" ]; then
	do_start
elif [ "$CMD" = "restart" ]; then
	do_restart
else
	echo "unknown command"
fi

cd $OLD_DIR
echo "return to `pwd`" 1>&2
