$OriginalDir = pwd
$Filename = "prometheus.conf"
$PathToConf = $OriginalDir + $Filename
cd "C:\Program Files\InfluxData\telegraf"
./telegraf --config $PathToConf