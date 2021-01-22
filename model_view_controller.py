import dataset_backend
from exchange_rate import CurrencyConverter


class ModelDataset(object):

    def __init__(self, application_items):
        self._item_type = 'currency_exchange_'
        self._connection = dataset_backend.connect_to_db(
            dataset_backend.DB_NAME, db_engine='postgres')
        dataset_backend.create_table(self.connection, self._item_type)
        self.create_items(application_items)

    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, new_item_type):
        self._item_type = new_item_type

    @property
    def connection(self):
        return self._connection

    # def create_item(self, dt, from_currency, from_amount, to_currency , to_amount, rate):
    #     dataset_backend.insert_one(
    #         self.connection, dt, from_currency, from_amount, to_currency , to_amount, rate, table_name=self.item_type)

    def create_items(self, items):
        dataset_backend.insert_many(
            self.connection, items, table_name=self.item_type)

    def read_item(self, id):
        return dataset_backend.select_one(
            self.connection, id, table_name=self.item_type)

    def read_items(self):
        return dataset_backend.select_all(
            self.connection, table_name=self.item_type)



class View(object):

    @staticmethod
    def show_bullet_point_list(item_type, items):
        print('--- {} LIST ---'.format(item_type.upper()))
        for item in items:
            print('* {}'.format(item))

    @staticmethod
    def show_number_point_list(item_type, items):
        print('--- {} LIST ---'.format(item_type.upper()))
        for i, item in enumerate(items):
            print('{}. {}'.format(i+1, item))


class Controller(object):

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show_items(self, bullet_points=False):
        items = self.model.read_items()
        item_type = self.model.item_type
        if bullet_points:
            self.view.show_bullet_point_list(item_type, items)
        else:
            self.view.show_number_point_list(item_type, items)


