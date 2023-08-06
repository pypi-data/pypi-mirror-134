from appyx.layers.application.application import Application


class PollsApplication(Application):

    @classmethod
    def running_context_test_dev(cls):
        return 'TEST_DEV'

    @classmethod
    def running_context_production(cls):
        return 'PROD'

    def _new_business(self):
        from polls.domain.poll_station import PollStation, FakeClock, SystemClock, QuestionsArchive
        business = None
        if self._running_context == self.running_context_test_dev():
            clock = FakeClock()
            business = PollStation(clock, QuestionsArchive())
        if self._running_context == self.running_context_production():
            clock = SystemClock()
            business = PollStation(clock, QuestionsArchive())
        if business is None:
            raise ValueError("Unrecognized running context: " + str(self._running_context))
        return business

    def default_running_context(self):
        return self.running_context_test_dev()
