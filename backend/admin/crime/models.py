from admin.common.models import ValueObject, Reader, Printer


class CrimeCctvModel():
    vo = ValueObject()
    reader = Reader()
    printer = Printer()

    def __init__(self):
        '''
        Raw Data 의  features 를 가져온다.
        살인 발생,살인 검거,강도 발생,강도 검거,강간 발생,강간 검거,절도 발생,절도 검거,폭력 발생,폭력 검거
        '''
        self.crime_columns = ['살인발생', '강도발생', '강간발생', '절도발생', '폭력발생'] # Nominal
        self.arrest_columns = ['살인검거', '강도검거', '강간검거', '절도검거', '폭력검거'] # Nominal
        self.crime_rate_column = ['살인검거율', '강도검거율', '강간검거율', '절도검거율', '폭력검거율'] # Ratio

    def create_crime_model(self):
        vo = self.vo
        reader = self.reader
        printer = self.printer
        vo.context = 'admin/crime/data/'
        vo.fname = 'crime_in_Seoul'
        crime_file_name = reader.new_file(vo)
        print(f'파일명: {crime_file_name}')
        crime_model = reader.csv(crime_file_name)
        printer.dframe(crime_model)
        return crime_model

    def create_police_position(self):
        crime = self.create_crime_model()
        reader = self.reader
        # vo = self.vo
        station_names = []
        [station_names.append('서울'+str(name[:-1] + '경찰서')) for name in crime['관서명']]
        station_address = []
        station_lats = []
        station_lngs = []
        gmaps = reader.gmaps()
        for name in station_names:
            temp = gmaps.geocode(name, language='ko')
            station_address.append(temp[0].get('formatted_address'))
            temp_loc = temp[0].get('geometry')
            station_lats.append(temp_loc['location']['lat'])
            station_lngs.append(temp_loc['location']['lng'])
            print(f'name : {temp[0].get("formatted_address")}')
        gu_names = []
        for name in station_address:
            temp = name.split()
            gu_name = [gu for gu in temp if gu[-1] == '구'][0]
            gu_names.append(gu_name)
        crime['구별'] = gu_names
        # 구와 경찰서의 위치가 다른 경우 수작업
        # crime.loc[crime['관서명'] == '혜화서', ['구별']] = '종로구'
        # crime.loc[crime['관서명'] == '서부서', ['구별']] = '은평구'
        print('==========================================================')
        print(f"샘플 중 혜화서 정보 : {crime[crime['관서명'] == '혜화서']}")
        print(f"샘플 중 금천서 정보 : {crime[crime['관서명'] == '금천서']}")
        # crime.to_csv(vo.context+'new_data/police_positions.csv')

    # def create_crime_rate_model(self):
    #     pass

    def create_cctv_model(self):
        vo = self.vo
        reader = self.reader
        printer = self.printer
        vo.context = 'admin/crime/data/'
        vo.fname = 'CCTV_in_Seoul'
        cctv_file_name = reader.new_file(vo)
        cctv_model = reader.csv(cctv_file_name)
        cctv_model.rename(columns={'기관명': '구별'}, inplace=True)
        printer.dframe(cctv_model)
        cctv_model.to_csv(vo.context+'new_data/cctv_positions.csv')
        return cctv_model

    def create_population_model(self):
        vo = self.vo
        reader = self.reader
        printer = self.printer
        vo.context = 'admin/crime/data/'
        vo.fname = 'population_in_Seoul'
        population_file_name = reader.new_file(vo)
        # ('B', 'D', 'G', 'J', 'N')
        population_model = reader.xls(population_file_name, 1, ('B, D, G, J, N'))
        population_model.rename(columns={'자치구': '구별'}, inplace=True)
        printer.dframe(population_model)
        population_model.to_csv(vo.context+'new_data/population_positions.csv')
        return population_model
