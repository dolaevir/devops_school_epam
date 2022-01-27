#!/usr/bin/bash

pid=/var/run/mail.pid
backup_path=/local/backup
max_n=4
max_size=8196

while true
do
echo $$ > ${pid}

num=$(ls -l ${backup_path} | wc -l)
size=$(du -b ${backup_path} | cut -f1)

if [ ${num} -gt ${max_n} ]
then
        echo "There are ${num} files in ${backup}" | mail -s "WARNING! There are many files in backups" root@localhost
fi

if [ ${size} -gt ${max_size} ]
then
        echo "There are ${size} bytes in ${backup}" | mail -s "WARNING! Backups take up too much space" root@localhost
fi

sleep 30

done
