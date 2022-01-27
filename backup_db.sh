#!/bin/sh
dump_path="/local/files"
backup_path="/local/backup"
db_name="app_db"
query='SELECT magazines.name, article_types.type, author.author FROM magazines, article_types, author, "Articles" WHERE "Articles".magazines_id=magazines.id AND "Articles".article_type_id=article_types.id AND "Articles".author_id=author.id;'
dump_count="3"
for db_name in $dump_path ; do
  echo $query |psql -d app_db -U postgres> $dump_path/app_db-`date \+\%Y-\%m-\%d-\%H:\%M:\%S`.sql
  num=$(ls -l ${dump_path} | wc -l)
  if [ ${num} -gt ${dump_count} ]
  then
    gzip -5 $dump_path/*.sql
    mv $dump_path/*.gz $backup_path
    echo "${num} files were moved into ${backup_path} directory"
    ls -l $backup_path
    else
    echo "No files were moved into ${backup_path} directory"
  fi ;
done
