import paramiko


class SSHClient(paramiko.SSHClient):
    def handler(self, title, instructions, prompt_list):
        answers = []

        for prompt_, _ in prompt_list:
            prompt = prompt_.strip().lower()
            print("'" + prompt + "'", prompt.startswith("Duo two-factor login"))
            if prompt.startswith("password"):
                answers.append(self.password)
            # TODO: Add ability to pass option 2 for a phone call
            elif prompt.startswith("duo two-factor login"):
                answers.append("1")
            else:
                raise ValueError("Unknown prompt: {}".format(prompt_))

        return answers

    def auth_interactive(self, username, handler):
        self._transport.auth_interactive(username, handler)

    def _auth(self, username, password, pkey, *args):
        self.password = password
        return self.auth_interactive(username, self.handler)
