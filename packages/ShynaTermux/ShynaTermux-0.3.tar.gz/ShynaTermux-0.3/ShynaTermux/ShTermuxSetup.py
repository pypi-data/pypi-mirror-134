import nltk
import os


class ShynaTermuxSetup:
    """We need setup few things to make it work and test"""
    case_env = ''

    def set_env_variable(self):
        try:
            self.case_env = input("Want to add Environment (y/n)")
            if self.case_env.__contains__('yes') or self.case_env.__contains__('y'):
                dbhost = input("Enter the database host")
                dbhost_cmd = "echo 'export host=" + dbhost + "'>>~/.profile;"
                os.popen(dbhost_cmd).readlines()
                dbpasswd = input("Enter the database password")
                dbhost_cmd = "echo 'export passwd=" + dbpasswd + "'>>~/.profile;"
                os.popen(dbhost_cmd).readlines()
                dbhost_cmd = "echo 'export bossname=Shivam'>>~/.profile;"
                os.popen(dbhost_cmd).readlines()
            else:
                pass
            self.case_env = input("Want to install remaining (y/n)")
            if self.case_env.__contains__('yes') or self.case_env.__contains__('y'):
                os.popen("pkg install sox --assume-yes").readlines()
                os.popen("pkg install termux-api --assume-yes").readlines()
                # os.popen('(crontab -l;echo "* * * * * .$HOME/.profile && termux-notification -t $host") | crontab -')
                dbhost_cmd = """termux-notification --on-delete 'termux-tts-speak "hey Shivam"' -t 'Hey Shivam' """
                os.popen(dbhost_cmd)
                nltk.download('all')
            else:
                pass
        except Exception as e:
            print(e)


if __name__ == '__main__':
    ShynaTermuxSetup().set_env_variable()