if __name__ == '__main__':
    API_KEY = 'ffb05d85592ed51d1220fcb3aafff91e'
    c1 = CurrencyConverter(API_KEY)

    global currency_rates
    currency_rates = c1.requestCurrency()
    timestamp = currency_rates['timestamp']
    currencyRates = currency_rates['quotes']

    print(timestamp)
    print(currencyRates)
    from_currency = "USD"
    to_currency = "EUR"
    from_amount ="5"
    targetCurrency = "EUR"
    currencyPair = 'USD' + targetCurrency
    exchangeRate = currencyRates[currencyPair]
    to_amount = exchangeRate * int(from_amount)
    rate = '$1 USD = {0} {1}'.format(exchangeRate, targetCurrency)
    print(rate)

    #{'base': 'USD', 'timestamp': '01-20-2021', 'quotes': {'USDAED': 3.673201, 'USDAFN': 78.190572, 'USDALL': 101.606546, 'USDAMD': 519.309746, 'USDANG': 1.793023, 'USDAOA': 656.379721, 'USDARS': 86.205805, 'USDAUD': 1.29511, 'USDAWG': 1.8, 'USDAZN': 1.701398, 'USDBAM': 1.610937, 'USDBBD': 2.016811, 'USDBDT': 84.699632, 'USDBGN': 1.610999, 'USDBHD': 0.377084, 'USDBIF': 1939.444108, 'USDBMD': 1, 'USDBND': 1.32709, 'USDBOB': 6.877221, 'USDBRL': 5.357868, 'USDBSD': 0.998851, 'USDBTC': 2.7703936e-05, 'USDBTN': 73.070559, 'USDBWP': 10.928634, 'USDBYN': 2.544776, 'USDBYR': 19600, 'USDBZD': 2.013434, 'USDCAD': 1.270915, 'USDCDF': 1970.000132, 'USDCHF': 0.887699, 'USDCLF': 0.02672, 'USDCLP': 737.289581, 'USDCNY': 6.470197, 'USDCOP': 3491.66, 'USDCRC': 608.433512, 'USDCUC': 1, 'USDCUP': 26.5, 'USDCVE': 90.820735, 'USDCZK': 21.535697, 'USDDJF': 177.827929, 'USDDKK': 6.12605, 'USDDOP': 58.094779, 'USDDZD': 133.005721, 'USDEGP': 15.716298, 'USDERN': 15.000113, 'USDETB': 39.393782, 'USDEUR': 0.823425, 'USDFJD': 2.04545, 'USDFKP': 0.732461, 'USDGBP': 0.732455, 'USDGEL': 3.303963, 'USDGGP': 0.732461, 'USDGHS': 5.823432, 'USDGIP': 0.732461, 'USDGMD': 51.702763, 'USDGNF': 10252.082844, 'USDGTQ': 7.781269, 'USDGYD': 208.978704, 'USDHKD': 7.75175, 'USDHNL': 24.078741, 'USDHRK': 6.228596, 'USDHTG': 72.598407, 'USDHUF': 294.665015, 'USDIDR': 14050, 'USDILS': 3.24843, 'USDIMP': 0.732461, 'USDINR': 73.169842, 'USDIQD': 1458.36199, 'USDIRR': 42104.999875, 'USDISK': 129.289708, 'USDJEP': 0.732461, 'USDJMD': 144.05792, 'USDJOD': 0.709044, 'USDJPY': 103.766024, 'USDKES': 110.080492, 'USDKGS': 84.7995, 'USDKHR': 4073.421246, 'USDKMF': 405.94966, 'USDKPW': 900.049792, 'USDKRW': 1099.304961, 'USDKWD': 0.30312, 'USDKYD': 0.832472, 'USDKZT': 419.464704, 'USDLAK': 9304.543714, 'USDLBP': 1510.260729, 'USDLKR': 193.287263, 'USDLRD': 169.00024, 'USDLSL': 15.2302, 'USDLTL': 2.95274, 'USDLVL': 0.60489, 'USDLYD': 4.459042, 'USDMAD': 8.928955, 'USDMDL': 17.310507, 'USDMGA': 3776.146018, 'USDMKD': 50.749735, 'USDMMK': 1330.502555, 'USDMNT': 2854.954807, 'USDMOP': 7.97557, 'USDMRO': 356.999828, 'USDMUR': 39.601597, 'USDMVR': 15.429814, 'USDMWK': 771.492346, 'USDMXN': 19.62087, 'USDMYR': 4.046982, 'USDMZN': 75.080094, 'USDNAD': 15.189539, 'USDNGN': 381.19779, 'USDNIO': 34.710914, 'USDNOK': 8.515701, 'USDNPR': 116.91356, 'USDNZD': 1.402405, 'USDOMR': 0.385027, 'USDPAB': 0.998933, 'USDPEN': 3.611497, 'USDPGK': 3.520923, 'USDPHP': 48.0345, 'USDPKR': 160.544274, 'USDPLN': 3.73495, 'USDPYG': 6862.230715, 'USDQAR': 3.64075, 'USDRON': 4.012794, 'USDRSD': 97.390663, 'USDRUB': 73.722, 'USDRWF': 990.663828, 'USDSAR': 3.750251, 'USDSBD': 7.970152, 'USDSCR': 21.204024, 'USDSDG': 55.325001, 'USDSEK': 8.332303, 'USDSGD': 1.32614, 'USDSHP': 0.732461, 'USDSLL': 10190.000051, 'USDSOS': 584.564276, 'USDSRD': 14.153983, 'USDSTD': 20834.863349, 'USDSVC': 8.740667, 'USDSYP': 512.825769, 'USDSZL': 14.946689, 'USDTHB': 29.989685, 'USDTJS': 11.382223, 'USDTMT': 3.51, 'USDTND': 2.704023, 'USDTOP': 2.292594, 'USDTRY': 7.462355, 'USDTTD': 6.771134, 'USDTWD': 27.988502, 'USDTZS': 2316.392045, 'USDUAH': 28.092777, 'USDUGX': 3685.873017, 'USDUSD': 1, 'USDUYU': 42.316943, 'USDUZS': 10489.006215, 'USDVEF': 9.987497, 'USDVND': 23076, 'USDVUV': 108.72749, 'USDWST': 2.533505, 'USDXAF': 540.284739, 'USDXAG': 0.03928, 'USDXAU': 0.000541, 'USDXCD': 2.70255, 'USDXDR': 0.693521, 'USDXOF': 540.284739, 'USDXPF': 98.92503, 'USDYER': 250.350105, 'USDZAR': 14.950201, 'USDZMK': 9001.207442, 'USDZMW': 21.305993, 'USDZWL': 322.000186}}
    #{'USDAED': 3.673201, 'USDAFN': 78.190572, 'USDALL': 101.606546, 'USDAMD': 519.309746, 'USDANG': 1.793023, 'USDAOA': 656.379721, 'USDARS': 86.205805, 'USDAUD': 1.29511, 'USDAWG': 1.8, 'USDAZN': 1.701398, 'USDBAM': 1.610937, 'USDBBD': 2.016811, 'USDBDT': 84.699632, 'USDBGN': 1.610999, 'USDBHD': 0.377084, 'USDBIF': 1939.444108, 'USDBMD': 1, 'USDBND': 1.32709, 'USDBOB': 6.877221, 'USDBRL': 5.357868, 'USDBSD': 0.998851, 'USDBTC': 2.7703936e-05, 'USDBTN': 73.070559, 'USDBWP': 10.928634, 'USDBYN': 2.544776, 'USDBYR': 19600, 'USDBZD': 2.013434, 'USDCAD': 1.270915, 'USDCDF': 1970.000132, 'USDCHF': 0.887699, 'USDCLF': 0.02672, 'USDCLP': 737.289581, 'USDCNY': 6.470197, 'USDCOP': 3491.66, 'USDCRC': 608.433512, 'USDCUC': 1, 'USDCUP': 26.5, 'USDCVE': 90.820735, 'USDCZK': 21.535697, 'USDDJF': 177.827929, 'USDDKK': 6.12605, 'USDDOP': 58.094779, 'USDDZD': 133.005721, 'USDEGP': 15.716298, 'USDERN': 15.000113, 'USDETB': 39.393782, 'USDEUR': 0.823425, 'USDFJD': 2.04545, 'USDFKP': 0.732461, 'USDGBP': 0.732455, 'USDGEL': 3.303963, 'USDGGP': 0.732461, 'USDGHS': 5.823432, 'USDGIP': 0.732461, 'USDGMD': 51.702763, 'USDGNF': 10252.082844, 'USDGTQ': 7.781269, 'USDGYD': 208.978704, 'USDHKD': 7.75175, 'USDHNL': 24.078741, 'USDHRK': 6.228596, 'USDHTG': 72.598407, 'USDHUF': 294.665015, 'USDIDR': 14050, 'USDILS': 3.24843, 'USDIMP': 0.732461, 'USDINR': 73.169842, 'USDIQD': 1458.36199, 'USDIRR': 42104.999875, 'USDISK': 129.289708, 'USDJEP': 0.732461, 'USDJMD': 144.05792, 'USDJOD': 0.709044, 'USDJPY': 103.766024, 'USDKES': 110.080492, 'USDKGS': 84.7995, 'USDKHR': 4073.421246, 'USDKMF': 405.94966, 'USDKPW': 900.049792, 'USDKRW': 1099.304961, 'USDKWD': 0.30312, 'USDKYD': 0.832472, 'USDKZT': 419.464704, 'USDLAK': 9304.543714, 'USDLBP': 1510.260729, 'USDLKR': 193.287263, 'USDLRD': 169.00024, 'USDLSL': 15.2302, 'USDLTL': 2.95274, 'USDLVL': 0.60489, 'USDLYD': 4.459042, 'USDMAD': 8.928955, 'USDMDL': 17.310507, 'USDMGA': 3776.146018, 'USDMKD': 50.749735, 'USDMMK': 1330.502555, 'USDMNT': 2854.954807, 'USDMOP': 7.97557, 'USDMRO': 356.999828, 'USDMUR': 39.601597, 'USDMVR': 15.429814, 'USDMWK': 771.492346, 'USDMXN': 19.62087, 'USDMYR': 4.046982, 'USDMZN': 75.080094, 'USDNAD': 15.189539, 'USDNGN': 381.19779, 'USDNIO': 34.710914, 'USDNOK': 8.515701, 'USDNPR': 116.91356, 'USDNZD': 1.402405, 'USDOMR': 0.385027, 'USDPAB': 0.998933, 'USDPEN': 3.611497, 'USDPGK': 3.520923, 'USDPHP': 48.0345, 'USDPKR': 160.544274, 'USDPLN': 3.73495, 'USDPYG': 6862.230715, 'USDQAR': 3.64075, 'USDRON': 4.012794, 'USDRSD': 97.390663, 'USDRUB': 73.722, 'USDRWF': 990.663828, 'USDSAR': 3.750251, 'USDSBD': 7.970152, 'USDSCR': 21.204024, 'USDSDG': 55.325001, 'USDSEK': 8.332303, 'USDSGD': 1.32614, 'USDSHP': 0.732461, 'USDSLL': 10190.000051, 'USDSOS': 584.564276, 'USDSRD': 14.153983, 'USDSTD': 20834.863349, 'USDSVC': 8.740667, 'USDSYP': 512.825769, 'USDSZL': 14.946689, 'USDTHB': 29.989685, 'USDTJS': 11.382223, 'USDTMT': 3.51, 'USDTND': 2.704023, 'USDTOP': 2.292594, 'USDTRY': 7.462355, 'USDTTD': 6.771134, 'USDTWD': 27.988502, 'USDTZS': 2316.392045, 'USDUAH': 28.092777, 'USDUGX': 3685.873017, 'USDUSD': 1, 'USDUYU': 42.316943, 'USDUZS': 10489.006215, 'USDVEF': 9.987497, 'USDVND': 23076, 'USDVUV': 108.72749, 'USDWST': 2.533505, 'USDXAF': 540.284739, 'USDXAG': 0.03928, 'USDXAU': 0.000541, 'USDXCD': 2.70255, 'USDXDR': 0.693521, 'USDXOF': 540.284739, 'USDXPF': 98.92503, 'USDYER': 250.350105, 'USDZAR': 14.950201, 'USDZMK': 9001.207442, 'USDZMW': 21.305993, 'USDZWL': 322.000186}

    my_items = [
        {'dt': '2012021', 'from_currency': 'USD', 'from_amount': '2', 'to_currency': 'EUR', 'to_amount': '5', 'rate': '1 usd = 0.9 eurr'},
        {'dt': '1912021', 'from_currency': 'USD', 'from_amount': '2', 'to_currency': 'EUR', 'to_amount': '5', 'rate': '1 usd = 0.9 eurr'},
        {'dt': '2112021', 'from_currency': 'USD', 'from_amount': '2', 'to_currency': 'EUR', 'to_amount': '5', 'rate': '1 usd = 0.9 eurr'},
        ]

    c = Controller(ModelDataset(my_items), View())
    c.show_items()
    c.show_items(bullet_points=True)

