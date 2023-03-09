from . import monad

class CliError(Exception):
    """
    Base Error Class for Job errors
    """

    def __init__(self, message="", name="", ctx={}, code=500, klass="", retryable=False, traceback: str = None):
        self.code = 500 if code is None else code
        self.retryable = retryable
        self.message = message
        self.name = name
        self.ctx = ctx
        self.klass = klass
        self.traceback = traceback
        super().__init__(self.message)

    def error(self):
        return {'error': self.message, 'code': self.code, 'step': self.name, 'ctx': self.ctx}

    def __str__(self):
        return f"error: {self.message}, code: {self.code}"

class ValidationError(CliError):
    pass

class FileWritingError(CliError):
    pass

class TemplateFormattingError(CliError):
    pass

def error_message(ex: monad.EitherMonad):
    if not isinstance(ex, monad.MEither) or ex.is_right():
        return None
    if isinstance(ex.error(), CliError):
        return ex.error().message
    return str(ex.error())

def error_ctx(ex: monad.EitherMonad):
    if not isinstance(ex, monad.MEither) or ex.is_right():
        return None
    if isinstance(ex.error(), CliError):
        return ex.error().ctx
    return str(ex.error())


