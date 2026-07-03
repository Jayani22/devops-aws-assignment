!/bin/bash

BACKUP_DIR="$HOME/backups"
DATE=$(date +%F-%H-%M)

mkdir -p $BACKUP_DIR

tar -czf $BACKUP_DIR/app-$DATE.tar.gz $HOME/devops-aws-assignment

aws s3 cp $BACKUP_DIR/app-$DATE.tar.gz s3://jayani-devops-assignment-backup-01/