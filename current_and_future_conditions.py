"""
organise current internal conditions
# use machine learning to forecast internal conditions based on weather conditons and
# time of day

"""
import pickle, numpy, urllib2, json, time, pandas, datetime

def call_weather_api():
	""" Call this once a day - London should provide a static geolookup """
	f = urllib2.urlopen('http://api.wunderground.com/api/7687a5aed195a60d/hourly10day/q/UK/London.json')
	json_string = f.read()
	parsed_json_hour = json.loads(json_string)
	return parsed_json_hour
	
def weather_to_pandas():
	parsed_json_hour = vall_weather_api()
	dts = []
	df_weather = pandas.DataFrame(columns = ['ts','wspd','humidity','tempe', 'icon'])
	for time_period in range(0,len(parsed_json_hour['hourly_forecast'])):
		#a = parsed_json_hour['hourly_forecast'][time_period]['FCTTIME']['pretty']
		year = int(parsed_json_hour['hourly_forecast'][time_period]['FCTTIME']['year'])
		month = int(parsed_json_hour['hourly_forecast'][time_period]['FCTTIME']['mon'])
		day = int(parsed_json_hour['hourly_forecast'][time_period]['FCTTIME']['mday'])
		hour = int(parsed_json_hour['hourly_forecast'][time_period]['FCTTIME']['hour'])
		minute = int(parsed_json_hour['hourly_forecast'][time_period]['FCTTIME']['min'])
		
		timestamp = datetime.datetime(year,month, day, hour, minute)
		wspd = int(parsed_json_hour['hourly_forecast'][time_period]['wspd']['metric']) *0.27777777777778
		humi = int(parsed_json_hour['hourly_forecast'][time_period]['humidity']) 
		temp = int(parsed_json_hour['hourly_forecast'][time_period]['temp']['metric']) 
		icon = parsed_json_hour['hourly_forecast'][time_period]['icon_url']
		df_weather.loc[len(df_weather)] = [timestamp,wspd,humi,temp, icon]
		# pandas has issues with storing timestamps sometimes
		dts.append(timestamp)
	return df_weather, dts
	
def plot_timeseries_forecast(df_weather, dts):
	trace = go.Scatter(x=dts,y=df_weather['humidity'].values, name = 'Humidity %')
	trace1 = go.Scatter(x=dts,y=df_weather['tempe'].values, name = 'Temperature C', yaxis='y2')
	layout = go.Layout(title ='Denmark Road External Condition Forecast', yaxis = dict(title='Humidity %'), yaxis2 = dict(title='oC', overlaying='y',side ='right'))
	data=[trace, trace1]
	fig = go.Figure(data=data, layout=layout)
	plotly.offline.plot(fig, filename = 'daily_forecast.html')
	
def extract_hourly_conditions(df_weather):
    """Get conditions for website."""
    now  = datetime.datetime(datetime.datetime.now().year,datetime.datetime.now().month,datetime.datetime.now().day, datetime.datetime.now().hour,0)
    df_now = df_weather.loc[df_weather['ts'] == now]
    t = df_now['tempe'].values[0]
    h = df_now['humidity'].values[0]
    icon = df_now['icon'].values[0]
    return t,h,icon

def read_cur_con():
    """Extract the latest internal values"""
    cur_hum = pandas.read_csv('humidity_basement_latest_value.csv')
    cur_temp = pandas.read_csv('temperature_basement_latest_value.csv')
    ch = cur_hum['relative_humidity'].values[0]
    ct = cur_temp['temperature_in_celsius'].values[0]
    return ch, ct
    
def define_window_strategy(internal_t, internal_h, external_t, external_h):
    humid_sum = internal_h - external_h
    temp_sum = internal_t - external_t
    
    if humid_sum <0:
        delta_h ='moister air outside'
    else:
        delta_h = 'moister air inside'
        
    if temp_sum <0:
        delta_t = 'warmer outsise'
    else:
        delta_t = 'warmer inside'
    return delta_h, delta_t    

