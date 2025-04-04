import blpapi
from blpapi import SessionOptions, Session

def process_event(event):
    for msg in event:
        if msg.hasElement("messageText"):
            print("Headline:", msg.getElementAsString("messageText"))

def main():
    options = SessionOptions()
    options.setServerHost('localhost')  # or Bloomberg Server IP
    options.setServerPort(8194)

    session = Session(options)

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
    subscriptions.add("AAPL",  # News headline source
                      "storyId, messageText",
                      "",
                      blpapi.CorrelationId("news_sub"))

    session.subscribe(subscriptions)

    while True:
        event = session.nextEvent()
        if event.eventType() in (blpapi.Event.SUBSCRIPTION_DATA,
                                 blpapi.Event.SUBSCRIPTION_STATUS):
            process_event(event)

if __name__ == "__main__":
    main()
