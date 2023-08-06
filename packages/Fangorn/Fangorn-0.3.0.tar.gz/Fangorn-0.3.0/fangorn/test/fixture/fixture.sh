#!/bin/bash

DIR=`dirname "$0"`

restore() {
  mysql --user=guest < $DIR/mysql_schema.sql
  mysql --user=guest test_fangorn < $DIR/data.sql
  
  rm -f $DIR/sqlite.db
  sqlite3 $DIR/sqlite.db < $DIR/sqlite_schema.sql
  sqlite3 $DIR/sqlite.db < $DIR/data.sql
}

dump() {
  mysqldump --no-data --databases --user=guest test_fangorn > $DIR/mysql_schema.sql

  mysqldump --no-autocommit --no-create-info --skip-opt --skip-extended-insert \
    --user=guest test_fangorn | sed 's/set autocommit=0;/begin;/g' > $DIR/data.sql
    
  sqlite3 $DIR/sqlite.db .schema > $DIR/sqlite_schema.sql
}

case $1 in
  restore)
    restore
    ;;
  dump)
    dump
    ;;
  *)
    echo "Usage: ./fixture.sh dump|restore"
    exit 1
    ;;
esac
