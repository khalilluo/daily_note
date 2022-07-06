```shell
docker run --name dmdb -i -p 3307:3306 -v /home/panocom/docker/dmdb/conf:/etc/mysql -v /home/panocom/docker/dmdb/logs:/var/log/mysql -v /home/panocom/docker/dmdb/data:/var/lib/mysql -v /home/panocom/docker/dmdb/mysql-files:/var/lib/mysql-files/ -e MYSQL_ROOT_PASSWORD=123456 --restart=always -d  mysql:8.0.24 --default-authentication-plugin=mysql_native_password
```