from appyx.layers.application.environment import Environment
from polls.polls_application import PollsApplication


class PollsEnvironment(Environment):

    def _application_class(self):
        return PollsApplication

    def _running_context(self):
        test = 'TEST'
        prod = 'PROD'
        environment_variable = self.get_or_default('ENVIRONMENT', test)
        context = PollsApplication.running_context_test_dev()
        if environment_variable == prod:
            context = PollsApplication.running_context_production()
        # Rellenar el context con mas variables leidas del ambiente

        return context

    def get_or_default(self, var, default):
        try:
            import os
            return os.environ[var]
        except KeyError:
            import logging
            logging.info("Using default value '{}' for environment variable {}".format(default, var))
            return default
