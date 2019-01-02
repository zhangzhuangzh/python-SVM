#!/bin/bash


function isFull()
{

	num=$(ps -ef|grep ./aimint|grep -v grep|cut -c 9-15 |wc -l)
	count=$(ps -ef|grep ./aimext|grep -v grep|cut -c 9-15 |wc -l)
	((total  =  $num + $count))
	time=$(date "+%Y-%m-%d %H:%M:%S")
	echo "${time}"
	echo "当前aimall的进程数量为$total"
	value=1
	#new_processer=56
	new_processer=$(cat /proc/cpuinfo |grep "processor"|wc -l  )
	if [ "$total" -le "$new_processer" ];  then
		value=0
	fi
	return $value	
}

n=0
for i in *.wfn
do
		
		while true
		do
			isFull
			statusFull=$?
			echo "当前状态：$statusFull"
			if [ "$statusFull" == 1 ];  then
				sleep 1m
			else
				break
			fi
		echo -e "true循环************\n\n"
		done
((n=$n+1))
echo "n= $n"
#在此写提交命令
/home/zhang/AIMAll/aimqb.ish -nogui -bim=proaim -boaq=veryhigh -shm_lmax=10 ${i} &
echo -e  "\n\n\n\n\n"
done
