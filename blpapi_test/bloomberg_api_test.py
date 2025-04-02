import blpapi
from blpapi import SessionOptions, Session

options = SessionOptions()
options.setServerHost('localhost')
options.setServerPort(8194)

session = Session(options)
if not session.start():
    print("Failed to start session.")
    exit()

if not session.openService("//blp/refdata"):
    print("Failed to open service.")
    exit()

service = session.getService("//blp/refdata")
request = service.createRequest("ReferenceDataRequest")
request.getElement("securities").appendValue("AAPL US Equity")
request.getElement("fields").appendValue("PX_LAST")

session.sendRequest(request)

while True:
    ev = session.nextEvent()
    for msg in ev:
        print(msg)
    if ev.eventType() == blpapi.Event.RESPONSE:
        break


