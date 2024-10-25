installing docker:
1. go to folder which is located ```docker.sh```
2. install below commmands

```bash
chmod +x docker.sh
./docker.sh
```



image building commands:
docker build --tag p24_news .

running container:
docker run --publish 8000:8000 p24_news
                      out:in
