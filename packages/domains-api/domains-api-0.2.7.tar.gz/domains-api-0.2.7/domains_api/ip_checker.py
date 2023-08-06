import os
import sys
import getopt
import base64
import smtplib
from email.message import EmailMessage
from getpass import getpass
from itertools import cycle

from requests import get, post
from requests.exceptions import ConnectionError as ReqConError

from .file_handlers import FileHandlers


fh = FileHandlers()

# # Uncomment or replicate in your code to set log level:
# fh.set_log_level('debug')
# fh.initialize_loggers()


def get_ip_only():
    """Gets current external IP from ipify.org"""
    current_ip = get("https://api.ipify.org").text
    return current_ip


class BaseUser:
    def __init__(self):
        """Create user instance and save it for future changes to API and for email notifications."""
        self.domain = input(
            'What is the reference for this IP? (Anything you like, e.g "example.com" or "Work PC"): '
        )
        self.notifications, self.gmail_address, self.gmail_password = self.set_email()
        self.outbox = []
        self.previous_ip = ""

    def set_email(self):
        """Set/return attributes for Gmail credentials if user enables notifications"""
        self.notifications = input(
            "Enable email notifications? [Y]all(default); [e]errors only; [n]no: "
        ).lower()
        if self.notifications != "n":
            self.gmail_address = input("What's your email address?: ")
            self.gmail_password = base64.b64encode(
                getpass(
                    "What's your email(less secure)/app(more secure) password?: "
                ).encode("utf-8")
            )
            if self.notifications != "e":
                self.notifications = "Y"
            return self.notifications, self.gmail_address, self.gmail_password
        else:
            return "n", None, None

    def send_notification(
        self, ip=None, msg_type="success", error=None, outbox_msg=None
    ):
        """Notify user via email if IP change is made successfully or if API call fails."""
        if self.notifications != "n":
            msg = EmailMessage()
            msg["From"] = self.gmail_address
            msg["To"] = self.gmail_address
            if ip and msg_type == "success" and self.notifications != "e":
                msg.set_content(f"IP for {self.domain} has changed! New IP: {ip}")
                msg["Subject"] = "Your IP has changed!"
            elif msg_type == "error":
                msg.set_content(f"Error with {self.domain}'s IPChanger: ({error})!")
                msg["Subject"] = "IPCHANGER ERROR!"
            elif outbox_msg:
                msg = outbox_msg

            try:
                server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                server.ehlo()
                server.login(
                    self.gmail_address,
                    base64.b64decode(self.gmail_password).decode("utf-8"),
                )
                server.send_message(msg)
                server.close()
                return True
            except Exception as e:
                log_msg = "Email notification not sent: %s" % e
                fh.log(log_msg, "warning")
                self.outbox.append(msg)
                fh.save_user(self)

    def set_domains_credentials(self):
        raise NotImplementedError


