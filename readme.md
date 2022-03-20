# srifintech CMS Base
159.89.164.119

## Setup and installation

- [ ] Clone the repository <br/>
      `git clone https://github.com/sriraj1122/srifintech.git`

- [ ] Install required libraries and dependencies <br/>
        `sudo apt-get update -y && sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib python3-venv nginx -y`


- [ ] Create Virtual Env <br/>
      `cd srifintech && python3 -m venv env`

- [ ] Activate Virtual Env <br/>
      `source env/bin/activate`

- [ ] Install dependencies <br/>
      `pip3 install wheel && pip3 install -r requirements.txt`



send db: 

sudo scp -i /home/ishant/brand.pem /home/ishant/ishant_linux/srifintech/srifintech/db.sqlite3 sriraj@52.172.35.186:/home/sriraj/srifintech

sudo scp -i /home/ishant/brand.pem /home/ishant/ishant_linux/srifintech/srifintech/media.zip sriraj@52.172.35.186:/home/sriraj/srifintech

sudo scp -i /home/ishant/brand.pem sriraj@52.172.35.186:/home/sriraj/srifintech/db.sqlite3 /home/ishant/ishant_linux/srifintech/srifintech

scp /home/ishant/ishant_linux/sriraj/srifintech/srifintech/email.json sriraj@128.199.28.207:/home/sriraj/srifintech/srifintech


#### Production Branch

Setup gunicorn :

sudo nano /etc/systemd/system/main.service


[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=ishant_do
Group=www-data
WorkingDirectory=/home/ishant_do/build/main
ExecStart=/home/ishant_do/build/main/env/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/ishant_do/build/main.sock srifintech.wsgi:application

[Install]
WantedBy=multi-user.target

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
nginx Setup:

sudo nano /etc/nginx/sites-available/main


server {
    listen 80;
    server_name srifintech.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/ishant_do/build/main;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ishant_do/build/main.sock;
    }

    location /media/ {
        alias /home/ishant_do/build/main/media/;
    }
}

sudo ln -s /etc/nginx/sites-available/main /etc/nginx/sites-enabled


#### QA Branch

Setup gunicorn :

sudo nano /etc/systemd/system/qa.service


[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=ishant_do
Group=www-data
WorkingDirectory=/home/ishant_do/build/qa
ExecStart=/home/ishant_do/build/qa/env/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/ishant_do/build/qa.sock srifintech.wsgi:application

[Install]
WantedBy=multi-user.target

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
nginx Setup:

sudo nano /etc/nginx/sites-available/qa


server {
    listen 80;
    server_name srifintech.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/ishant_do/build/qa;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ishant_do/build/qa.sock;
    }

    location /media/ {
        alias /home/ishant_do/build/qa/media/;
    }
}

sudo ln -s /etc/nginx/sites-available/qa /etc/nginx/sites-enabled

#### DEV Branch

Setup gunicorn :

sudo nano /etc/systemd/system/dev.service


[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=ishant_do
Group=www-data
WorkingDirectory=/home/ishant_do/build/dev
ExecStart=/home/ishant_do/build/dev/env/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/ishant_do/build/dev.sock srifintech.wsgi:application

[Install]
WantedBy=multi-user.target

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
nginx Setup:

sudo nano /etc/nginx/sites-available/dev


server {
    listen 80;
    server_name dev.srifintech.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/ishant_do/build/dev;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ishant_do/build/dev.sock;
    }

    location /media/ {
        alias /home/ishant_do/build/dev/media/;
    }
}

sudo ln -s /etc/nginx/sites-available/dev /etc/nginx/sites-enabled



#### To restart server
sudo pkill gunicorn
sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl restart nginx
sudo systemctl restart gunicorn.service


sudo systemctl restart main.service
sudo systemctl restart qa.service
sudo systemctl restart dev.service
sudo systemctl restart nginx

sudo python3 manage.py collectstatic --no-input

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

CMS PANEL : 



Products - Lexotique , kitchenji, etc - list of products - product x ( with the related fields , buy link )
Blogs  - Lexotique , kitchenji, etc - list of blogs - blogs x ( with the related fields )
settings - Users - Name , Site ownership , username and email/pass ( create general admin , create executive ) 
                          - Lexotique
                          - kitchenji
                          - Madhuram  



Settings - Site owners will have  multiple selection of 


Presentations:

Fresheys:
Web = https://docs.google.com/presentation/d/1lP4BtFX4kIW2gxr7FwuXHpxCKIaDnVkuIizkh-RHpc8/edit#slide=id.g966a22fd74_0_0
Mobile = https://docs.google.com/presentation/d/1jtG1jdyI6lg916VUsZMgMWnFDCgJquBZH0xYZiREY4I/edit


Lexotique:
Web = https://docs.google.com/presentation/d/1FRT00VIZJ7xr8YCDvPrVDcoSHlG9zcKeCezC2vNHHwk/edit?usp=sharing
Mobile = https://docs.google.com/presentation/d/1c0EECcwOZbK2mWitnevRsZa0wpzm1n0RJYg1Omr34cw/edit?usp=sharing


Cron command for emails

* * * * * /home/sriraj/srifintech/env/bin/python /home/sriraj/srifintech/manage.py send_queued_mail >> /home/sriraj/srifintech/send_mail.log 2>&1