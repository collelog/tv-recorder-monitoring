FROM alpine:3.11
LABEL maintainer "collelog <collelog.cavamin@gmail.com>"

EXPOSE 9684

WORKDIR /usr/local/

RUN set -eux && \
	apk upgrade --update && \
	apk add --no-cache py-pip tzdata && \
	\
	# timezone
	cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
	echo "Asia/Tokyo" > /etc/timezone && \
	apk del tzdata && \
	\
	mkdir /usr/local/mirakurun && \
	cd /usr/local/mirakurun && \
	\
	# install Python Package
	pip install prometheus-client && \
	pip install requests-unixsocket && \
	\
	# cleaning
	rm -rf /tmp/* /var/cache/apk/*

COPY exec_mirakurun_exporter.py /usr/local/mirakurun/

WORKDIR /usr/local/mirakurun

ENTRYPOINT ["/usr/bin/python", "-u", "/usr/local/mirakurun/exec_mirakurun_exporter.py"]
