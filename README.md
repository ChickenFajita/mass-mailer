## Table of contents
1. Description
2. Technologies
3. Setup
4. Performance
5. Next improvements

## 1. Description
Small program resulting from a coding challenge: 
> “Please write a program in your prefered language that will send out emails to recipients from a huge list (1 Mio entries) in a performant way. You do not need to > send real emails but just fake the email sending by waiting for half a second.”

This program takes any csv (emails must be in the first column) and broadcasts a configured plain text email towards all recipients. It uses SSL/TLS for encryption.

Authorization Code flow using OAuth2, which gains access to the resource with a token gained after authorization with the authorization server.

Using Gmail API and OAuth is beneficial since storing username and password will not be needed. Also there won't be the need to allow access for less secure apps on your gmail account. Gmail API with OAuth will allow you to only request the scope of access you need, while smtp gives full access.
I initially implemented the smtplib alternative, but was planning to implement authentication via OAuth2. Unfortunately I was not able to proceed, because I need to setup a OAuth consent screen.
As of now I can not choose the interal user type, because one needs to be a G Suite user, which requires your own domain. Going the route as an external user I will have to wait for authentication which can take 4-6 weeks
.
![workflow](https://miro.medium.com/max/1400/0*IsGZosgvxFHqNJYA.)

[src](https://miro.medium.com/max/1400/0*IsGZosgvxFHqNJYA.)

# 2. Technologies
Project is created with:
- Python version: 3.7

# 3. Setup
1. generate the password which this program will use to login with [apppasswords](https://myaccount.google.com/apppasswords)
2. allow access to your google account for less secure apps [lesssecureapps](https://myaccount.google.com/lessecureapps)
3. make sure your recipient list is in the project folder inside of the `names.csv` file with all the email adresses in the 1st column.

# 4. Run
1. open terminal
2. clone repo with `git clone https://github.com/ChickenFajita/mass-mailer.git`
3. open the folder with your preferred editor or IDE, edit config.py and enter your login data as well as subject and body of the message you are going to broadcast
4. execute the smtplib-mailer.py

# 5. Performance

**SMTP**:

Some solutions I saw were creating and destroying thread for every single email which is inefficient due to the three-way handshakes to setup the connection.
In this program I use a context manager to maintain the connection and prevent this extreme overhead and by holding the connection until all jobs were sent to the server.
Alternatively I could use thread pools that keep the connections and share the workload of sending all the emails. This problem is known as the thundering herd problem when too many threads are created simultaneously and try to access a single resource.

**Gmail API:**

Here I am looking to use batch requests to avoid multiple HTTP requests and do multiple API calls during one HTTP request.

# 6. Next steps

**Extend email functionalities**
- attachments and html bodies
- individual subjects, bodies and greetings along with a new csv format
- more secure and smooth login and authorization using OAuth2
- use gmail API
