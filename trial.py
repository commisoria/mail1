import smtplib
import yfinance as yf

gold = yf.download(tickers="GC=F", period="1d", interval="15m")
latest_price = gold['Close'].iloc[-1]


def prompt(prompt):
    return input(prompt).strip()


fromaddr = prompt("From:lex.commisoria@gmail.com")
toaddrs = prompt("To:ism.bolat@hotmail.com").split()
# Add the From: and To: headers at the start!
msg = (f"From: %s\r\nTo: %s\r\n\r\n {latest_price}"
       % (fromaddr, ", ".join(toaddrs)))
while True:
    try:
        line = input()
    except EOFError:
        break
    if not line:
        break
    msg = msg + line

print("Message length is", len(msg))
server = smtplib.SMTP('localhost', 1025)
server.set_debuglevel(1)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
