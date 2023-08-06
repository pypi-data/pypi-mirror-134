import subprocess

_command = "ydotool"


class YdoTool:
    def __init__(self):
        self.instructions = []
        # default sleep added for udev to kick in
        self.sleep(500)

    def exec(self):
        command = subprocess.run(
            [_command] + self.instructions,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if command.returncode != 0:
            raise Exception(command.stderr)

    def _add_instruction(self, instruction: list):
        self.instructions.extend([","] + instruction)

    @staticmethod
    def command(fun):
        def wrapper(self, *args, **kwargs):
            out = fun(self, *args, **kwargs)
            self._add_instruction(out)
            return self

        return wrapper

    @staticmethod
    def _parse_options(**kwargs):
        opts = []
        for key, value in kwargs.items():
            if value is True:
                opts.append(f"--{key}")
            elif value is not False:
                opts.extend([f"--{key}", value])
        return opts

    @command
    def sleep(self, delay: int):
        return ["sleep", delay]

    @command
    def key(self, keys, **kwargs):
        opts = self._parse_options(**kwargs)
        return ["key", keys] + opts

    @command
    def type(self, texts: str, **kwargs):
        opts = self._parse_options(**kwargs)
        return ["type", texts] + opts

    @command
    def mousemove(self, x: int, y: int, **kwargs):
        opts = self._parse_options(**kwargs)
        return ["mousemove", x, y] + opts

    @command
    def click(self, buttons: str, **kwargs):
        opts = self._parse_options(**kwargs)
        return ["click", buttons] + opts

    @command
    def recorder(self, **kwargs):
        if kwargs.get("replay") is None and kwargs.get("record") is None:
            raise ValueError("One of ['replay', 'record'] must be set.")
        if kwargs.get("replay") is not None and kwargs.get("record") is not None:
            raise ValueError("'replay' and 'record' can't be both set")
        opts = self._parse_options(**kwargs)
        return ["recorder"] + opts
