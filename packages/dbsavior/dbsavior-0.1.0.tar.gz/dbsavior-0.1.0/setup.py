# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dbsavior', 'dbsavior.db', 'dbsavior.storage']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.20.27,<2.0.0', 'psycopg2-binary>=2.9.3,<3.0.0']

setup_kwargs = {
    'name': 'dbsavior',
    'version': '0.1.0',
    'description': 'This backup restore bot can backup/restore a database and upload/download the backup file to/from a remote storage engine',
    'long_description': '# DataBaseBackupRestoreOnK8s\n\n## Project Introduction\nIf you have data that you want to import or export from a database that you deployed in a k8s cluster, you need to \ninstall a database client, create a dump file, then upload the dump file somewhere else. \n\nThis project will help you to avoid all that. The only thing you need to do is to provide the name of the database and\nwhere you want to upload/download the backup file. \n\n## Features\n\n* Create database backup file\n* Upload backup file to remote storage\n* Download backup file from remote storage\n* Restore/Populate database\n* Provide k8s cron job to create backup with configurable time interval \n* If you use auto backup/restore feature in the cronjob/job, the restore job will always find the latest backup of the\n  target database to do restore.\n* List available database that can be backed up.\n* List available backup that can be used to restore\n\n## Usage\n\nThere are different ways to use this project. \n1. Use this project as a python package\n2. Use this project as a python Command Line Interface\n3. Use this project as a k8s cronjob/job\n\n### Use this project as a python package\n\n### Use this project as a python Command Line Interface\n\nNote, if you use remote storage such as s3 (or minio), you need to set up your s3 creds correctly in your env variables.\n\n\n```shell\ngit clone https://github.com/pengfei99/K8sCronJobPostgresBackup.git\n\ncd K8sCronJobPostgresBackup\n\n# show the command line options and comments\npython dbsavior/main.py -h\n\n# list existing backup\npython dbsavior/main.py --db_type postgres --storage_type s3 --action list_backups --backup_dir s3://path/to/sql_backup\n\n# list existing database\npython dbsavior/main.py --db_type postgres --storage_type s3 --action list_dbs --db_login user-pengfei --db_pwd changeMe --db_host 127.0.0.1 --db_port 5432\n\n# auto backup\npython dbsavior/main.py --db_type postgres --storage_type s3 --action auto_backup --db_login user-pengfei --db_pwd changeMe --db_host 127.0.0.1 --backup_dir s3://path/to/sql_backup --target_db test\n \n# auto restore \npython dbsavior/main.py --db_type postgres --storage_type s3 --action auto_restore --db_login user-pengfei --db_pwd changeMe --db_host 127.0.0.1 --backup_dir s3://path/to/sql_backup --target_db test \n\n# populate a database with a sql dump\npython dbsavior/main.py --db_type postgres --storage_type s3 --action populate --db_login user-pengfei --db_pwd changeMe --db_host 127.0.0.1 --backup_file s3://path/to/sql_backup/2022-01-12_test_pg_bck.sql --target_db test\n\n```\n\n\n### Use this project as a k8s cronjob/job\n\nFor the job and cronjob is set up for s3 and postgresql. You need to add your s3 and postgresql server credentials\ninto the yaml file to run the job and cronjob correctly.\n\n```shell\ngit clone https://github.com/pengfei99/K8sCronJobPostgresBackup.git\n\ncd K8sCronJobPostgresBackup/k8s\n\n# this job calls auto backup on a database once\nkubectl apply -f job_backup.yaml\n\n# this cronjob calls auto backup on a database based on the cron. The default cron starts at mid night every day  \nkubectl apply -f cronjob_backup.yaml\n\n# this job calls auto restore of a database, if it finds many available backups, it will apply the latest one\nkubeclt apply -f job_restore.yaml\n\n# this job populate a database with a specific backup file.\nkubectl apply -f job_populate.yaml\n\n```\n\n## Future works\n\nFor now, this project only implements the postgres server for the **DbManagerInterface**. For the \n**StorageEngineInterface**, we only implement the s3 and local filesystem(tested for linux). If you want to back up a\ndatabase in a mysql server and store the backup on HDFS, you only need to implement the **DbManagerInterface** and \n**StorageEngineInterface**. The rest of the project can be reused automatically.\n\n## Other docs that may be useful for you\nIf you are not familiar with postgresql backup and restore procedure. Please visit\nthis [doc](docs/Postgres_db_backup_restore.md).\n\n\n',
    'author': 'Liu Pengfei',
    'author_email': 'liu.pengfei@hotmail.fr',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/pengfei99/K8sCronJobPostgresBackup',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
