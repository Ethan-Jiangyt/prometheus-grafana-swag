# This Powershell Script installs Telegraf and Grafana

# Install telegraf
wget https://dl.influxdata.com/telegraf/releases/telegraf-1.22.2_windows_amd64.zip -UseBasicParsing -OutFile telegraf-1.22.2_windows_amd64.zip
# Unzip and move to the right directory
Expand-Archive .\telegraf-1.22.2_windows_amd64.zip -DestinationPath 'C:\Program Files\InfluxData\telegraf'

# Install grafana
./grafana-enterprise-8.5.0.windows-amd64.msi
