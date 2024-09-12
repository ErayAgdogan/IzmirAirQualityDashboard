import string_res.string_keys as keys

LANGUAGE='language'

EN = 'en'
TR = 'tr'
TURKISH = 'Turkish'

_string_res = {
    TR: {
        keys.PAGE_TITLE: 'İzmir Hava Kalitesi',
        keys.MAP: 'Harita',
        keys.BAR: 'Bar',
        keys.IZMIR_AIR_QUALITY: '🌍 İzmir Hava Kalitesi',
        keys.SELECT_A_DATE: 'bir tarih seç',
        keys.SELECT_POLLUTANT: 'kirletici seç',
        keys.IZMIR_POLLUTANT_DATA: 'İzmir {pollutant} Verileri',
        keys.ABOUT_COLOR_CODES: 'Renk kodları hakkında',
        keys.DATA_AND_TRENDS: 'Veriler/Eğilimler',
        keys.NO_DATA: 'Veri Yok',
        keys.VALUE_IS: 'değeri',
        keys.PREVIOUS_DAYS_VALUE_IS: "önceki günün değeri",



        keys.GOOD: 'iyi',
        keys.MODERATE: 'orta',
        keys.SENSITIVE: 'hassas',
        keys.UNHEALTHY: 'sağlıksız',
        keys.VERY_UNHEALTHY: 'kötü',
        keys.HAZARDOUS: 'tehlikeli',

        keys.AIR_QUALITY_IS: 'Hava kalitesi',

        keys.HIDE_PREVIOUS_DAYS_VALUE: "Önceki Günün Verilerini Sakla",
        keys.SHOW_REVIOUS_DAYS_VALUE: "Önceki Günün Verilerini Göster",

        keys.SORT_BY: 'Sırala',
        keys.DEFAULT: 'Varsayılan',
        keys.VALUE: 'Değer',
        keys.TREND: 'Eğilim',
        keys.INCREASING: 'Artan',
        keys.DECREASING: 'Azalan',

        keys.COLOR_CODE_EXPLANATION: '''            
- <span style="color:green">İyi</span>: Hava kalitesi memnun edici ve hava kirliliği az riskli veya hiç risk teşkil etmiyor.
- <span style="color:yellow">Orta</span>:	Hava kalitesi uygun fakat alışılmadık şekilde hava kirliliğine hassas olan çok az sayıdaki insanlar için bazı kirleticiler açısından orta düzeyde sağlık endişesi oluşabilir.
- <span style="color:orange">Hassas</span>: Hassas gruplar için sağlık etkileri oluşabilir. Genel olarak kamunun etkilenmesi olası değildir.
- <span style="color:red">Sağlıksız</span>: Herkes sağlık etkileri yaşamaya başlayabilir, hassas gruplar için ciddi sağlık etkileri söz konusu olabilir.
- <span style="color:purple">Kötü</span>: Sağlık açısından acil durum oluşturabilir. Nüfusun tamamının etkilenme olasılığı yüksektir.
- <span style="color:brown">Tehlikeli</span>: Sağlık alarmı: Herkes daha ciddi sağlık etkileri ile karşılaşabilir.
**Kaynak:** https://sim.csb.gov.tr/Home/HKI  
            ''',
        keys.PM10_EXPLANATION: '''
### PM10 Nedir?        
Partikül madde kirliliği veya PM olarak da bilinen partikül madde, havada asılı kalan son derece küçük katı 
partikülleri ve sıvı damlacıklarını tanımlayan bir terimdir. Havadaki partikül madde (PM) tek bir kirletici değildir;
birçok kimyasal türün karışımıdır.  
- PM10(çapı 10 mikrometre veya daha küçük olan parçacıklar): bu parçacıklar boğazdan ve burundan geçip akciğerlere 
girebilecek kadar küçüktür. Bu parçacıklar solunduğunda kalbi ve akciğerleri etkileyebilir ve sağlık üzerinde ciddi 
etkilere neden olabilir.
- 5(çapı 2,5 mikrometre veya daha küçük olan parçacıklar): Bu parçacıklar o kadar küçüktür ki akciğerlerin 
derinliklerine ve kan dolaşımına karışabilirler. Uzun süreler (yıllar) boyunca PM2.5’e maruz kalmanın olumsuz sağlık
 etkilerine neden olabileceğine dair yeterli kanıt bulunmaktadır."  
 **Kaynak:** https://haliccevre.com/partikul-madde-pm10-ve-pm2-5/#:~:text=PM10(%C3%A7ap%C4%B1%2010%20mikrometre%20veya,%C3%BCzerinde%20ciddi%20etkilere%20neden%20olabilir.
        ''',
        keys.SO2_EXPLANATION: '''
### So2 Nedir?
Kükürt dioksit(SO2): Bileşiminde kükürt bulunduran yakıtların yanmasıyla açığa çıkan keskin kokulu bir gazdır.
 Bu, zehirleme özelliği olan gazı çıkaran maddelerin başında kötü kaliteli katı yakıtlar gelmektedir. 
 Bunlar, linyit, asfaltit, fuel-oil ve gazyağı gibi maddelerdir. 
 Yanma ile meydana gelen kükürt dioksit (SO2) miktarı, 
 yanmanın kalitesine ve yakıtın içinde bulunan katkı maddelerine bağlıdır.  
**Kaynak:** https://mugla.csb.gov.tr/hava-kalitesi-izleme-istasyonu-i-91856        
'''
    },



    EN: {
        keys.PAGE_TITLE: 'İzmir Air Quality',
        keys.MAP: 'Map',
        keys.BAR: 'Bar',
        keys.IZMIR_AIR_QUALITY: '🌍 İzmir Air Quality',
        keys.SELECT_A_DATE: 'select a date',
        keys.SELECT_POLLUTANT: 'select pollutant',
        keys.IZMIR_POLLUTANT_DATA: 'İzmir {pollutant} Data',
        keys.ABOUT_COLOR_CODES: 'About color codes',
        keys.DATA_AND_TRENDS: 'Data/Trends',
        keys.NO_DATA: 'No Data',
        keys.VALUE_IS: 'value is',
        keys.PREVIOUS_DAYS_VALUE_IS: "previous day's value is",

        keys.GOOD: 'good',
        keys.MODERATE: 'moderate',
        keys.SENSITIVE: 'unhealthy for sensitive groups',
        keys.UNHEALTHY: 'unhealthy',
        keys.VERY_UNHEALTHY: 'very unhealthy',
        keys.HAZARDOUS: 'hazardous',

        keys.AIR_QUALITY_IS: 'Air quality is',

        keys.HIDE_PREVIOUS_DAYS_VALUE: "Hide Previous Day's Values",
        keys.SHOW_REVIOUS_DAYS_VALUE: "Show Previous Day's Values",

        keys.SORT_BY: 'Sort by',
        keys.DEFAULT: 'Default',
        keys.VALUE: 'Value',
        keys.TREND: 'Trend',
        keys.INCREASING: 'Increasing',
        keys.DECREASING: 'Decreasing',

        keys.COLOR_CODE_EXPLANATION: '''
- <span style="color:green">Good</span>: Air quality is satisfactory, and air pollution poses little or no risk.
- <span style="color:yellow">Moderate</span>: Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution.
- <span style="color:orange">Unhealthy for Sensitive Groups</span>:	Members of sensitive groups may experience health effects. The general public is less likely to be affected.
- <span style="color:red">Unhealthy</span>: Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects.
- <span style="color:purple">Very Unhealthy</span>: Health alert: The risk of health effects is increased for everyone.
- <span style="color:maroon">Hazardous</span>: Health warning of emergency conditions: everyone is more likely to be affected.    
**Source:** https://www.airnow.gov/aqi/aqi-basics/          
        ''',
        keys.PM10_EXPLANATION: '''   
### What is PM10?
"Airborne particulate matter (PM) is not a single pollutant, but rather is a mixture of many chemical species. 
It is a complex mixture of solids and aerosols composed of small droplets of liquid, dry solid fragments,
 and solid cores with liquid coatings. Particles vary widely in size, shape and chemical composition, 
 and may contain inorganic ions, metallic compounds, elemental carbon, organic compounds, 
 and compounds from the earth’s crust. Particles are defined by their diameter for air quality regulatory purposes. 
 Those with a diameter of 10 microns or less (PM10) are inhalable into the lungs and can induce adverse health effects. 
 Fine particulate matter is defined as particles that are 2.5 microns or less in diameter (PM2.5). 
 Therefore, PM2.5 comprises a portion of PM10."  
 **Source:** [The California Air Resources Board](https://ww2.arb.ca.gov/resources/inhalable-particulate-matter-and-health)
        ''',
        keys.SO2_EXPLANATION: '''
### What is SO2?        
"Sulfur dioxide (SO2), a foul-smelling toxic gas, is part of a larger group of chemicals called sulfur oxides. 
These gases, especially SO2, are emitted by the burning of fossil fuels or other materials that contain sulfur.  
Sulfur dioxide can damage trees and plants, inhibit plant growth, and damage sensitive ecosystems and waterways. 
It also can contribute to respiratory illness and aggravate existing heart and lung conditions."
**Source:** https://www.pca.state.mn.us/pollutants-and-contaminants/sulfur-dioxide
        '''

    }
}


def get_string_dict(language):
    return _string_res[language]
