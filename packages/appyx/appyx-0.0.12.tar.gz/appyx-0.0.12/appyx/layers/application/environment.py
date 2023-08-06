class Environment:
    CURRENT_APP = None

    def current_app(self):
        if self.__class__.CURRENT_APP is None:
            self.__class__.CURRENT_APP = self._new_application()
        return self.__class__.CURRENT_APP

    def _new_application(self):
        context = self._running_context()
        app_class = self._application_class()
        return app_class(context)

    def reset_current_app(self):
        self.__class__.CURRENT_APP = None

    def _application_class(self):
        raise NotImplementedError('Subclass responsibility')

    def _running_context(self):
        raise NotImplementedError('Subclass responsibility')
