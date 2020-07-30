## Table of contents
1. Description
2. Technologies
3. Setup
4. Run
5. Performance
6. Next improvements

## 1. Description
Small program to supplement some emailing work.

This program takes a csv its lines representing tuples (email, subject, msg) and sends all emails. This makes quick editing with sheets with the option of using individual subjects and message bodies for each recipient. Analogously broadcasting the same message is possible. SSL/TLS is used for encryption.

Using Gmail API and OAuth is beneficial since storing username and password will not be needed. Also there won't be the need to allow access for less secure apps on your gmail account. Gmail API with OAuth will allow you to only request the scope of access you need, while smtp gives full access.
I initially implemented the smtplib alternative, but was planning to implement authentication via OAuth2. Unfortunately I was not able to proceed, because I need to setup a OAuth consent screen.
As of now I can not choose the interal user type, because one needs to be a G Suite user, which requires your own domain. Going the route as an external user I will have to wait for authentication which can take 4-6 weeks

![workflow](https://miro.medium.com/max/1400/0*IsGZosgvxFHqNJYA.)

[src](https://miro.medium.com/max/1400/0*IsGZosgvxFHqNJYA.)

# 2. Technologies
Project is created with:
- Python version: 3.7

# 3. Setup
1. generate the password which this program will use to login with [apppasswords](https://myaccount.google.com/apppasswords)
2. allow access to your google account for less secure apps [lesssecureapps](https://myaccount.google.com/lessecureapps)

# 4. Run
1. open terminal
2. clone repo with `git clone https://github.com/ChickenFajita/mass-mailer.git`
3. open the csv file in excel or any sheet editor and edit all messages you want to send. Avoid double semicolons and make sure the following format is used **(email, subject, msg)**
4. open config.py and enter email and the app password
5. execute the smtplib-mailer.py

# 5. Performance

**SMTP**:

Some solutions I saw were creating and destroying the thread for every single email which is inefficient due to the three-way handshakes to setup the connection.
In this program I use a context manager to maintain the connection and prevent this extreme overhead and by holding the connection until all jobs were sent to the server.
Alternatively I could use thread pools that keep the connections and share the workload of sending all the emails. This problem is known as the thundering herd problem when too many threads are created simultaneously and try to access a single resource.

**Gmail API:**

Here I am looking to use batch requests to avoid multiple HTTP requests and do multiple API calls during one HTTP request.

# 6. Next steps

**Extend email functionalities**
- attachments and html bodies
- thread pools and multiple connections?
- more secure and smooth login and authorization using OAuth2
- use gmail API
