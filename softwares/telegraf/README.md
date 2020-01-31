# Telgraf

## Installation 

```shell
sudo apt-get install telegraf
sudo service telegraf start
```

## Configuration

```
SHOW DATABASES
SHOW MEASUREMENTS

SELECT * FROM disk;

USE telegraf
ALTER RETENTION POLICY "autogen" ON "telegraf" DURATION 4w REPLICATION 1 DEFAULT;
CREATE RETENTION POLICY "forever" ON "telegraf" DURATION INF REPLICATION 1;
SHOW RETENTION POLICIES;

CREATE CONTINUOUS QUERY "disk_free_1h" ON "telegraf" RESAMPLE EVERY 1h BEGIN SELECT min("free") INTO "forever"."disk" FROM "autogen"."disk" WHERE device = 'root' GROUP BY time(1h) END
```
