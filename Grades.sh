#! /bin/bash
# Paul Lucero

if [[ $# -ne 1 ]]; then
	echo "Usage: $0 filename"
	exit 1
fi

while IFS=' ' read -r idno first last scoreone scoretwo scorethree
do
	avg=$(((scoreone + scoretwo + scorethree) / 3))
	echo "$avg [$idno] $last, $first"
done < <(sort $1 -k3,3 -k2,2 -k1,1n)