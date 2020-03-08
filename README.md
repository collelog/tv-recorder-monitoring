# TV Recorder Monitoring

> TV Recorder 使用環境の監視  
  
[cAdvisor](https://github.com/google/cadvisor) + [Prometheus](https://github.com/prometheus/prometheus) + [Grafana](https://grafana.com/) の監視系コンテナ群をdocker-composeで提供する「[dockprom](https://github.com/stefanprodan/dockprom)」プロジェクトを元に、「[TV Recorder](https://github.com/collelog/tv-recorder)」 の監視環境を整理しました。


## Dockerホスト実行条件
- TV Recorderが提供するDockerコンテナをデプロイ済みであること。
- 当プロジェクトのディレクトリ「tv-recorder-monitoring」（ディレクトリ名変更可）をTV Recorderのディレクトリ「tv-recorder」と同列階層に配置していること。

## 利用ソースコード
当ソースコードは以下のソースコード（docker-compose.yml,Dockerfile,その他動作に必要なファイル一式）を改変または参考に作成しています。

- **dockprom** ([stefanprodan/dockprom](https://github.com/stefanprodan/dockprom))  
Docker hosts and containers monitoring with Prometheus, Grafana, cAdvisor, NodeExporter and AlertManager
  - [MIT License](https://github.com/stefanprodan/dockprom/blob/master/LICENSE)


### 主な機能
- TV録画系コンテナ群の情報を集約したダッシュボード「TV Recorder」を用意しました。
  - [EPGStation](https://github.com/l3tnun/EPGStation) V1.6.xの録画番組数・ドロップ数をグラフ化します。
- [Mirakurun](https://github.com/Chinachu/Mirakurun)のStatus APIから性能情報を収集するPrometheus exporter（Dockerコンテナ：mirakurun-exporter）を用意しました。
  - ダッシュボード「Mirakurun」でグラフ化しています。

## 開発環境
> OS
>>Synology NAS DiskStation Manager 6.2
>>>Linux NAS01 4.4.59+ #24922 SMP PREEMPT Mon Aug 19 12:11:11 CST 2019 x86_64 GNU/Linux synology_denverton_1618+

>Docker
>> Version: 18.09.8, build 2c0a67b

>docker-compose
>> version 1.24.0, build 0aa59064


## License
このソースコードは [MIT License](https://github.com/collelog/tv-recorder-monitoring/blob/master/LICENSE) のもとでリリースします。
