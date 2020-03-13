import os
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
	name = request.form.get("name") # if method is 'GET', xxx = request.args.get("xxx")
	mail = request.form.get("mail")
	dorm = request.form.get("dorm") # if method is 'POST', xxx = request.form.get("xxx")
	if not name or not mail or not dorm:
		return render_template("failure.html")
	
	# set third-part smtp server
	mail_host = "smtp.163.com"
	from_account = "brysjhhrhl95@163.com"
	to_account = mail

	# set message
	content = "Dear %s, congratulate that you have registered successfully, and your information is as follow:\nName: %s\nEmail: %s\nDorm: %s\n" %(name, name, to_account, dorm)
	message = MIMEText(content, 'plain', 'utf-8') # content, format, code
	message['Subject'] = "Froshims Project"
	message['From'] = from_account
	message['To'] = to_account
	
	# check if get password from system, noting that password is authentic code of 163.com, not password for email!!!
	pw = os.getenv("password")
	if not pw:
		print("please export password in server's system environment.")
		return ("fail to get password")

	try:
		server = smtplib.SMTP_SSL(mail_host, 994)
		server.login(from_account , os.getenv("password"))
		server.sendmail(from_account, to_account, message.as_string())
		print("The mail has been sent successfully to %s." %(to_account))

		# generate mail login page, noting 'https' must be added when using '<a>' tag 
		mail_host_name = to_account[to_account.find('@')+1 : ]
		mail_login_page = "https://mail." + mail_host_name

		return render_template("success.html", name=name, email=to_account, email_login_page=mail_login_page)
	
	except smtplib.SMTPException as e:
		print(e)
		return render_template("server_failure.html")
