# exampleQuartApp
 Example of how to deploy a Quart/Flask Server to an Azure VM with automatic deployment. More details will be added to the README.  

# Main Guide
Follow this tutorial mainly

[How to Deploy Flask Application Guide](https://medium.com/@adityaarya1/deploy-a-flask-application-to-azure-vm-with-a-ssl-certificate-d2960c50783d#id_token=eyJhbGciOiJSUzI1NiIsImtpZCI6IjQ4YTYzYmM0NzY3Zjg1NTBhNTMyZGM2MzBjZjdlYjQ5ZmYzOTdlN2MiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiIyMTYyOTYwMzU4MzQtazFrNnFlMDYwczJ0cDJhMmphbTRsamRjbXMwMHN0dGcuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJhdWQiOiIyMTYyOTYwMzU4MzQtazFrNnFlMDYwczJ0cDJhMmphbTRsamRjbXMwMHN0dGcuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJzdWIiOiIxMTgxMjk1NzA0MDkyMjkyMzExNDQiLCJlbWFpbCI6ImphY2tibGFpcmluZ0BnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwibmJmIjoxNzA1NjMwNDI5LCJuYW1lIjoiSmFjayBCbGFpciIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BQ2c4b2NMaGNVcnlUcERKLWdSSWNiSExrWFpuTTFIYmpNNmZjZXRRN3gwdHQwSWVWV0liPXM5Ni1jIiwiZ2l2ZW5fbmFtZSI6IkphY2siLCJmYW1pbHlfbmFtZSI6IkJsYWlyIiwibG9jYWxlIjoiZW4iLCJpYXQiOjE3MDU2MzA3MjksImV4cCI6MTcwNTYzNDMyOSwianRpIjoiYWI5ZDc1OTc4NGEwZDFiZmU0Njg5ZGEwNDQzOTRmNzRhYTNkZTA5OSJ9.e1eXLmUU8-r6CzwW3qo1Nrf_KOc-2W4b1sI6htjRBzFx3RxZOeGz7NECjUD5obXUTBVFUu5ne9aUCT0Q9dcsU61JsD1WctgDBFL_fQ6-lypGfNeJLisvwI_RoGkF9_KuPezcrZqZqdrmAhKIFIeC1om9si6qT0zlHHoBHbZgYk0qD5qpJrPP1UGDLbchdPTeDxyXDQ7wNsc0Vmq6PMMh9104mb_pbruHwivg9W7dCa6cb3QUr9MTgWlcvgyx9M-LNmJD2s1p2cxwxzT9ZFvv-2xXEdO2Ycj0oWegfs4QlvOjy5mbETdlUcAQgN0nlmnbzwHjq9g6mjtv3e47v9Yhzw)

However, creating a venv was werird. In worst case, dont create a venv and just install the packages globally.
must use sudo on `sudo gunicorn -b 0.0.0.0:8000 app:app` to run and see errors

`sudo gunicorn -b 0.0.0.0:8000 -k uvicorn.workers.UvicornWorker app:app`

```jsx
[Unit]
Description=Gunicorn instance for a simple quart app
After=network.target
[Service]
User=testing
Group=www-data
WorkingDirectory=/home/testing/exampleQuartApp
ExecStart=/home/testing/exampleQuartApp/venv/bin/gunicorn -b localhost:8000 app:app
Restart=always
[Install]
WantedBy=multi-user.target
```

====================================

Docker Installation
We have successfully logged in. Now start the Docker installation. Firstly, update our package manager with sudo apt-get update.

Check Docker documentation for more information and installation.

Type in the command line step by step.

sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo apt-key fingerprint 0EBFCD88

sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

sudo apt-get install docker-ce docker-ce-cli containerd.io

https://medium.com/hardwareandro/install-docker-on-azure-virtual-machine-github-docker-hub-azure-deploy-pipeline-part-1-4b1e73dd0d7

https://www.docker.com/blog/how-to-deploy-containers-to-azure-aci-using-docker-cli-and-compose/