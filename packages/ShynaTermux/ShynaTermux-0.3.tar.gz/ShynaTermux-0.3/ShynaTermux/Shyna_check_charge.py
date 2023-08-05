import os
from ShynaProcess import Shprocess


class ShynaCharge:
    s_process = Shprocess.ShynaSpeak()

    def check_charge(self):
        try:
            dic_charge = os.popen('termux-battery-status')
            charge = dic_charge['percentage']
            status = dic_charge['status']
            if int(charge) < 15 and str(status).lower() == 'discharging':
                self.s_process.shyna_speaks(msg="Hey! Shiv please plugin the charger. My battery is low")
            elif int(charge) == 100 and str(status).lower() == 'charging':
                self.s_process.shyna_speaks(msg="Hey! Shiv please unplug the charger. My battery is full")
            else:
                pass
        except Exception as e:
            print(e)


if __name__ == '__main__':
    ShynaCharge().check_charge()

