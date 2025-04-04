import blpapi
from blpapi import SessionOptions, Session

def process_event(event):
    print(event.eventType())
    for msg in event:
        print(msg)
        # if msg.hasElement("messageText"):
        #     print("Headline:", msg.getElementAsString("messageText"))

def main():
    print("introduction")
    options = SessionOptions()
    options.setServerHost('localhost')  # or Bloomberg Server IP
    options.setServerPort(8194)

    session = Session(options)
    print("afters ession")

    if not session.start():
        print("Failed to start session.")
        return

    if not session.openService("//blp/mktnews"):
        print("Failed to open service.")
        return

    service = session.getService("//blp/mktnews")
    subscriptions = blpapi.SubscriptionList()

    print("subs: ", subscriptions)

    # Subscribe to all headlines – customize as needed
    # subscriptions.add("AAPL",  # News headline source
    #                   "storyId, messageText",
    #                   "",
    #                   blpapi.CorrelationId("news_sub"))
    subscriptions.add("AAPL")

    session.subscribe(subscriptions)

    print("after sub")
    while True:
        print("inside loop")
        try:
            event = session.nextEvent()
            print(event)
            if event.eventType() in (blpapi.Event.SUBSCRIPTION_DATA,
                                    blpapi.Event.SUBSCRIPTION_STATUS):
                process_event(event)
        except:
            print("Error while processing")

if __name__ == "__main__":
    main()