class IPChecker:
    ARG_STRING = "defhil:ns"
    ARG_LIST = [
        "delete_user",
        "email",
        "force",
        "help",
        "ip",
        "load_user=",
        "notifications",
        "simulate",
    ]

    def __init__(self, argv=None, user_type=BaseUser):
        """Check for command line arguments, load/create User instance,
        check previous IP address against current external IP, and change via the API if different."""
        self.changed = False
        self.current_ip = self.get_set_ip()
        # Load old user, or create new one:
        if os.path.isfile(fh.user_file):
            self.user = fh.load_user(fh.user_file)
            fh.log("User loaded from pickle", "debug")
        elif arg := [arg for arg in sys.argv if arg in {"-l", "--load_user"}]:
            try:
                self.user = fh.load_user(sys.argv[sys.argv.index(arg[0]) + 1])
                fh.log("User loaded from pickle", "debug")
                fh.save_user(self.user)
                fh.log("New user saved", "info")
                return
            except Exception as e:
                raise e
        else:
            self.user = user_type()
            fh.log(
                "New user created.\n(See `python -m domains_api --help` for help changing/removing the user)",
                "info",
            )

        # Parse command line options:
        try:
            opts, _args = getopt.getopt(argv, self.ARG_STRING, self.ARG_LIST)
        except getopt.GetoptError:
            print(
                """Usage:
        python/python3 -m domains_api --help"""
            )
            sys.exit(2)
        if opts:
            self.arg_parse(opts)
        else:
            self.check_ip()

    def get_set_ip(self):
        """Gets current external IP from api.ipify.org and sets self.current_ip"""
        try:
            return get_ip_only()
        except (ReqConError, ConnectionError) as e:
            fh.log("Connection Error. Could not reach api.ipify.org", "warning")
            self.user.send_notification(msg_type="error", error=e)

    def check_ip(self):
        try:
            if self.user.previous_ip == self.current_ip:
                log_msg = "Current IP: %s (no change)" % self.user.previous_ip
                fh.log(log_msg, "debug")
            else:
                self.user.previous_ip = self.current_ip
                self.changed = True
                fh.save_user(self.user)
                log_msg = "Newly recorded IP: %s" % self.user.previous_ip
                fh.log(log_msg, "info")
        except AttributeError:
            setattr(self.user, "previous_ip", self.current_ip)
            self.changed = True
            log_msg = "Newly recorded IP: %s" % self.user.previous_ip
            fh.log(log_msg, "info")
            fh.save_user(self.user)
        finally:
            if fh.op_sys == "pos" and os.geteuid() == 0:
                fh.set_permissions(fh.user_file)

            # Send outbox emails:
            if self.user.outbox:
                for i in range(len(self.user.outbox)):
                    if self.user.send_notification(outbox_msg=self.user.outbox.pop(i)):
                        fh.log("Outbox message sent", "info")
                fh.save_user(self.user)
            fh.clear_logs()

    def arg_parse(self, opts):
        """Parses command line options: e.g. "python -m domains_api --help" """
        for opt, arg in opts:
            if opt in {"-i", "--ip"}:
                print(
                    """
[Domains API] Current external IP: %s
                """
                    % get_ip_only()
                )
            if opt in {"-h", "--help"}:
                print(
                    """

    domains-api help manual (command line options):
    ```````````````````````````````````````````````````````````````````````````````````````

    python -m domains_api                    || - set up /or check ip, change if necessary
    python -m domains_api -f --force         || - force domains API call, necessary or not
    python -m domains_api -h --help          || - show this help manual
    python -m domains_api -i --ip            || - show current external IP address
    python -m domains_api -e --email         || - email set up wizard
    python -m domains_api -n --notifications || - toggle email notification settings
    python -m domains_api -d --delete_user   || - delete current email/domains profile
    python -m domains_api -l --load_user     || - load email/domains profile from file

    *User profile is stored as "../site-packages/domains_api/domains.user"
    """
                )

            elif opt in {"-d", "--delete"}:
                fh.delete_user()
                fh.log("User deleted", "info")
                print(
                    ">>> Run the script without options to create a new user, or "
                    '"python3 -m domains_api -l path/to/pickle" to load one from file'
                )

            elif opt in {"-e", "--email"}:
                self.user.set_email()
                fh.save_user(self.user)
                fh.log("Notification settings changed", "info")

            elif opt in {"-l", "--load_user"}:
                if (
                    input("Are you sure you want to load a new user? [Y/n]").lower()
                    == "n"
                ):
                    return
                self.user = fh.load_user(arg)
                fh.save_user(self.user)
                fh.log("New user loaded", "info")

            elif opt in {"-n", "--notifications"}:
                n_options = {"Y": "[all changes]", "e": "[errors only]", "n": "[none]"}
                options_iter = cycle(n_options.keys())
                for option in options_iter:
                    if self.user.notifications == option:
                        break
                self.user.notifications = next(options_iter)
                fh.save_user(self.user)
                log_msg = (
                    "Notification settings changed to %s"
                    % n_options[self.user.notifications]
                )
                fh.log(log_msg, "info")
                if (
                    self.user.notifications in {"Y", "e"}
                    and not self.user.gmail_address
                ):
                    fh.log("No email user set, running email set up wizard...", "info")
                    self.user.set_email()
                    fh.save_user(self.user)

            elif opt in {"-f", "--force"}:
                fh.log("***Forcing API call***", "info")
                self.changed = True


if __name__ == "__main__":
    IPChecker(sys.argv[1:])
