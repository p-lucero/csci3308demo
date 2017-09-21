#! /bin/bash
# Paul Lucero

if [[ $# -ne 1 ]]; then
	echo "Usage: $0 filename"
	exit 1
fi

grep -c -E "[0-9]$" $1
grep -c -E "^[^aeiouAEIOU]" $1
grep -c -E "^[a-zA-Z]{12}$" $1
grep -c -E "[0-9]{3}-[0-9]{3}-[0-9]{4}" $1
grep -c -E "303-[0-9]{3}-[0-9]{4}" $1
grep -c -E "^[aeiouAEIOU].*[0-9]$" $1
grep -c -E "geocities.com$" $1
grep -c -E "@[^.]+$" $1
