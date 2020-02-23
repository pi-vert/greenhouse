import influxdb_client
from influxdb_client import InfluxDBClient

## You can generate a Token from the "Tokens Tab" in the UI
client = InfluxDBClient(url="https://eu-central-1-1.aws.cloud2.influxdata.com", token="ruutArT4eY7CI-DYea_nYeOweEb8AP-ot1lW4YRpFH-ONSYOo5Gqux2ol4XUpPL0j9osHK111rvBTgWdllz7dQ==")

data = "mem,host=host1 used_percent=23.43234543 1556896326"
write_client.write("bucketID", "165e8fa3788acc22", data)
