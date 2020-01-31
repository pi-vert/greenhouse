# Grafana

```shell
wget https://dl.grafana.com/oss/release/grafana_6.4.4_armhf.deb
sudo apt-get install libfontconfig1
sudo dpkg -i grafana_6.4.4_armhf.deb
sudo systemctl enable grafana-server
sudo systemctl start grafana-server
```

## Plugins

```shell
sudo grafana-cli plugins install grafana-clock-panel
sudo grafana-cli plugins install natel-discrete-panel
sudo grafana-cli plugins install briangann-gauge-panel
sudo grafana-cli plugins install vonage-status-panel
sudo grafana-cli plugins install neocat-cal-heatmap-panel
sudo grafana-cli plugins install natel-plotly-panel
```
