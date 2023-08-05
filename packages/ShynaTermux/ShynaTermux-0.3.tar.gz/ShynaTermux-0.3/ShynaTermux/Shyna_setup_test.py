from ShynaProcess import Shprocess
import os
from ShynaDatabase import Shdatabase


class ShynaStartTest:
    s_process = Shprocess.ShynaSpeak()
    s_data = Shdatabase.ShynaDatabase()
    s_data.host = os.environ.get('host')
    s_data.passwd = os.environ.get('passwd')
    s_data.device_id = "termux"

    def test_tts(self):
        msg = "hello" + str(os.environ.get("bossname"))
        self.s_process.shyna_speaks(msg=msg)
        self.s_data.set_date_system(process_name="termux_test")


if __name__ == '__main__':
    ShynaStartTest().test_tts()
