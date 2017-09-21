#! /bin/bash
# Paul Lucero

if [[ $# -ne 1 ]]; then
	echo "Usage: $0 filename"
	exit 1
fi

sort $1 -k3,3 -k2,2 -k1,1n | awk '{print ($4+$5+$6)/3, "["$1"]", $3",", $2}'