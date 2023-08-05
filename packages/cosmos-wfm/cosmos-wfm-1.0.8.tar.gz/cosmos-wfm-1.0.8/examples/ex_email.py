from cosmos import Cosmos, signal_execution_status_change, ExecutionStatus
from ex1 import main

()


def main(execution):
    @signal_execution_status_change.connect
    def sig(ex):
        msg = "%s %s" % (ex, ex.status)
        if ex.status in [ExecutionStatus.successful, ExecutionStatus.failed, ExecutionStatus.killed]:
            text_message(msg)
            ex.log.info('Sent a text message')

    def text_message(message):
        from twilio.rest import TwilioRestClient

        account = "XYZ"
        token = "XYZ"
        client = TwilioRestClient(account, token)

        message = client.messages.create(to="+1231231234", from_="+1231231234", body=message)

    main(execution)


if __name__ == '__main__':
    cosmos = Cosmos('sqlite:///%s/sqlite.db' % os.path.dirname(os.path.abspath(__file__)))
    cosmos.initdb()

    execution = cosmos.start('Example1', 'out/ex1', max_attempts=2, restart=True, skip_confirm=True)
    main(execution)